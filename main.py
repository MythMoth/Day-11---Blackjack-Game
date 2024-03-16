from art import logo
import random


def draw_card(player):
    player.append(cards.pop(random.randint(0, len(cards)-1)))


on = True

while on:
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6,
             7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    computer_cards = []
    game_over = False

    draw_card(user_cards)
    draw_card(user_cards)
    draw_card(computer_cards)
    draw_card(computer_cards)

    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")
    choice = input("Type 'y' to get another card or 'n' to pass: ")

    while choice == "y":
        draw_card(user_cards)
        if sum(user_cards) > 21:
            if 11 in user_cards:
                user_cards[user_cards.index(11)] = 1
                print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
                print(f"Computer's first card: {computer_cards[0]}")
                choice = input("Type 'y' to get another card or 'n' to pass: ")
            else:
                print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
                print(f"Computer's first card: {computer_cards[0]}")
                print("You went over. You lose")
                choice = "n"
                game_over = True
        else:
            print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
            print(f"Computer's first card: {computer_cards[0]}")
            choice = input("Type 'y' to get another card or 'n' to pass: ")

    if not game_over:
        print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
        while sum(computer_cards) < sum(user_cards) and sum(computer_cards) < 18:
            draw_card(computer_cards)
            if sum(computer_cards) > 21 and 11 in computer_cards:
                computer_cards[computer_cards.index(11)] = 1
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
        if sum(computer_cards) > 21:
            print("Computer went over. You win!")
        elif sum(computer_cards) > sum(user_cards):
            print("Computer has a higher score than you. You lose")
        elif sum(computer_cards) == sum(user_cards):
            print("It's a tie!")
        else:
            print("You have a higher score than computer. You win!")

    play = input("Do you want to play a game of Blackjack? y/n:")
    if play == "n":
        on = False
