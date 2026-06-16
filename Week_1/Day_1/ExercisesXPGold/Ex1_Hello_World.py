print("Hello World \n" * 4)
print("I love Python \n" * 4)

while True:
    try:
        user_input = int(input("Input month (1 to 12): " ))
        if user_input in (3,4,5):
            print("Spring runs from March (3) to May (5)")
        elif user_input in (6,7,8):
            print("Summer runs from June (6) to August (8)")
        elif user_input in (9,10,11):
            print("Autumn runs from September (9) to November (11)")
        elif user_input in (12,1,2):
            print("Winter runs from December (12) to February (2)")
        else:
            print("Not a number from 1 to 12. Try again")
            continue
        break
    except ValueError:
        print("Not a number, try again.")
