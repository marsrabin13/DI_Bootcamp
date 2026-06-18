# 🌟 Exercise 1: Favorite Numbers
# Key Python Topics:

# Sets
# Adding/removing items in a set
# Set concatenation (using union)


# Instructions:

# Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
my_fav_numbers = [1,3,7,21]
my_fav_numbers = [1,3,7,21] + [2,4]
print(my_fav_numbers)

# Remove the last number you added to the set.
print(my_fav_numbers.pop())
print(my_fav_numbers)

# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
friend_fav_numbers = [2,4,6]
print(friend_fav_numbers)

# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
our_fav_numbers = set(my_fav_numbers + friend_fav_numbers)
print(our_fav_numbers)

# Note: Sets are unordered collections, so ensure no duplicate numbers are added.


# 🌟 Exercise 2: Tuple
# Key Python Topics:

# Tuples (immutability)
# Instructions:

# Given a tuple of integers, try to add more integers to the tuple.
# Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.
int_tuple = (1,2,3,4)
print(int_tuple)
int_list = list(int_tuple)
int_list.append(5)
int_tuple = tuple(int_list)
print(int_tuple)

# 🌟 Exercise 3: List Manipulation
# Key Python Topics:

# Lists
# List methods: append, remove, insert, count, clear


# Instructions:

# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# Remove "Banana" from the list.
basket.remove("Banana")
#print(basket)

# Remove "Blueberries" from the list.
basket.remove("Blueberries")
#print(basket)

# Add "Kiwi" to the end of the list.
basket.append("Kiwi")
#print(basket)

# Add "Apples" to the beginning of the list.
basket.insert(0,"Apples")
#print(basket)

# Count how many times "Apples" appear in the list.
print("Apples count:",basket.count("Apples"))

# Empty the list.
basket.clear()
print(basket)
# Print the final state of the list.


# 🌟 Exercise 4: Floats
# Key Python Topics:

# Lists
# Floats and integers
# Range generation


# Instructions:

# Recap: What is a float? What’s the difference between a float and an integer?
# Create a list containing the following sequence of mixed types: floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?
mixed_list = []
start_num = 1

for n in range(10):
    print(start_num) 
    if start_num % 2 == 0:
        mixed_list.append(int(start_num))
    else:
        mixed_list.append(start_num)
    start_num += 0.5
    

print(mixed_list) 


# 🌟 Exercise 5: For Loop
# Key Python Topics:

# Loops (for)
# Range and indexing


# Instructions:

# Write a for loop to print all numbers from 1 to 20, inclusive.
for n in range(1,21):
    print(n)

# Write another for loop that prints every number from 1 to 20 where the index is even.
for n in range(1,21):
    if n%2 == 0:
        print(n)


# 🌟 Exercise 6: While Loop
# Key Python Topics:

# Loops (while)
# Conditionals


# Instructions:

# Use an input to ask the user to enter their name.

# Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
# hint: check for the method isdigit()
# if the input is incorrect, keep asking for the correct input until it is correct
# if the input is correct print “thank you” and break the loop

while True: 
    usr_name = input("Enter your name: ")
    if len(usr_name) < 3:
        print("Name should be more than 3 character.Try again.")
    elif usr_name.isdigit():
        print("Name should noy be digits.Try again.")
    elif usr_name.isalpha():
        print("Thank you!")
        break
    else:
        print("Invalid name.Try again.")



# 🌟 Exercise 7: Favorite Fruits
# Key Python Topics:

# Input/output
# Strings and lists
# Conditionals


# Instructions:

# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"

fav_fruits = list(input("Enter your favorite fruits (separate by spaces):").split(" "))
any_fruit = input("Enter any fruit:")
if any_fruit in fav_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

# 🌟 Exercise 8: Pizza Toppings
# Key Python Topics:

# Loops
# Lists
# String formatting


# Instructions:

# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.

pizza_order = []
while True:
    pizza_topping = input("Enter pizza toppings one by one.Type quit once you're done.")
    if pizza_topping == "quit":
        break
    elif pizza_topping:
        pizza_order.append(pizza_topping)
        print(f"Adding {pizza_topping} to your pizza: ")

print(f"All the toppings are {", ".join(pizza_order)}. Total cost is ${10 + 2.50*len(pizza_order)}.")


# 🌟 Exercise 9: Cinemax Tickets
# Key Python Topics:

# Conditionals
# Lists
# Loops


# Instructions:

# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.




fam_age_list = list(input("Enter ages of all family members:").split(" "))
#print(fam_age_list)
fam_age_int = [int(x) for x in fam_age_list]
#print(fam_age_int)
tot_cost = 0

for age in fam_age_int:
    if age < 3:
        continue
    elif age >= 3 and age <= 12: 
        tot_cost += 10
    elif age > 12:
        tot_cost += 15

print(f"Total ticket cost is {tot_cost}.")

# Bonus:

# Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
# Write a program to:
# Ask for each person’s age.
# Remove anyone who isn’t allowed to watch.
# Print the final list of attendees.
