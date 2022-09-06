from Suit import Suit
from Card import Card
from Deck import Deck
from Player import Player
from War_card_game import WarCardGame

player = Player("Tom", Deck(is_empty=True))
computer = Player("Computer", Deck(is_empty=True),is_computer=True)
deck = Deck()

game = WarCardGame(player, computer, deck)

game.print_welcome_message()

while not game.check_game_over():
    game.start_battle()
    game.print_stats()

    answer = input("\nAre you ready for the next round\nPress Enter to continue. Enter X to stop.")

    if answer.lower() == "x":
        break
        