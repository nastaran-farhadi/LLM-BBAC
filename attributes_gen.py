import csv

# Define the roles and their access details as a list of dictionaries
roles_data = [
    {
        "person_name": "John Doe",
        "Role": "Administrator",
        "Permissions": "Full access: Read, Write, Execute, Manage Users",
        "Information_Access": "All Information: Access to all systems, configuration data, user accounts, logs, financial records, HR data, and authority to modify security policies, roles, and access rules.",
        "Time": "Working Hours",
        "Location": "In the Department"
    },
    {
        "person_name": "Jane Smith",
        "Role": "IT Support",
        "Permissions": "Read, Execute, Troubleshoot",
        "Information_Access": "System Logs, User Accounts: Diagnostic data, system performance reports, user technical support data, but no access to confidential HR or financial information.",
        "Time": "Night Shift",
        "Location": "Home"
    },
    {
        "person_name": "Mike Johnson",
        "Role": "Security Officer",
        "Permissions": "Read, Monitor, Execute, Configure Security Policies",
        "Information_Access": "Access Logs, Security Policies, Encryption Keys: Focus on security events, audit logs, and role compliance monitoring.",
        "Time": "Weekend",
        "Location": "In the Department"
    },
    {
        "person_name": "Emily Davis",
        "Role": "Compliance Officer",
        "Permissions": "Read, Monitor",
        "Information_Access": "Audit Logs, Access Logs, Compliance Reports: Access to audit reports for regulatory compliance, and user behavior monitoring logs.",
        "Time": "Working Hours",
        "Location": "Home"
    },
    {
        "person_name": "Laura Wilson",
        "Role": "HR Manager",
        "Permissions": "Read, Write",
        "Information_Access": "Employee Data, Payroll Information, Benefits Data: Manage employee personal records, performance reviews, but no access to system or financial logs.",
        "Time": "Working Hours",
        "Location": "In the Department"
    },
    {
        "person_name": "Robert Brown",
        "Role": "Finance Manager",
        "Permissions": "Read, Write, Approve Payments",
        "Information_Access": "Financial Records, Payroll Data, Budget Reports: Access to company accounts, budgets, payroll, but no access to employee personal data or system logs.",
        "Time": "Working Hours",
        "Location": "In the Department"
    },
    {
        "person_name": "Michael Clark",
        "Role": "Project Manager",
        "Permissions": "Read, Write, Approve",
        "Information_Access": "Project Plans, Budget Forecasts, Employee Performance (limited): Oversee project-related data, budget forecasts, timelines, with limited access to team-specific HR data.",
        "Time": "Working Hours",
        "Location": "Home"
    },
    {
        "person_name": "Sophia Miller",
        "Role": "Developer",
        "Permissions": "Read, Write Code, Access Development Tools",
        "Information_Access": "Source Code, Technical Documentation, Development Data: Access to code repositories, project documentation, product blueprints, but no access to financial or employee personal data.",
        "Time": "Night Shift",
        "Location": "Home"
    },
    {
        "person_name": "William Martinez",
        "Role": "Salesperson",
        "Permissions": "Read, Update CRM",
        "Information_Access": "Customer Data, Sales Reports, Product Catalog: Access to customer details, sales records, CRM tools, but no access to HR, financial, or technical data.",
        "Time": "Weekend",
        "Location": "In the Department"
    },
    {
        "person_name": "Olivia Taylor",
        "Role": "Marketing Team",
        "Permissions": "Read, Write Campaign Data, Analyze Metrics",
        "Information_Access": "Customer Segments, Campaign Data, Website Analytics: Access to customer targeting, marketing data, campaign effectiveness, but no access to financial or HR data.",
        "Time": "Working Hours",
        "Location": "Home"
    }
]


# Write data to CSV
csv_file = "data/roles/rbac_roles.csv"

# Open file and write
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["person_name","Role", "Permissions", "Information_Access", "Time", "Location"])
    
    # Write header
    writer.writeheader()
    
    # Write rows from roles_data
    for person in roles_data:
        writer.writerow(person)


print(f"RBAC roles and access data successfully written to {csv_file}")
