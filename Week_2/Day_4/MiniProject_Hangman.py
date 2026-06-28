# Instructions
# The computer choose a random word and mark stars for each letter of each word.
# Then the player will guess a letter.
# If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
# If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
# The player will continue guessing letters until they can either solve the word(s) (or phrase) or all six body parts are on the gallows.
# The player can’t guess the same letter twice.


# Starter code
# Here is a piece of code that will give you a random word.

#     import random

#     wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
#     word = random.choice(wordslist) 

#     ### YOUR CODE STARTS FROM HERE ###

import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 
print("Welcome to hangman!! Guess the word: ")
hidden_word = []

def print_word():
    for letter in word:
        if letter == " ":
            letter = " "
        else:
            letter = "*"
        hidden_word.append(letter)
    #print(word)
    print(" ".join(hidden_word))
    return hidden_word


def input_letter(hidden_word): 
    guessed_letters = []
    count_incorrect_guesses = 0
    while True: 
        letter = input("Guess a letter: ")
        if letter in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        guessed_letters.append(letter)
        if letter in word:
            print("Correct guess!")
            for i in range(len(word)):
                if word[i] == letter:
                    hidden_word[i] = letter
            print(" ".join(hidden_word))
            if "*" not in hidden_word:
                print("Congratulations! You've guessed the word!")
                break
        else:
            count_incorrect_guesses += 1
            print("Incorrect guess. Try again.")
            print_hangman(count_incorrect_guesses)
            if count_incorrect_guesses == 6:
                print("Game over! The word was: " + word)
                break

def print_hangman(incorrect_guesses):
    hangman_stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
           |   |
          /    |
        """,
        """
           -----
           |   |
           O   |
           |   |
          / \  |
               |
        """,
        """
           -----
           |   |
           O   |
          /|   |
          / \  |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        """
    ]
    print(hangman_stages[incorrect_guesses])


def main():
    hidden_word = print_word()
    input_letter(hidden_word)

main()