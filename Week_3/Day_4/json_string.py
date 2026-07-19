import json

json_string = '{"name": "John", "age": 30, "city": "New York"}'

data = json.loads(json_string) #load string to dictionary

print(f"Type of data: {type(data)}")
print(f"Name: {data['name']}")

person = {"name": "John",
          "age": 30, 
          "city": "New York",
          "score": None}

ugly = json.dumps(person)  # Convert dictionary to JSON string
print(f"Ugly JSON person: {ugly}")

pretty = json.dumps(person, indent=2)
print(f"Pretty:   {pretty}")
