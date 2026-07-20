import json

sampleJson = """{
   "company":{
      "employee":{
         "name":"emma",
         "payable":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


#Parse the JSON string using json.loads()
data = json.loads(sampleJson) #load string to dictionary

print(f"Salary: {data['company']['employee']['payable']['salary']}")
data['company']['employee']['birthdate'] = "1990-01-01" #add new key-value pair

with open("employee.json","w") as f:
    json.dump(data, f, indent=2) #dump dictionary to file with indentation
    print("Modified data saved to employee.json")

with open("employee.json", "r") as f:
    verified = json.load(f) #load file to dictionary 

print(f"Verified birthdate: {verified['company']['employee']['birthdate']}")
