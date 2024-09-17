from turtle import *

### write all new functions here ###



def draw_emoji(turtle):   # draws the suprised face emoji
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    turtle.circle(150)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(0, 45)
    turtle.pendown()
    turtle.fillcolor("#4B2E1A")
    turtle.begin_fill()
    turtle.circle(35)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-70, 160)
    turtle.pendown()
    turtle.fillcolor("#4B2E1A")
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

    turtle.fillcolor("#4B2E1A") #hex color for dark brown
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(70, 160)
    turtle.pendown()
    turtle.fillcolor("#4B2E1A")
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-110, 215)
    turtle.pendown()
    turtle.width(10)
    turtle.color("#4B2E1A")
    turtle.setheading(0)
    turtle.left(45)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)


    turtle.penup()
    turtle.goto(50, 235)
    turtle.pendown()
    turtle.width(10)
    turtle.setheading(0)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.end_fill()









def main():
    screen = Screen()
    screen.bgcolor("tan")
    t = Turtle()
    
    draw_emoji(t)
    # Lift the turtle at the end
    t.hideturtle()
    screen.exitonclick()


if __name__ == '__main__':
    main()


