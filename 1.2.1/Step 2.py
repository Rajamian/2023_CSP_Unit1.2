import turtle as trtl
spot = trtl.Turtle()


# a121_catch_a_turtle.py
#-----import statements-----
import random as rand



#-----game configuration----
spot.shape("circle")
spot.shapesize(5)
spot.fillcolor("Red")


#-----initialize turtle-----


#-----game functions--------
spot_clicked = (5,10)
def spot_clicked(x, y):
    print("Spot was clicked!")


#-----events----------------
spot.onclick(spot_clicked)


wn = trtl.Screen()
wn.mainloop()