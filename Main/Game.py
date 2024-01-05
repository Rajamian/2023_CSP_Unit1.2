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

#make x

x_image = "x.gif"





wn = trtl.Screen()
wn.mainloop()