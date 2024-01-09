import turtle as trtl

line = trtl.Turtle()


#make game board
line.speed(0)

line.penup()
line.goto(-125,-300)
line.pendown()
line.left(90)
line.forward(600)
line.penup()
line.goto(125,-300)
line.pendown()
line.forward(600)
line.penup()
line.goto(-300,125)
line.pendown()
line.right(90)
line.forward(600)
line.penup()
line.goto(300,-125)
line.pendown()
line.right(180)
line.forward(600)
line.hideturtle()

list = (1 , 2,3,4,5,6,7,8,9)


#make x
x_image = "TurtleImage.gif"

wn = trtl.Screen()
wn.setup(width=2.0, height=2.0)
wn.addshape(x_image)

x = trtl.Turtle()


def draw_x(active_x):
  active_x.shape(x_image)
  wn.update()

draw_x(x)
wn.mainloop()


#make an O
o_image = "Opic.gif"

wn = trtl.Screen()
wn.setup(width=.5, height=.5)
wn.addshape(o_image)

o = trtl.Turtle()

def draw_o(active_o):
  active_o.shape(o_image)
  wn.update()

draw_o(o)
wn.mainloop()













wn = trtl.Screen()
wn.mainloop()