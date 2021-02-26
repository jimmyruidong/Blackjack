import random

#Reason for classes:
#Modelling. Divide complex software into pieces that are easier to understand.
#Blackjack - divided into Deck, Card, Hand, etc.
#Pieces solving a puzzle.

class Deck():
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, size=(len(suits)*len(ranks))): #Instead of hardcoding size = 52.
        print("Generating Deck...")
        #        self.name = name
        self.size = size
        self.cards = []

        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(rank, suit))
        print("Deck Created!")
    def __str__(self):
        return "This is a deck of cards"

    def __len__(self):
        return self.size

    def shuffle(self):
        print("Shuffling Cards...")
        random.shuffle(self.cards)
        print("Deck has been shuffled!")

    def issue(self):
        return self.cards.pop()


class Card():

    def __init__(self, rank, suit):
        print("A card has been created")
        self.rank = rank

        self.suit = suit

        self.name = f"{rank} of {suit}"

    def __str__(self):
        return f"This a {self.name} with a value of {self.cardValue()}"

    def cardValue(self):
        if self.rank == 'Jack' or 'Queen' or 'King':
            return 10

        elif self.rank == 'Ace':
            return '11'

        else:
            return self.rank

    def __del__(self):
        print(f"{self.name} has been destroyed")


class Hand():

    def __init__(self, name):
        self.name = name
        self.cards = []
        self.sum = 0
        print(self)

    def __str__(self):
        return f"This is {self.name}'s hand"

    def accept(self, card):
        self.cards.append(card)

    def tally_sum(self):
        for card in self.cards:
            sum += card.cardValue

        return sum

       # self.sum = self.cards[]#STOPPINGHERFORNOW

    def cards(self):
        return self.cards()

def initial_hand(size,hand,hand2,deck):
    for i in range(size):
        hand.issue((deck.issue()))
        hand2.issue(deck.issue())
# def is_bust(cards):
#     sum = 0
#     if sum ==
#
#     for card in cards:
#
#     #cardsislist
def blackjack_game():
    print("Welcome to Blackjack\n")

    start_size = 2
    GameDeck = Deck()
    GameDeck.shuffle()

    PlayerHand = Hand(input("Please enter your name"))
    DealerHand = Hand('Dealer')

    initial_hand(start_size, PlayerHand, DealerHand, GameDeck)

    PlayerHand.accept(GameDeck.issue()) #Meant to be a hit function. Changed from deal (deal) to accept(issue)
    #Reading things in English makes it easier to reason/read the code


def main():
    blackjack_game()



if __name__ == '__main__':
    main()
