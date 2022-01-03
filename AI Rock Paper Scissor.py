
import random

hands = ['rock', 'paper', 'scissors']

pairs = {"rock": "scissors", "paper": "rock", "scissors": "paper", "car": "plane"}

while True:

    comp_hand = random.choice(hands)

    player_hand = input('Rock, Paper or Scissors? ')

    print("AI played " + comp_hand)

    try:
        if pairs[comp_hand] == player_hand:
            print("The AI wins :(")
        elif pairs[player_hand] == comp_hand:
            print("You win")
        else:
            print("Tie. Try again")
    except KeyError:
        print("Invalid input")
