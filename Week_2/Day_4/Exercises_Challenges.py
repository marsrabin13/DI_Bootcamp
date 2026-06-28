# Exercise 1
# Instructions
# Write a script that inserts an item at a defined index in a list.

list1 = [1, 2, 3, 4, 5]
print("Original list:", list1)
def insert_item_at_index(temp_list, index, item):
    temp_list.insert(index, item)
    return temp_list

list1 = insert_item_at_index(list1, 2, 99)
print("New list:", list1)

# Exercise 2
# Instructions
# Write a script that counts the number of spaces in a string.

def count_spaces(input_string):
    space_count = input_string.count(' ')
    return space_count

input_str = input("Enter a string: ")
print(f"Number of spaces: {count_spaces(input_str)}")

# Exercise 3
# Instructions
# Write a script that calculates the number of upper case letters and lower case letters in a string.

def count_upper_lower(input_string):
    upper_count = 0
    lower_count = 0
    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

input_str = input("Enter a string: ")
upper, lower = count_upper_lower(input_str)
print(f"Number of uppercase letters: {upper}")
print(f"Number of lowercase letters: {lower}")


# Exercise 4
# Instructions
# Write a function to find the sum of an array without using the built in function:
# >>>my_sum([1,5,4,2])
# >>>12

def my_sum(num_array):
    total = 0
    for num in num_array:
        total += num
    return total


# Exercise 5
# Instructions
# Write a function to find the max number in a list
# >>>find_max([0,1,3,50])
# >>>50

def find_max(num_list):
    return max(num_list) 

print(find_max([0, 1, 3, 50]))

# Exercise 6
# Instructions
# Write a function that returns factorial of a number
# >>>factorial(4)
# >>>24

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

print(factorial(4))

# Exercise 7
# Instructions
# Write a function that counts an element in a list (without using the count method):
# >>>list_count(['a','a','t','o'],'a')
# >>>2

def list_count(input_list, element):
    count = 0
    for item in input_list:
        if item == element:
            count += 1
    return count

list_count_result = list_count(['a', 'a', 't', 'o'], 'a')
print(list_count_result)


# Exercise 8
# Instructions
# Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:
# >>>norm([1,2,2])
# >>>3

def l2_norm(num_list):
    sum_of_squares = sum(x ** 2 for x in num_list)
    return sum_of_squares ** 0.5

print(l2_norm([1, 2, 2]))  # Output: 3.0

# Exercise 9
# Instructions
# Write a function to find if an array is monotonic (sorted either ascending of descending)

def is_mono(num_list):
    if num_list == sorted(num_list) or num_list == sorted(num_list, reverse=True):
        return True
    return False

print(is_mono([7, 6, 5, 5, 2, 0]))
print(is_mono([7, 6, 8, 5, 2, 0]))



# Exercise 10
# Instructions
# Write a function that prints the longest word in a list.

def longest_word(list_of_words):
    longest = ""
    for word in list_of_words:
        if len(word) > len(longest):
            longest = word
    return longest

print(longest_word(["apple", "banana", "cherry", "date"]))


# Exercise 11
# Instructions
# Given a list of integers and strings, put all the integers in one list, and all the strings in another one.

def separate_types(mixed_list):
    int_list = []
    str_list = []
    for item in mixed_list:
        if isinstance(item, int):
            int_list.append(item)
        elif isinstance(item, str):
            str_list.append(item)
    return int_list, str_list

print(separate_types([1, 'hello', 2, 'world', 3, 'python']))
