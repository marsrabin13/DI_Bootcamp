while True:
    try:
        user_input = int(input("Input a number: " ))
        if user_input % 2 == 0:
            print("Your input is an EVEN number.")
        else:
            print("Your input is an ODD number.")
        break
    except ValueError:
        print("Not a number, try again.")
