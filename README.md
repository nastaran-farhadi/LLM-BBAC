# Behavior Based Access Control in Large Language Models

This code repository contains implementations and experiments with various approaches to Behavior-based access control in Large Language Models. I’ve explored techniques such as RAG and fine-tuning to accomplish this. With RAG, an intermediary layer is created between the user and the LLM, serving as a system to enforce Behavior-based access control.

## Table of Contents
- [Installation](#installation)
- [SetUp](#setup)
- [Usage](#usage)

### Installation & Requirements

The following commands need to be run in order to run the project:
```
!pip install faker
!pip install pandas
!pip install -U langchain-openai
!pip install python-magic
!pip install unstructured
!pip install chromadb
!pip install langchain-community
!pip install python-dotenv
!pip install matplotlib
!pip install seaborn
```

### Setup
Follow these steps to set up the project on your local machine:

1. Clone the repository:
   ```bash
   git clone [https://github.com/aiqqia/LLM-RBAC.git](https://github.com/nastaran-farhadi/LLM-BBAC)
   cd LLM-BBAC
   ```

### Usage

Running these files to generate relevant files for testing:

1. Run this to generate synthetic database for employee records:
```
python3 data_gen.py
```
2. Run this to create a CSV file for all persons, and its access information:
```
python3 attributes_gen.py
```
3. Run this to vectorize the entire database into chunks and store it in the Chroma database:
```
python3 generate_database.py
4. Import Model of LLM and API key
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key="")

# Initialize the model
GEMINI_MODEL = genai.GenerativeModel('gemini-pro')
```
5. Import necessary libraries:
!pip install langchain-google-genai
import os
from langchain_google_genai import ChatGoogleGenerativeAI
```

6. Finally, we can query the interface and provide the person_name and ask it any question:
```
python query_data.py "Person_name" "My question" "Time" "Location"   
```

Example: 
```
python query_data.py "John Doe" "What is Victoria Vasquez's salary?" "Working Hours" "In the Department"
```

