import os
import platform
import random


suits = ['h', 'd', 's', 'c']
deck = {
    'h': ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'],
    'd': ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'],
    's': ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'],
    'c': ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
}
card_value = {
    'A': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}


def deal_card() -> str:
    card = ''
    while not card:
        suit = random.randint(0, 3)
        rank = random.randint(0, 12)
        card = deck[suits[suit]][rank]
        if card:
            deck[suits[suit]][rank] = ''

    return f"{card}{suits[suit]}"


def get_card_value(card: str) -> int:
    return card_value[card[:-1]]


def get_card_rank(card: str) -> str:
    return card[:-1]


def get_hand_value(hand: list[str]) -> int:
    total = 0
    ace_count = 0
    for card in hand:
        if get_card_rank(card) == 'A':
            ace_count += 1
        total += get_card_value(card)

    # Handle Ace as 1/11
    for _ in range(0, ace_count):
        if total > 21:
            total -= 10

    return total


def blackjack():
    os.system("cls" if platform.system() == 'Windows' else "clear")

    hand = []
    dealer_hand = []

    # First card
    hand.append(deal_card())
    dealer_hand.append(deal_card())
    # Second card
    hand.append(deal_card())
    dealer_hand.append(deal_card())

    stand = False
    while not stand:
        hand_value = get_hand_value(hand)
        print(f"\tYour cards: {hand}, current score: {hand_value}")
        print(f"\tDealer's first card: {dealer_hand[0]}, score showing: {get_card_value(dealer_hand[0])}")

        if hand_value > 21:
            break

        stand = input("Type (y)es to get another card or (n)o to stand : ").lower().startswith("n")

        if not stand:
            hand.append(deal_card())

    hand_value = get_hand_value(hand)
    print(f"\tYour final hand: {hand}, final score: {hand_value}")

    # Dealer must keep drawing if total less than 17
    while get_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card())

    dealer_hand_value = get_hand_value(dealer_hand)
    print(f"\tDealer's final hand: {dealer_hand}, final score: {dealer_hand_value}")

    if hand_value > 21:
        if dealer_hand_value > 21:
            print("You both bust... it's a DRAW")
        else:
            print("Busted... you LOSE sucker")
    else:
        if dealer_hand_value > 21:
            print("WINNER, WINNER... chicken dinner")
        elif hand_value > dealer_hand_value:
            print("WINNER, WINNER... chicken dinner")
        elif hand_value == dealer_hand_value:
            print("What are the chances... it's a DRAW")
        else:
            print("You LOST fair and square")


if input("Do you want to play Blackjack ? (y)es or (n)o : ").lower().startswith("n"):
    exit(0)

blackjack()