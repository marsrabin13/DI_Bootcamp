#Part 2:  Create a deck of cards class.


import random
 
 
class Card:
 
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
 
    def __repr__(self):
        # __repr__ decides what Python shows when you print the object.
        return f"{self.value} of {self.suit}"
 
 
class Deck:
 
    suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
 
    def __init__(self):
        self.cards = self._build_deck()
 
    def _build_deck(self):
        return [Card(suit, value) for suit in self.suits for value in self.values]
 
    def __repr__(self):
        return f"Deck of {self.count()} cards"
 
    def count(self):
        return len(self.cards)
 
    def shuffle(self):
        if self.count() != 52:
            raise ValueError("Only a full deck of 52 cards can be shuffled.")
        random.shuffle(self.cards)
        return self  # returning self lets you write deck.shuffle().deal()
 
    def deal(self):
        if not self.cards:
            raise ValueError("All cards have been dealt.")
        return self.cards.pop()
 
    def deal_hand(self, number):
        return [self.deal() for _ in range(number)]
 
    def reset(self):
        self.cards = self._build_deck()
        return self
 
 
# This block only runs when you execute the file directly,
# not when you import it from another file.
if __name__ == "__main__":
    deck = Deck()
    print(deck)                      # Deck of 52 cards
 
    deck.shuffle()
    print("Top card:", deck.deal())  # one random card
    print("Hand:", deck.deal_hand(5))
    print(deck)                      # Deck of 46 cards
 
    deck.reset()
    print("After reset:", deck)



 