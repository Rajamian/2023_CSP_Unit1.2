import random
import turtle as trtl

#Introduce the computer to the different options in rock,paper,scissors
Choices = ("rock", "paper", "scissors")
player = None
Bot = random.choice(Choices)
playing = True

while playing:
    player = None
    Bot = random.choice(Choices)
    while player not in Choices:
        player = input("Rock, Paper, Scissor, Shoot! (rock, paper, scissors):")
    print(f"player: {player}")
    print(f"computer: {Bot}")
def winner(Bot, Player):
    if(player == "rock" and Bot == "paper"):
        print("You Lose!")
    elif (player == "rock" and Bot == " scissors"):
        print("You Win!")
    elif (player == "rock" and Bot == "rock"):
        print("It's a Tie!")
    elif (player == "paper" and Bot == "rock"):
        print("You Win!")
    elif (player == "paper" and Bot == "scissors"):
        print("You Lose!")
    elif (player == "paper" and Bot == "paper"):
        print("It's a Tie!")
    elif (player == "scissors" and Bot == "rock"):
        print("You Lose!")

        if not input("Play Again? (y/n): ").lower() == "y":
            playing = False

    print("Thanks for playing!")