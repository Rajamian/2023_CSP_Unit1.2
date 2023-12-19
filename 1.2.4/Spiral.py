import turtle as trtl
'''
x = starting distance
y = incremental distance

In a loop:
    1. go forward x
    2. turn left 90 degrees
    3. go forward x + Y
    4. turn left 90 degrees

Doors
1. Go forward 10 and place a door 
maze_painter.forward(10)
maze_painter.penup()
maze_painter.forward(path_width*2)
maze_painter.pendown()




'''

maze_painter = trtl.Turtle()
x = 10
y = 20
maze_painter.hideturtle()

for walls in range(28):
    maze_painter.left(90)
    maze_painter.forward(x + y)
    y += 10
maze_painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()
