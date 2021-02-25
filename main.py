import random
from art import logo, ACE
import os

def incorrect_answer(text, type):
    if type == str:
        incorrect_answer = True
        while incorrect_answer:
            variable = input(f"{text}: ").lower()
            if variable == 'y' or variable == 'n':
                return variable
            else:
                print("-" * 50, '\nIncorrect answer\n', "-" * 50)
    elif type == int:
        incorrect_answer = True
        while incorrect_answer:
            variable = input(f"{text}: ").lower()
            if variable == '11' or variable == '1':
                return int(variable)
            else:
                print("-" * 50, '\nIncorrect answer\n', "-" * 50)      


def score(list_with_cards):
    result = 0
    for number in list_with_cards:
        result += number
    return result
 
 
def blackjack():
    all_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
 
    user_cards = []
    computer_cards = []

    for _ in range(2):
        computer_cards.append(random.choice(all_cards))
        user_cards.append(random.choice(all_cards))
 
    another_card = True
    user_score = score(user_cards)
 
    while user_score < 21:
        print(logo)
        print(f'    Your cards: {user_cards}, current score: {user_score}')
        print(f'    Computer first card: [{computer_cards[0]}]')
        another_card = incorrect_answer("Type 'y' to get another card, type 'n' to pass", type=str)
 
        if user_score > 21:
            user_score = score(user_cards)
        elif another_card == 'y':
            new_card = random.choice(all_cards)
            if new_card == 11:
                print(f'{ACE}')
                new_card = incorrect_answer('You take Ace and you can choose count "11" or "1"', type=int)
                user_cards.append(new_card)
            else:
                user_cards.append(new_card)
            user_score = score(user_cards)
        elif another_card == 'n' :
            user_score = score(user_cards)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        os.system('cls' if os.name == 'nt' else 'clear')
 
 
    computer_score = score(computer_cards)
 
    while computer_score < 17:
        new_card = random.choice(all_cards)
        if new_card == 11:
            if computer_score + new_card > 21:
                new_card = 1
                computer_cards.append(new_card)
            else:
                new_card = 11
                computer_cards.append(new_card)
        else:
            computer_cards.append(new_card)
        computer_score = score(computer_cards)
    
    print(logo)
    print(f'    Your final hand: {user_cards}, final score: {user_score}')
    print(f'    Computer final hand: {computer_cards}, final score: {computer_score}')
 
    if user_score > 21 and computer_score > 21:
        if user_score > computer_score:
            print(f'    You lose! :(')
        elif user_score == computer_score:
            print(f'    Draw')
        else:
            print(f'    You win! Congratulations :)')
    elif user_score > 21:
        print(f'    You lose! :(')
    elif computer_score > 21:
        print(f'    You win! Congratulations :)')
    elif user_score < computer_score:
        print(f'    You lose! :(')
    elif user_score > computer_score:
        print(f'    You win! Congratulations :)')
    else:
        print(f'    Draw.')

    new_game = incorrect_answer(text="Do you want to play a new game? Type 'y' or 'n'", type=str)
 
    if new_game == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')
        blackjack()
 

os.system('cls' if os.name == 'nt' else 'clear') 
answer = incorrect_answer("Do you want to play a game of Blackjack? Type 'y' or 'n'", type=str)
if answer == 'y':
    os.system('cls' if os.name == 'nt' else 'clear')
    blackjack()

