import random


def create_deck():
    ranks = [str(num) for num in range(2, 11)] + ["J", "Q", "K", "A"]
    suits = ["hearts", "diamonds", "clubs", "spades"]
    deck = [(rank, suit) for rank in ranks for suit in suits]
    return deck


def shuffle_deck(deck):
    random.shuffle(deck)
    return deck


def deal_cards(deck):
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    return player_hand, dealer_hand, deck


def calculate_hand_value(hand):
    values = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
        "A": 11,
    }
    value = sum([values[card[0]] for card in hand])
    num_aces = len([card for card in hand if card[0] == "A"])
    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1
    return value


def player_turn(player_hand, deck):
    while True:
        print(f"Your hand: {player_hand}")
        print(f"Your hand value: {calculate_hand_value(player_hand)}")
        choice = input("Do you want to hit or stand? ")
        if choice.lower() == "hit":
            player_hand.append(deck.pop())
            if calculate_hand_value(player_hand) > 21:
                print(f"Your hand: {player_hand}")
                print(f"Your hand value: {calculate_hand_value(player_hand)}")
                print("Bust! You lose.")
                return "dealer"
        else:
            return "continue"


def dealer_turn(dealer_hand, deck):
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    print(f"Dealer hand: {dealer_hand}")
    print(f"Dealer hand value: {calculate_hand_value(dealer_hand)}")
    if calculate_hand_value(dealer_hand) > 21:
        print("Dealer bust! You win.")
        return "player"
    else:
        return "continue"


def determine_winner(player_hand, dealer_hand):
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    if player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")


def play_game():
    deck = create_deck()
    deck = shuffle_deck(deck)
    player_hand, dealer_hand, deck = deal_cards(deck)
    print(f"Player hand: {player_hand}")
    print(f"Player hand value: {calculate_hand_value(player_hand)}")
    print(f"Dealer hand: [{dealer_hand[0]}, ?]")
    if calculate_hand_value(player_hand) == 21:
        print("Blackjack! You win!")
    else:
        result = player_turn(player_hand, deck)
        if result == "continue":
            result = dealer_turn(dealer_hand, deck)
            if result == "continue":
                determine_winner(player_hand, dealer_hand)


play_game()
