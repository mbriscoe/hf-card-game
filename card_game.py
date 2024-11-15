# import packages
import os
import random
from colorama import Fore, Back, Style

os.system("clear")

# set up the game
suits = ("Hearts", "Clubs", "Diamonds", "Spades")
numbers = (range(2, 15))

# define variables
player1_card = []
player2_card = []

player1_pack = []
player2_pack = []


def create_deck():
    deck = []
    for suit in suits:
        for number in numbers:
            card = (number, suit)
            deck.append(card)
    random.shuffle(deck)

    return deck

# process card number


def process_card(card_number):
    if card_number == 11:
        return "Jack"
    if card_number == 12:
        return "Queen"
    if card_number == 13:
        return "King"
    if card_number == 14:
        return "Ace"
    else:
        return card_number


# create deck
deck_of_cards = create_deck()

# game loop
while len(deck_of_cards) > 1:
    input("press enter to deal cards")

    # deal cards and remov ethem from pack
    player1_card = random.choice(deck_of_cards)
    deck_of_cards.remove(player1_card)

    player2_card = random.choice(deck_of_cards)
    deck_of_cards.remove(player2_card)

    os.system("clear")

    # display cards
    if player1_card[0] > player2_card[0]:
        print(f"{Fore.GREEN}Player 1 card: {process_card(
            player1_card[0])} of {player1_card[1]}")
        print(f"{Fore.RED}Player 2 card: {process_card(
            player2_card[0])} of {player2_card[1]}")
        print(Style.RESET_ALL)
    elif player1_card[0] < player2_card[0]:
        print(f"{Fore.RED}Player 1 card: {process_card(
            player1_card[0])} of {player1_card[1]}")
        print(f"{Fore.GREEN}Player 2 card: {process_card(
            player2_card[0])} of {player2_card[1]}")
        print(Style.RESET_ALL)
    else:
        print(f"{Fore.RED}Player 1 card: {process_card(
            player1_card[0])} of {player1_card[1]}")
        print(f"{Fore.GREEN}Player 2 card: {process_card(
            player2_card[0])} of {player2_card[1]}")
        print(Style.RESET_ALL)

    # compare cards
    if player1_card[0] > player2_card[0]:
        print(f"{Fore.YELLOW}Player 1 wins this hand!{Style.RESET_ALL}")
        player1_pack.append(player1_card)
        player1_pack.append(player2_card)
    elif player1_card[0] < player2_card[0]:
        print(f"{Fore.YELLOW}Player 2 wins this hand!{Style.RESET_ALL}")
        player2_pack.append(player1_card)
        player2_pack.append(player2_card)
    else:
        print(f"{Fore.YELLOW}It's a draw!{Style.RESET_ALL}")
        player1_pack.append(player1_card)
        player2_pack.append(player2_card)

    # display number of cards left in deck
    print(f"\n{Fore.BLUE} Number of cards left: {
        len(deck_of_cards)}{Style.RESET_ALL}")


# determine the winner
if len(player1_pack) > len(player2_pack):
    # player 1 wins
    print(
        f"{Fore.YELLOW}Player 1 Wins the game with {len(player1_pack)} cards over {
            len(player2_pack)} cards!"
    )
elif len(player1_pack) < len(player2_pack):
    # player2 wins
    print(
        f"{Fore.YELLOW}Player 2 Wins the game with {len(player2_pack)} cards over {
            len(player1_pack)} cards!"
    )
else:
    # it's a draw
    print(f"{Fore.YELLOW}It's a draw!!")

print(Style.RESET_ALL)


if input("would you like to see the cards in the player packs (y/n)?").upper() == "Y":
    # display the cards in the player packs
    for card in player1_pack:
        print(
            f"{Fore.MAGENTA}Player 1 Pack: {process_card(card[0])} of {card[1]}{
                Style.RESET_ALL}"
        )

    for card in player2_pack:
        print(
            f"{Fore.CYAN}Player 2 Pack: {process_card(card[0])} of {card[1]}{
                Style.RESET_ALL}"
        )

    print(f"\nThanks for playing!\n")
else:

    print(f"\nThanks for playing!\n")
