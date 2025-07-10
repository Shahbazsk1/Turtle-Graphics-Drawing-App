from turtle import Turtle, Screen

tim =Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading_1 = tim.heading() - 10
    tim.setheading(new_heading_1)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
# move forward
screen.onkey(move_forwards, "w")
# move backward
screen.onkey(move_backwards, "s")
# turn left
screen.onkey(turn_left, "a")
# turn right
screen.onkey(turn_right, "d")
# clear the screen and back to the home
screen.onkey(clear, "c")
screen.exitonclick()
