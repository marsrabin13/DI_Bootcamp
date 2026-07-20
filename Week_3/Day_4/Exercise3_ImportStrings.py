import string

print("Lowercase:", string.ascii_lowercase) # ascii
print("Uppercase:", string.ascii_uppercase) # ascii
print("All letters:", string.ascii_letters) # ascii
print("Digits:", string.digits)
print()

import random

pool = string.ascii_letters
random_string = ""
for _ in range(5):
  random_string += random.choice(pool)

print(f"Random string: {random_string}")