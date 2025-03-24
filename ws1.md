# Intro to Python

## Basic Python Syntax

Python syntax is designed to be readable and straightforward. Let’s walk through some basics:

### Variables and Data Types

```python
name = "Alice"
age = 25
height = 5.6
is_student = True
```

- Strings (`str`): Text values like "Alice".
- Integers (`int`): Whole numbers like 25.
- Floats (`float`): Decimal numbers like 5.6.
- Booleans (`bool`): True/False values.

### Control Structures

```python
age = 25
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### Loops

```python
for i in range(5):
    print(i)
```

### Functions

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

## Data on the internet

Most modern apps communicate with servers and APIs using data formats like JSON. Python’s `requests` library helps fetch and send data easily.

```python
import requests

response = requests.get("https://api.example.com/data")
if response.status_code == 200:
    print(response.json())
```

## Shape of our data

The data we’re working with often looks like this JSON structure:

```json
{
  "customers": [
    {
      "address": "123 Maple Street",
      "created_at": "2025-02-17 14:30:04",
      "customer_id": 1,
      "email": "alice.johnson@example.com",
      "name": "Alice Johnson"
    }
  ],
  "purchases": [
    {
      "customer_id": 1,
      "employee_id": 1,
      "product_id": 1,
      "purchase_date": "2024-01-01 10:30:00",
      "purchase_id": 1,
      "quantity": 1,
      "total_price": 1200.0
    }
  ],
  "employees": [
    {
      "created_at": "2025-02-17 14:27:18",
      "employee_id": 1,
      "hire_date": "2023-05-10",
      "name": "Emma Wilson",
      "position": "Sales Associate"
    }
  ]
}
```

This structure is nested — a dictionary containing lists of dictionaries.

## Converting JSON

We can fetch this data and convert it into a more familiar format, like CSV.

```python
import requests
import csv

url = "https://base-excel.vercel.app/api/january"
data = {"key": 1234}
response = requests.post(url, json=data)

data = response.json()

# Extract data
pur_data = data["purchases"]
cus_data = data["customers"]
emp_data = data["employees"]

# Write purchases data
with open("purchases.csv", mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=pur_data[0].keys())
    writer.writeheader()
    writer.writerows(pur_data)

# Write customers data
with open("customers.csv", mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=cus_data[0].keys())
    writer.writeheader()
    writer.writerows(cus_data)

# Write employees data
with open("employees.csv", mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=emp_data[0].keys())
    writer.writeheader()
    writer.writerows(emp_data)
```

### Explanation

- `requests.post()` sends data to the API.
- `response.json()` converts the API response to a Python dictionary.
- `csv.DictWriter` writes this data into clean, organized CSV files.

## Why CSV?

CSV (Comma Separated Values) files are widely supported by spreadsheet programs like Excel, Google Sheets, and others. While JSON is excellent for web data and APIs, it's not immediately usable in Excel without additional parsing. By converting the data to CSV, we get several benefits:

- **Ease of Use:** Excel can open CSV files directly without any extra configuration.
- **Data Analysis:** Once in Excel, you can sort, filter, and apply formulas easily.
- **Portability:** CSV files are lightweight and universally compatible.
- **Human-Readable:** Each row represents a record, making the data visually intuitive.

This conversion allows non-programmers to explore and analyze data without writing code — a crucial step in making data accessible to everyone.

## Final thoughts

Python’s ability to interact with web data and structure it neatly is one of its superpowers. Now you’re equipped to fetch data, explore its structure, and convert it into a usable format — all core steps in data analysis and automation.
