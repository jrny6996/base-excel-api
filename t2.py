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