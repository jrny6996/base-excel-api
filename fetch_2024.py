import requests
import csv

url = "https://base-excel.vercel.app/api/2024"
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

for month in pur_data:
    print( month)
    # Write purchases data
    with open(f"{month}_purchases.csv", mode='w', newline='', encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=pur_data[month][0].keys())
        writer.writeheader()
        writer.writerows(pur_data[month])

# Write customers data
with open("customers.csv", mode='w', newline='', encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=cus_data[0].keys())
    writer.writeheader()
    writer.writerows(cus_data)

# Write employees data
with open("employees.csv", mode='w', newline='', encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=emp_data[0].keys())
    writer.writeheader()
    writer.writerows(emp_data)

print("success")