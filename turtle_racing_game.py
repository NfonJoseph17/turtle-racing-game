import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'orange', 'yellow', 'green', 'violet', 'blue', 'black', 'purple', 'pink', 'brown', 'cyan']


def get_numb_of_racers():
    racers = 0
    while True:
        racers = input("How many racers do you want? [2-10]")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Please enter a number")
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print("Please enter a number within the range 2 to 10")



def race(colors):
    turtles = create_turtle(color)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x,y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


def create_turtle(colors):
    turtles = []
    spacingx = WIDTH / (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.title("Turtle Racing Game")


racers = get_numb_of_racers()
init_turtle()
random.shuffle(COLORS)
color = COLORS[:racers]
winner = race(color)
print(f"The winner is {winner}")
time.sleep(5)
