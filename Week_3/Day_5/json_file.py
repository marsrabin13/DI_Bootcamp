import json

student_data = {
  "name": "Charlie",
  "grades": [85, 92, 78, 95],
  "graduated": False
}

with open("student.json", "w") as f:
    json.dump(student_data, f, indent=2)

print("Wrote student.json")

with open("student.json", "r") as f:
    loaded = json.load(f)

print(f"Loaded: {loaded}")
print(f"Name: {loaded['name']}")