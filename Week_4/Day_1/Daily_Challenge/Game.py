import random

# <!-- #rock
# What you will create


# Mini-project: Rock, Paper, Scissors
# Rock-paper-scissors is an old game that can be played between two people. You can read about it in wikipedia

# We will create a game for the user to play Rock-paper-scissors against the computer.

# The user will input his/her move (rock/paper/scissors),
# and the computer will select either rock, paper or scissors at random.
# We will then compare the user’s move with the computer’s move, and determine the results of the game:

# The user won

# The computer won (the user lost)
# A draw (tie)
# We will print the outcome of each game: the user’s choice, the computer’s choice, and the result.

# The user will be able to play again and again. Once the user decides to exit the program, we will print a summary of the outcomes of all the games: how many times they won, lost or and tied the computer.


# Instructions
# Create a new directory for the game. Inside it, create 2 files:
# rock-paper-scissors.py – this will contain functions to show the main menu, handle user’s input, and show the game summary before exiting.
# game.py – this will contain a Game class which will have functions to play a single game of rock-paper-scissors against the computer, determine the game’s result, and return the result.


# Steps
# Part I - game.py
# game.py – this file/module should contain a class called Game. It should have 4 methods:
# get_user_item(self) – Ask the user to select an item (rock/paper/scissors). Keep asking until the user has selected one of the items – use data validation and looping. Return the item at the end of the function.

class Game:
    """One round of rock-paper-scissors against the computer."""

    def __init__(self):
        self.items = ["r", "p", "s"]
 
        # For each item, this is the item it beats
        self.beats = {
            "r": "s",
            "p": "r",
            "s": "p",
        }

        self.user_item = None
        self.computer_item = None
        self.result = None

    def get_user_item(self):
        while True:
            user_input = input("Select (r)ock, (p)aper, or (s)cissors: ").strip().lower()
            if user_input not in self.items:
                print("Invalid input. Please select 'r', 'p', or 's'.")
            else:
                self.user_item = user_input
                return self.user_item

    def get_computer_item(self):
        self.computer_item = random.choice(self.items)
        return self.computer_item

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            self.result = "draw"
        elif self.beats[user_item] == computer_item:
            self.result = "win"
        else:
            self.result = "loss"
        return self.result

    def play(self):
        self.user_item = self.get_user_item()
        self.computer_item = self.get_computer_item()
        self.result = self.get_game_result(self.user_item, self.computer_item)
        print(f"You chose: {self.user_item}. "
              f"The computer chose: {self.computer_item}. "
              f"Result: {self.result}")
 
        return self.result

# get_computer_item(self) – Select rock/paper/scissors at random for the computer. Return the item at the end of the function. Use python’s random.choice() function (read about it online).

# get_game_result(self, user_item, computer_item) – Determine the result of the game.
# Parameters:
# user_item – the user’s chosen item (rock/paper/scissors)
# computer_item – the computer’s chosen (random) item (rock/paper/scissors)
# Return either win, draw, or loss. Where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.

# play(self) – the function that will be called from outside the class (ie. from rock-paper-scissors.py). It will do 3 things:
# Get the user’s item (rock/paper/scissors) and remember it

# Get a random item for the computer (rock/paper/scissors) and remember it

# Determine the results of the game by comparing the user’s item and the computer’s item
# Print the output of the game; something like this: “You selected rock. The computer selected paper. You lose”, “You selected scissors. The computer selected scissors. You drew!”

# Return the results of the game as a string: win;draw;loss;, where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost. -->

