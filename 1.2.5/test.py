import random
import turtle as trtl

#Introduce the computer to the different options in rock,paper,scissors
Choices = ("rock", "paper", "scissors")
player = None
Bot = random.choice(Choices)
playing = True

#Generate a random choice from both player and computer
while playing:
    player = None
    Bot = random.choice(Choices)
    while player not in Choices:
        player = input("Rock, Paper, Scissor, Shoot! (rock, paper, scissors):")
    print(f"player: {player}")
    print(f"computer: {Bot}")

#This section of code is how the computer knows how the game functions and determines who wins or loses
    if player == Bot:
        print("Draw")
    elif player == "rock" and Bot == "scissors":
        print("Player Wins!")
    elif player == "paper" and Bot == "rock":
        print("Player Wins!")
    elif player == "scissors" and Bot == "paper":
        print("Player Wins!")
    else:
        print("You lose!")

        if not input("Play Again? (y/n): ").lower() == "y":
            playing = False

    print("Thanks for playing!")
