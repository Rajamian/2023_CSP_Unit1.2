import random
import turtle as trtl

#Introduce the computer to the different options in rock,paper,scissors
options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)
playing = True

#Generate a random choice from the computer and generate a choice as a player
while playing:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors):")


    print(f"player: {player}")
    print(f"computer: {computer}")

#This section of code is how the computer knows who wins
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

#Create the visual aspect of the project
visual = trtl.Turtle()
#If player loses, draw a red x
if player == "You lose!!":
    visual.penup()
    x_image = "Redx.gif"
    wn = trtl.Screen()
    wn.setup(width=2.0, height=2.0)
    wn.addshape(x_image)
    x = trtl.Turtle()

    def draw_x(active_x):
        active_x.shape(x_image)
        wn.update()
    draw_x(x)
    wn.mainloop()

#if player wins, draw a green checkmark
if player == "Player wins!":
    visual.penup()
    check_image = "Checkmark.gif"
    wn = trtl.Screen()
    wn.setup(width=2, height=2)
    wn.addshape(check_image)
    check = trtl.Turtle()

    def draw_check(active_check):
      active_check.shape(check_image)
      wn.update()

    draw_check(check)
    wn.mainloop()
