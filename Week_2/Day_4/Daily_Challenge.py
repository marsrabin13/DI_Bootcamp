# Challenge 1: Sorting
# Instructions:
# Write a Python program that takes a single string of words as input, where the words are separated by commas (e.g., ‘apple,banana,cherry’). The program should output these words sorted in alphabetical order, with the sorted words also separated by commas.
# Step 1: Get Input

# Use the input() function to get a string of words from the user.
# The words will be separated by commas.

def get_input():
    user_input = input("Enter a list of words separated by commas: ")
    return user_input


# Step 2: Split the String
def split_string(input_string):
    word_list = input_string.split(",")
    return word_list


# Step 3: Sort the List
def sort_list(word_list):
    sorted_list = sorted(word_list)
    return sorted_list



# Step 4: Join the Sorted List
def join_list(sorted_list):
    new_str = ",".join(sorted_list)
    return new_str



# Step 5: Print the Result
get_input_string = get_input()
split_list = split_string(get_input_string)
sorted_list = sort_list(split_list)
new_str = join_list(sorted_list)
print(f"Sorted list: {new_str}") 


# Expected Output:

# If the input is without,hello,bag,world, the output should be bag,hello,without,world.


# Challenge 2: Longest Word

# Instructions:

# Write a function that takes a sentence as input and returns the longest word in the sentence. If there are multiple longest words, return the first one encountered. Characters like apostrophes, commas, and periods should be considered part of the word.
# Step 1: Define the Function

# Define a function that takes a string (the sentence) as a parameter.

# Step 2: Split the Sentence into Words



# Step 3: Initialize Variables



# Step 4: Iterate Through the Words



# Step 5: Compare Word Lengths



# Step 6: Return the Longest Word



# Expected Output:

# longest_word("Margaret's toy is a pretty doll.") should return "Margaret's".
# longest_word("A thing of beauty is a joy forever.") should return "forever.".
# longest_word("Forgetfulness is by all means powerless!") should return "Forgetfulness".


def input_sentence():
    sentence = input("Enter a sentence: ")
    return sentence

def longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

input_str = input_sentence()
result = longest_word(input_str)
print(f"The longest word is: {result}")

