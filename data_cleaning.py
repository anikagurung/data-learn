
# Data Cleaning Practice

# Sample employee data
employees = [
    {"name": " Anika ", "age": "24", "salary": "50000"},
    {"name": " Rahul ", "age": "27", "salary": "60000"},
    {"name": " Priya ", "age": "", "salary": "55000"},
    {"name": " John ", "age": "30", "salary": ""},
    {"name": " Sara ", "age": "26", "salary": "65000"}
]

cleaned_data = []

# Clean employee records
for employee in employees:

    name = employee["name"].strip()
    age = employee["age"]
    salary = employee["salary"]

    # Skip records with missing values
    if name == "" or age == "" or salary == "":
        continue

    # Convert string values into integers
    age = int(age)
    salary = int(salary)

    # Store cleaned records
    cleaned_employee = {
        "name": name,
        "age": age,
        "salary": salary
    }

    cleaned_data.append(cleaned_employee)

# Display cleaned data
print("Cleaned Employee Data:")

for employee in cleaned_data:
    print(employee)

print("Total Clean Records:", len(cleaned_data))
