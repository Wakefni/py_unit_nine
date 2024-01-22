# Nicholas Wakefield
# 1/20/24
# compare game

from testing_card import compareCards


def cardsPerPlayer():
    """
    asks the user how many cards (rounds) there should be
    :return: returns the amount of cards to deal each player.
    """
    while True:                                                                                                     # Creates a loop that doesn't end until a valid input is received.
        try:
            numberOfCards = int(input("How many cards should each player get? Enter a number between 1 and 26: "))
            if 1 <= numberOfCards <= 26:                                                                               # Tests to make sure the user enters a number between 1 and 26, as that is how many rounds can be played (assuming there are 2 players.)
                return numberOfCards
            else:
                print("Please enter a number between 1 and 26.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 26.")


def main():
    print("Welcome to the game of Compare. You will decide how many cards we get, and then we'll play them one by one.")
    print("Whoever has the higher card wins that round. Whoever wins the most rounds wins the game.")

    numberCards = cardsPerPlayer()

    game = startGame()
    game.start_game(numberCards)

    while game.roundNumber < numberCards:
        game.playBall()

    print("Game Over!")

    winners, maxRounds = game.getWinner()

    for i, rounds in enumerate(game.roundsWon, start=1):
        print("Player", i, "wins", rounds, "rounds.")
    value = len(winners)
    if value == 1:
        print("Player", *winners, "wins the game with:", maxRounds, "round(s).")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    main()