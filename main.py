#Portfolio Project: Turtle
#by Leah McNamee
#03/21/25

#Step 1: Draw a line
#Step 2: Draw a square
    #1. Draw a square on the screen.
    #2. Change its color.
    #3. Make the line thicker by changing the pensize or width.
    #4. Change the speed the turtle draws.
#Step 3: Draw two squares
#Step 4: create a square function
#Step 5: create a rectangle function
import turtle
#turtle.shape("turtle") #optional
turtle.speed(3) #optional

turtle.pensize(5)


def square(size):
    for i in range(4):
        turtle.color("blue")
        turtle.forward(size)
        turtle.left(90)
square(90)
square(100)

turtle.penup()
turtle.forward(20)

def triangle(size):
    for j in range(3):
        turtle.color("brown")
        turtle.pendown()
        turtle.forward(size)
        turtle.left(120)
triangle(90)

turtle.penup()
turtle.forward(20)
#turtle.color("pink")
triangle(90)


turtle.penup()
turtle.setpos(25,50)
turtle.pendown()
turtle.color("yellow")
turtle.circle(10)

turtle.Screen().exitonclick()
