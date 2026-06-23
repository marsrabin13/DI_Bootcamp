
# Challenge 1: Multiples of a Number


# Key Python Topics:
# input() function
# Loops (for or while)
# Lists and appending items
# Basic arithmetic (multiplication)


# Instructions:
# 1. Ask the user for two inputs:

# A number (integer).
# A length (integer).
# 2. Create a program that generates a list of multiples of the given number.
# 3. The list should stop when it reaches the length specified by the user.

number = int(input("Enter an integer: "))
length = int(input("Enter lenght of list: "))
number_list = []

for items in range(1,length+1):
    number_list.append(number*items)
    items+=1

print(number_list)

# Example 1:

# Input:

# number: 7
# length: 5
# Output:
# [7, 14, 21, 28, 35]



# Example 2:

# Input:

# number: 12
# length: 10
# Output:
# [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]



# Example 3:

# Input:

# number: 17
# length: 6
# Output:
# [17, 34, 51, 68, 85, 102]



# Challenge 2: Remove Consecutive Duplicate Letters


# Key Python Topics:
# input() function
# Strings and string manipulation
# Loops (for or while)
# Conditional statements (if)


# Instructions:
# 1. Ask the user for a string.
# 2. Write a program that processes the string to remove consecutive duplicate letters.

# The new string should only contain unique consecutive letters.
# For example, “ppoeemm” should become “poem” (removes consecutive duplicates like ‘pp’, ‘ee’, and ‘mm’).
# 3. The program should print the modified string.

str = input("Give a string: ")
result = "".join(dict.fromkeys(str))
print(result)
# Example 1:

# Input:
# user’s word: "ppoeemm"
# Output:
# "poem"


# Example 2:

# Input:
# user’s word: "wiiiinnnnd"
# Output:
# "wind"


# Example 3:

# Input:
# user’s word: "ttiiitllleeee"
# Output:
# "title"


# Example 4:

# Input:
# user’s word: "cccccaaarrrbbonnnnn"
# Output:
# "carbon"