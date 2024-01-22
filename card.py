import random
class deckOfCards:
    def __init__(self):
        self.suits = ["♣️", "♦️", "♥️", "♠️"]                               # This makes the suits that can be used.
        self.values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        # This makes the values that can be used.
        self.deck = self.makeDeck()

    def makeDeck(self):
        """
        This function creates the deck
        :return: list of all cards
        """
        return [
            (value, suit)                           # Makes a list with every card
            for value in self.values                # This is a nested loop that iterates over each value
            for suit in self.suits                  # Second part of list that goes over every suit
        ]

    def shuffleDeck(self):              # ChatGPT fisher-yates shuffle method

        n = len(self.deck)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]

    def dealCards(self, numberOfCards):        #Asked ChatGPT for some help :)
        """
        Deals the cards to the players
        :param numberOfCards: amount of cards
        :return: amount of cards delt to the players
        """
        return self.deck[:numberOfCards]        # Takes the 'top' card off of the deck and 'deals' it
