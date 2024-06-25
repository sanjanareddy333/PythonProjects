from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape("turtle")
turtle.color("Blue")
# turtle.forward(200)
# turtle.right(90)
# turtle.forward(200)
# turtle.right(90)
# turtle.forward(200)
# turtle.right(90)
# turtle.forward(200)

#
# for _ in range(15):
#     turtle.forward(10)
#     turtle.color("white")
#     turtle.forward(10)
#     turtle.color("black")
#
# for i in range (4):
#     turtle.forward(200)
#     turtle.right(360/4)
# for i in range(5):
#     turtle.forward(200)
#     turtle.right(360/5)

turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)

draw_spirograph(5)









my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()



# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("name", ["sanju", "sathwi"])
# table.add_column("dbo", ["12/03/1999", "14/09/2000"])
# table.align = "r"
#
# print(table)
