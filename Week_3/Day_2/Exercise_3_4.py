# 🌟 Exercise 3: Dogs Domesticated
# Goal: Create a PetDog class that inherits from Dog and adds training and tricks.



# Key Python Topics:

# Inheritance
# super() function
# *args
# Random module


# Instructions:

# Step 1: Import the Dog Class

# In a new Python file, import the Dog class from the previous exercise.
import random


class Dog:
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return f"{self.name} wins the fight!"
        else:
            return f"{other_dog.name} wins the fight!"

# Step 2: Create the PetDog Class

# Create a class called PetDog that inherits from the Dog class.
# Add a trained attribute to the __init__ method, with a default value of False.
# trained means that the dog is trained to do some tricks.
# Implement a train() method that prints the output of bark() and sets trained to True.
# Implement a play(*args) method that prints “<dog_names> all play together”.
# *args on this method is a list of dog instances.
# Implement a do_a_trick() method that prints a random trick if trained is True.
# Use this list for the ramdom tricks:
# tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
# Choose a random index from it each time the method is called.

class PetDog(Dog):
    def __init__(self,name,age,weight):
        super().__init__(name,age,weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")

    def play(self, *args):
        dog_names = [self.name] + [dog.name for dog in args]
        print(f"{','.join(dog_names)} all play together")


# Step 3: Test PetDog Methods

# Create instances of the PetDog class and test the train(), play(*args), and do_a_trick() methods.

dog1 = PetDog("Buddy", 3, 20)
dog2 = PetDog("Max", 4, 25)
dog3 = PetDog("Bella", 2, 15)
dog1.train()
dog1.do_a_trick()
dog1.play(dog2, dog3)

# Example:

# # In a new file
# # import the Dog class

# class PetDog(Dog):
#     def __init__(self, name, age, weight): <mark> no need to put the details in the function, you are giving the solution</mark>
#         super().__init__(name, age, weight)
#         self.trained = False

#     def train(self): <mark> no need to put the details in the function, you are giving the solution</mark>
#         print(self.bark())
#         self.trained = True

#     def play(self, *args):
#         # ... code to print play message ...

#     def do_a_trick(self): <mark> no need to put the details in the function, you are giving the solution</mark>
#         if self.trained:
#             tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
#             print(f"{self.name} {random.choice(tricks)}")

# # Test PetDog methods
# my_dog = PetDog("Fido", 2, 10)
# my_dog.train()
# my_dog.play("Buddy", "Max")
# my_dog.do_a_trick()


# 🌟 Exercise 4: Family and Person Classes
# Goal:

# Practice working with classes and object interactions by modeling a family and its members.



# Key Python Topics:

# Classes and objects
# Instance methods
# Object interaction
# Lists and loops
# Conditional statements (if/else)
# String formatting (f-strings)


# Instructions:

# Step 1: Create the Person Class

# Define a Person class with the following attributes:
# first_name
# age
# last_name (string, should be initialized as an empty string)
# Add a method called is_18():
# It should return True if the person is 18 or older, otherwise False.

class Person:
    def __init__(self, first_name,age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18
    


# Step 2: Create the Family Class

# Define a Family class with:
# A last_name attribute
# A members list that will store Person objects (should be initialized as an empty list)

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []


# Add a method called born(first_name, age):
# It should create a new Person object with the given first name and age.
# It should assign the family’s last name to the person.
# It should add this new person to the members list.

    def born(self, first_name,age):
        new_member = Person(first_name,age)
        new_member.last_name = self.last_name
        self.members.append(new_member)


# Add a method called check_majority(first_name):
# It should search the members list for a person with that first_name.
# If the person exists, call their is_18() method.
# If the person is over 18, print:
# "You are over 18, your parents Jane and John accept that you will go out with your friends"
# Otherwise, print:
# "Sorry, you are not allowed to go out with your friends."

    def check_majority(self,first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(f"{member.first_name}, You are over 18, your parents accept that you will go out with your friends")
                else:
                    print(f"{member.first_name}, Sorry, you are not allowed to go out with your friends.")


# Add a method called family_presentation():
# It should print the family’s last name.
# Then, it should print each family member’s first name and age.

    def family_presentation(self):
        print(f"Family Last Name: {self.last_name}")
        for member in self.members:
            print(f"Member: {member.first_name}, Age: {member.age}")


# Expected Behavior:

# Once implemented, your program should allow you to:

# Create a family with a last name.
# Add members to the family using the born() method.
# Use check_majority() to see if someone is allowed to go out.
# Display family information with family_presentation().
# Don’t forget to test your classes by creating an instance of Family, adding members, and calling each method to see the expected output.

family1 = Family("Smith")
family1.born("Alice", 20)
family1.born("Bob", 17)
family1.born("Andrew", 25)

for member in family1.members:
    family1.check_majority(member.first_name)

family1.family_presentation()