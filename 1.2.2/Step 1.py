
# a121_catch_a_turtle.py
#-----import statements-----
import random as rand
import turtle as trtl
import turtle as score_writer


#-----game configuration----
score = 0






#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape("circle")
spot.shapesize(5)
spot.fillcolor("Red")

#-----game functions--------
def spot_clicked(x, y):
    change_position()
    update_score()

def change_position():
    global spot
    new_xpos = rand.randint(0, 400)
    new_ypos = rand.randint(0, 400)
    print(new_xpos)
    print(new_ypos)
    spot.penup()
    spot.goto(new_xpos, new_ypos)

def update_score():
    global score
    score =+ 1
    print("score")



#-----events----------------
spot.onclick(spot_clicked)

wn = trtl.Screen()
wn.mainloop()