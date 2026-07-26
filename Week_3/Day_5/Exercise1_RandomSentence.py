# 🌟 Exercise 1 — Random Sentence Generator
import random
from pathlib import Path
import json

def get_words_from_file(file_path):
    file_path = Path(__file__).parent / "words.txt"
    with open(file_path, "r") as f:
        content = f.read()
    return content.split()

def get_random_sentence(length):
    words = get_words_from_file("words.text")
    chosen = [random.choice(words) for _ in range(length)]
    return " ".join(chosen)

def main():
    # get input, validate, generate sentence
    try: 
        length = int(input("Enter sentence length (2-20): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    if length < 2 or length > 20:
        print("Length must be between 2 and 20.")
        return
    
    sentence = get_random_sentence(length)
    print(f"Random sentence: {sentence}")   

main()

#Exercise 2 — JSON Manipulation

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
