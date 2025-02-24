import argparse
import pandas as pd
import warnings
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

warnings.filterwarnings("ignore")
load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")
DATABASE_PATH = "data/textfiles/database.txt"
USER_ACCESS_PATH = "data/Behavior/BBAC_attributes.csv"

PROMPT_TEMPLATE = """
You are the company's chat assistant and your job is to answer questions for employees based on their allowed access.
Answer the question taking reference from the following context:

{context}

---

Answer the question based on the above context if relevant, otherwise answer: {question}

{access_prompt}
"""

def read_database():
    """Read and return the content of the database.txt file."""
    with open(DATABASE_PATH, "r") as file:
        return file.read()

def get_user_access(person_name):
    access_data = pd.read_csv(USER_ACCESS_PATH)
    user_data = access_data[access_data['person_name'] == person_name]
    
    if user_data.empty:
        return None
    return user_data.iloc[0]  # Return first matching row

def check_access(person_name, query_time, query_location):
    user_data = get_user_access(person_name)
    
    if user_data is None:
        return False, "User not found. Access denied."
    
    allowed_time = user_data['Time']
    allowed_location = user_data['Location']
    
    if query_time != allowed_time or query_location != allowed_location:
        return False, "Access denied due to location or time restriction."
    
    return True, user_data['Information_Access']

def generate_access_prompt(person_name, information_access):
    return (f"The user '{person_name}' has access to the following information:\n"
            f"{information_access}.\n\n"
            "Ensure the user only receives the allowed information. Do not provide restricted details.")

def get_response(person_name, query_text, query_time, query_location):
    has_access, info_access = check_access(person_name, query_time, query_location)
    
    if not has_access:
        return info_access  # Return denial message
    
    context_text = read_database()
    access_prompt = generate_access_prompt(person_name, info_access)
    
    model = ChatGoogleGenerativeAI(
        google_api_key=google_api_key,
        model="gemini-pro"
    )
    prompt = PROMPT_TEMPLATE.format(context=context_text, question=query_text, access_prompt=access_prompt)
    response_text = model.predict(prompt)
    
    return f"\nResponse: {response_text}\n\nSource: database.txt\n"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("person_name", type=str, help="The person's name.")
    parser.add_argument("query_text", type=str, help="The query text.")
    parser.add_argument("query_time", type=str, help="The query time.")
    parser.add_argument("query_location", type=str, help="The query location.")
    args = parser.parse_args()
    
    response = get_response(args.person_name, args.query_text, args.query_time, args.query_location)
    print(response)

if __name__ == "__main__":
    main()