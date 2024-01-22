from card import deckOfCards


class compareCards:

    def __init__(self):

        self.numberOfPlayers = 2                  #sets base amount of player to 2

        self.hands = [[] for _ in range(self.numberOfPlayers)]  # Makes two empty lists, the players 'hands'
                # keeps track of the current round winner
        self.roundNumber = 0                # keeps track of the round, starting at 0.
        self.deck = None   #Imports the deck
        self.roundsWinner = None     # keeps track of the current round winner
        self.roundsWon = [0] * self.numberOfPlayers     #list to keep track of how many rounds each player has won

    def startGame(self, numberOfCards):
        """
        This is the first function that will be called. It starts the game by making, shuffling, and dealing the deck.
        :param numberOfCards: this parameter represent the number of cards that each player will receive.
        :return:N/A
        """
        self.deck = deckOfCards()                                      # creates a new deck.
        self.deck.shuffleDeck()                                    # shuffles the deck.

        print("Dealer deals", numberOfCards, "cards to each player...")
        cards = self.deck.dealCards(numberOfCards * self.numberOfPlayers)
        #Total number of cards needed (for each player)
        for i in range(self.numberOfPlayers):
            self.hands[i] = cards[i::self.numberOfPlayers]      # Just ran a line thru chat GPT until it spit out something that worked,equally deals cards
                                                                    # Had to ChatGPT this one too simulate a fair deal and make sure everyone gets the same amount of different cards .
        self.showHands()                                    # Prints the hand of each player

    def showHands(self):
        """
        Shows player's hands
        :return: N/A
        """
        for i, hand in enumerate(self.hands, start=1):                                   # Next two lines come from ChatGpt. The enumerate function is used to go over each player's hand (self.hands). It returns pairs of the form (index, hand), where index is the position of the hand in self.hands. The start=1 makes it so that indexing should start from 1 instead of the default 0.
            print(f"Player {i} Hand:", ", ".join(f"{value} {suit}" for value, suit in hand))    # connects values and suits of each card in the hand into a string.

    def playBall(self):
        """
        Plays through a round, adding a tally to the round total, Printing each user's card, finding the winner, and printing the winner.
        :return: N/A
        """
        self.roundNumber += 1                                                              # Adds a tally to the amount of rounds
        print("Round", self.roundNumber, ":")                                              # Prints which round it is

        for i in range(self.numberOfPlayers):
            print("Player", i + 1, ":", self.hands[i][self.roundNumber - 1][0],     # Finds value of the card that the player has in their hand for the current round.
                  self.hands[i][self.roundNumber - 1][1])                           # Finds the suit of the card that the player has in their hand for the current round.

        self.findWinner()
        self.roundsWon[self.roundsWinner] += 1                                      # Gives a point to winner of round
        print("Player", self.roundsWinner + 1, "wins this round!")

    def findWinner(self):
        """
        compares the cards to find the winner of the round.
        :return: N/A
        """
        roundValues = [hand[self.roundNumber - 1][0] for hand in self.hands]
        maxValue = max(roundValues)
        self.roundsWinner = roundValues.index(maxValue)
    def getWinner(self):
        """
        Gets the overall winner
        :return: winner and how many rounds they won.
        """
        maxRounds = max(self.roundsWon)                       # Finds the max rounds won by a single player

        if self.roundsWon.count(maxRounds) == 1:              # Sees if there is a person with the most wins
            winner = self.roundsWon.index(maxRounds) + 1      # If there is only one, that player is the winner.
            return [winner], maxRounds                         # winner and how many rounds they won
        else:
            return [], maxRounds                               # If multiple winners, a value is returned with how many rounds were won.



