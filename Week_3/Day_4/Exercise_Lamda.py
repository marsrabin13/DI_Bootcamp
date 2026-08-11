people = []

for i in range(5):
    name = input("Name: ")
    age = input("Age: ")
    score = input("Score: ")
    people.append((name, age, score))

# The lambda builds the sort key: name first, then age, then score
people.sort(key=lambda person: (person[0], person[1], person[2]))

print(people)