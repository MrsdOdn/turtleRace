import random
from turtle import Turtle, Screen

screen = Screen()
#pencerenin boyutunu ayarlamaya yarar
screen.setup(width=500, height=400)
#kullanıcıdan girdi almamızı sağlar
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
count = 0
y_coordinate = -100
for color in colors:
    turtles.append(Turtle(shape="turtle"))
    turtles[count].penup()
    turtles[count].color(color)
    turtles[count].goto(x=-230, y=y_coordinate)
    y_coordinate += 40
    count += 1

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()


# def move_forwards():
#     tim.forward(10)
# def clear_screen():
#     tim.reset()
#
# def move_backwards():
#     tim.backward(10)
#
# def turn_left():
#     tim.left(10)
#
# def turn_right():
#     tim.right(10)
#
#
# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(key="c", fun=clear_screen)


