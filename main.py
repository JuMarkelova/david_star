import turtle


def david():
    for step in range(6):
        for i in range(3):
            turtle.forward(30)
            turtle.left(360 / 3)      
        turtle.forward(30)
        turtle.right(60)


turtle.shape('turtle')
turtle.shapesize(2)
turtle.color('blue')
turtle.pensize(10)
turtle.speed(5)


david()


turtle.hideturtle()