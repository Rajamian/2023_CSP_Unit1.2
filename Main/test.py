import random

import turtle as trtl


options = ("rock", "paper" ,"scissors")
player = None
computer = random.choice(options)
playing = True

while playing:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors):")


    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("Draw")
    elif player == "rock" and computer == "scissors":
        print("Player Wins!")
    elif player == "paper" and computer == "rock":
        print("Player Wins!")
    elif player == "scissors" and computer == "paper":
        print("Player Wins!")
    else:
        print("You lose!")

        if not input("Play Again? (y/n): ").lower() == "y":
            playing = False

    print("Thanks for playing!")

line = trtl.Turtle()






wn = trtl.Screen()
wn.mainloop()

