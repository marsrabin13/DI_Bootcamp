# Here is a python code that generates a list of 20000 random numbers, called list_of_numbers, and a target number.

import random
list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
#list_of_numbers = [0,3728,1,2]
target_number   = 3728
#print(list_of_numbers)
unique_pair_set = set()

def print_line(num1,num2):
    print(f"{num1} and {num2} sums to the target number {target_number}")

# for num1 in range(len(list_of_numbers)):
#     for num2 in range(num1 + 1, len(list_of_numbers)):
#         if list_of_numbers[num1] + list_of_numbers[num2] == target_number:
#             pair = tuple(sorted((list_of_numbers[num1], list_of_numbers[num2])))
#             unique_pair_set.add(pair)

seen = set()
for num in list_of_numbers:
    complement = target_number - num
    if complement in seen:
        pair = tuple(sorted((num, complement)))
        unique_pair_set.add(pair)
    seen.add(num)

for num1, num2 in unique_pair_set:
    print_line(num1, num2)

print(f"Total unique pairs {len(unique_pair_set)} ")

# Copy this code, and create a program that finds, within list_of_numbers all the pairs of number that sum to the target number
# For example

# for num in list_of_numbers:
#     for n in range(len(list_of_numbers):
#         if num + list_of_numbers[n] 



# 1000 and 2728 sums to the target_number 3728
# 1864 and 1864 sums to the target_number 3728




# One Last Thing: Good luck!