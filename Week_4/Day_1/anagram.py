# Now create another Python file, called anagrams.py. This will contain all the UI (user interface) functionality of your program, and will rely on AnagramChecker for the anagram-related logic.

# It should do the following:
# Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.

# If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then be validated:
# Only a single word is allowed. If the user typed more than one word, show an error message. (Hint: how do we know how many words were typed?)
# Only alphabetic characters are allowed. No numbers or special characters.
# Whitespace should be removed from the start and end of the user’s input.

# Once your code has decided that the user’s input is valid, it should find out the following:
# All possible anagrams to the user’s word.
# Create an AnagramChecker instance and apply it to the steps created above.
# Display the information about the word in a user-friendly, nicely-formatted message such as:

from anagram_checker import AnagramChecker

checker = AnagramChecker()

while True:
    print("\n===== ANAGRAM CHECKER =====")
    print("1. Enter a word")
    print("2. Exit")
    choice = input("Choose an option: ").strip()

    if choice == "2":
        print("Goodbye!")
        break

    if choice != "1":
        print("Invalid choice, please type 1 or 2.")
        continue

    word = input("Enter a word: ").strip()

    if len(word.split()) > 1:
        print("Error: please enter only ONE word.")
    elif not word.isalpha():
        print("Error: letters only, no numbers or special characters.")
    elif not checker.is_valid_word(word):
        print(f'"{word}" is not a valid English word.')
    else:
        anagrams = checker.get_anagrams(word)
        print(f'\nYOUR WORD: "{word.upper()}"')
        print("This is a valid English word.")
        if anagrams:
            print("Anagrams for your word:", ", ".join(anagrams))
        else:
            print("This word has no anagrams.")
# YOUR WORD :”MEAT”
# this is a valid English word.
# Anagrams for your word: mate, tame, team.


