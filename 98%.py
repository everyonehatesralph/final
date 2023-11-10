import turtle
from random import randint

print("By:\nRalph Joshua Seromines and Hedjara Darapa. \n")

# Input the racer names
print('Please Enter Names')
name1 = input("Name for Racer 1: ")
name2 = input("Name for Racer 2: ")

# Input here who will you bet from Racer 1 or 2.
bet = input(f"Pick one player for your bet? \n      [{name1}] or [{name2}]\nJust type the name of your bet: ")

# I'm using variable for changing section
# here you can change the colors, coordinates, title and the shape easily, so that I can find and edit it easily.
screen_title = 'TURTLE DRAG RACE'
t1_border = 'SkyBlue'
t1_fill = 'Black'
t2_border = 'Pink'
t2_fill = 'Black'
BgColor = 'Black'

width = 650
height = 180
turtle_shape = 'turtle'

# Screen setup
display = turtle.Screen()
display.setup(width, height)
display.bgcolor(BgColor)

# Finish Line Setup
fin_line = turtle.Turtle()
fin_line.speed(0)
fin_line.color('White')
fin_line.shape('square')
fin_line.penup()

distance = 250
y_position = 85

# Create the finish line using stamps
for i in range(5):
    fin_line.goto(distance, y_position - i * 40)
    fin_line.stamp()

for j in range(4):
    fin_line.goto(distance + 20, y_position - 20 - j * 40)
    fin_line.stamp()

# The Onscreen title
title = turtle.Turtle()
title.goto(-100, 50)
title.pencolor('White')
title.write(screen_title, font=("Arial", 15, "normal"))
title.hideturtle()

# Create two turtle objects
T1 = turtle.Turtle()
T2 = turtle.Turtle()

R1 = turtle.Turtle()
R1.hideturtle()
R1.penup()
R1.goto(-290, 10)
R1.color(t1_border, t1_fill)
R1.write(name1, font=("Arial", 15, "normal"))

T1.shape(turtle_shape)
T1.color(t1_border, t1_fill)
T1.penup()
T1.goto(-200, 20)
T1.penup()

R2 = turtle.Turtle()
R2.hideturtle()
R2.penup()
R2.goto(-290, -30)
R2.color(t2_border, t2_fill)
R2.write(name2, font=("Arial", 15, "normal"))

T2.shape(turtle_shape)
T2.color(t2_border, t2_fill)
T2.color()
T2.penup()
T2.goto(-200, -20)
T2.penup()

# Simulate the race
for i in range(250):
    T1.forward(randint(1, 5))
    T2.forward(randint(1, 5))

    if T1.xcor() >= distance or T2.xcor() >= distance:
        break

# Determine the winner
if T1.xcor() >= distance and T2.xcor() >= distance:
    winner_message = "It's a tie!"
    color = 'White'

elif T1.xcor() >= distance:
    if bet == name1:
        winner_message = f"Congratulations! You won against {name2}.\nYou win the bet on Racer 1!"
        color = 'Green'
    elif bet == name2:
        winner_message = f"{name1} wins, and you lost your bet on Racer 2."
        color = 'Red'
    else:
        winner_message = "YOU BET WHO?!\nPlease Try Again."
        color = 'Red'

elif T2.xcor() >= distance:
    if bet == name2:
        winner_message = f"Congratulations! You won against {name1}.\nYou win the bet on Racer 2"
        color = 'Green'
    elif bet == name1:
        winner_message = f"{name2} wins, and you lost your bet on Racer 1."
        color = 'Red'
    else:
        winner_message = "YOU BET WHO?!\nPlease Try Again."
        color = 'Red'
else:
    winner_message = "Please Try Again."
    color = 'White'

# Display the winner message on the screen
result = turtle.Turtle()
result.goto(0, -15)
result.color(color)
result.write(winner_message, align="center", font=("Arial", 14, "normal"))
result.hideturtle()

if bet == name1:
    print(f"\nThe winner is {name1}, Congratulations!")
else:
    print(f"\nThe winner is {name2}, Congratulations!")

print("\nRace and Bet again!\n  Enjoy the Game!!")

# Close the turtle graphics window when clicked
turtle.done()
turtle.exitonclick()