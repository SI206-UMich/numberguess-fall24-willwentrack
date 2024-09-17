# Your name: William Wentrack
# Your student id: 19194918
# Your email: wwentrac@umich.edu
# List who or what you worked with on this homework:
# If you used generative AI, say that you used it and also how you used it: Yes, I used it for the star function to find bugs.

# import the turtle functions for use in this program
# don't need to use the module name

from turtle import *

### write all new functions here ###



def draw_circle(turtle, color, x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

def draw_rectangle(turtle, color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(2):   # make the sides of the rectangle
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_triangle(turtle, color, x, y, length):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(3):    # make the sides of the traingle
        turtle.forward(length)
        turtle.left(120)
    turtle.end_fill()

def draw_star(turtle, color, x, y, length):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(5):   # create the general star shape (is hollow)
        turtle.forward(length)
        turtle.right(144)
    turtle.end_fill()

    turtle.penup()     # Drawing the pentagon inside the star
    turtle.goto(x + 19, y)   # allings the pentagon
    turtle.pendown()
    turtle.fillcolor(color)  
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(12)  # the correct side length
        turtle.right(72)
    turtle.end_fill()


def draw_square(turtle, color, x, y, length):   # for presents
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range (4):  # draw sides of square
        turtle.forward(length)
        turtle.left(90)
    turtle.end_fill()

def draw_bow(turtle, color, x, y, size):   # for the presents' bow (draws a half circle)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.setheading(90) 
    turtle.circle(size, 180) # 180 makes it a half-circle
    turtle.end_fill()

def draw_w(turtle, x, y, pen_size):   # both initials are 'W'
    turtle.pensize(pen_size)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.right(60)          
    turtle.forward(50)      
    turtle.left(120)
    turtle.forward(50)       
    turtle.right(120)
    turtle.forward(50)        
    turtle.left(120)
    turtle.forward(50)


def draw_my_scene(turtle):
    # trunk
    draw_rectangle(turtle, 'brown', 60, -200, 50, 50)
    
    # bottom tree
    draw_triangle(turtle, 'green', -20, -150, 200)

    # Middle tree
    draw_triangle(turtle, 'green', -20, -75, 200)
    
    # top tree
    draw_triangle(turtle, 'green', -20, 0, 200)
    
    # ornament 1
    draw_circle(turtle, 'red', 175, -25, 15)
    
    # ornament 2
    draw_circle(turtle, 'purple', -20, -100, 15)
    
    # star on top of tree
    draw_star(turtle, 'yellow', 55, 180, 50)
    
    # present
    draw_square(turtle, 'orange', -180, -175, 100)
    
    # ow for present
    draw_bow(turtle, 'blue', -110, -75, 20)
    draw_bow(turtle, 'blue', -140, -75, 10)
    draw_bow(turtle, 'blue', -100, -75, 10)

    # DRAW INITIALS (W.W.)
    # First W
    draw_w(turtle, -250, 150, 5)
    # Second W
    draw_w(turtle, -130, 150, 5)


def main():
  
    screen = Screen()
    screen.bgcolor("sky blue")
    t = Turtle()

    # Call draw_my_scene
    draw_my_scene(t)
    # Lift the turtle at the end
    t.hideturtle()
    
    
    screen.exitonclick()


if __name__ == "__main__":
    main()