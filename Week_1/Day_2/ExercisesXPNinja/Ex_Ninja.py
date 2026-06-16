print(bool(bool(None)))

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x) # True
print("y is", y) #False
print("a:", a) #5
print("b:", b) #10

my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco 
           laboris nisi ut aliquip ex ea commodo consequat. 
           Duis aute irure dolor in reprehenderit in voluptate velit 
           esse cillum dolore eu fugiat nulla pariatur. 
           Excepteur sint occaecat cupidatat non proident, 
           sunt in culpa qui officia deserunt mollit anim id est laborum."""


print(len(my_text))

user_input = input("Input the longest sentence you can without the character “A”:")
if "A" in user_input:
    print("Sorry, you entered a sentence with character “A”")
else:
    print("Great!you entered a sentence without character “A”.")
    user_input2 = input("Input a longer sentence without the character “A”:")
    if "A" in user_input2:
        print("Sorry, you entered a sentence with character “A”")
    else:
        if len(user_input2) > len(user_input):
            print("Congratulations! You entered a longer sentence.")
        else:
            print("Sorry that's a shorter sentence.") 

