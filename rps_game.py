import random

choices = ["rock", "paper", "scissors"]
games_played = int(input("Decide how many rounds you want to play. Choose odd number: "))
player = 0
computer = 0

for game in range(games_played):
    computer_choice = random.choice(choices)
    print(f"Choose one of {choices}")
    player_choice = input()
    if player_choice == computer_choice:
        print("It's tie! Try again!")
    elif (player_choice == "rock") and (computer_choice == "scissors"):
        print("You win!")
        player += 1
    elif (player_choice == "paper") and (computer_choice == "rock"):
        print("You win!")
        player += 1
    elif (player_choice == "scissors") and (computer_choice == "paper"):
        print("You win!")
        player += 1
    else:
        print("You lose!")
        computer += 1

if player > computer:
    print(f"You won the game! You managed to win {player} rounds out of {games_played}")
elif player < computer:
    print(f"You lost the game! Computer managed to win {computer} rounds out of {games_played}")
else:
    print("You tied with computer!")