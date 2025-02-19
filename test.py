import requests
import csv

url = "https://base-excel.vercel.app/api/january"
data = {"key": 1234}
response = requests.post(url, json=data)

if response.status_code == 200:
    data = response.json()
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    exit()

# Extract data
pur_data = data["purchases"]
cus_data = data["customers"]
emp_data = data["employees"]

# Write purchases data
with open("purchases.csv", mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=pur_data[0].keys())
    writer.writeheader()
    writer.writerows(pur_data)

# Write unique customers data
unique_customers = {frozenset(item.items()): item for item in cus_data}.values()
with open("customers.csv", mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=cus_data[0].keys())
    writer.writeheader()
    writer.writerows(unique_customers)

# Write unique employees data
unique_employees = {frozenset(item.items()): item for item in emp_data}.values()
with open("employees.csv", mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=emp_data[0].keys())
    writer.writeheader()
    writer.writerows(unique_employees)
