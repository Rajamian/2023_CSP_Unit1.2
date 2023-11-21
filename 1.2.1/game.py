
# a121_catch_a_turtle.py
#-----import statements-----
import random as rand
import turtle as trtl


#-----game configuration----
score = 0

font_setup = ("Arial",50,"normal")

timer = 5
counter_interval = 1000
timer_up = False




#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape("circle")
spot.shapesize(5)
spot.fillcolor("Red")

score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(350,-350)
score_writer.pendown()
score_writer.hideturtle()
counter =  trtl.Turtle()
counter.penup()
counter.goto(-350,-350)
counter.pendown()
counter.hideturtle()
#-----game functions--------
def spot_clicked(x, y):
    global timer_up
    if timer_up == False:

        change_position()
    else:
        counter.hideturtle()



def change_position():
    global spot
    new_xpos = rand.randint(0, 400)
    new_ypos = rand.randint(0, 400)
    print(new_xpos)
    print(new_ypos)
    spot.penup()
    spot.goto(new_xpos, new_ypos)
    update_score()

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score,font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)


#-----events----------------
spot.onclick(spot_clicked)

wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()