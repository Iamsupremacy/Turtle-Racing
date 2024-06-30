import turtle
import time
import random
WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'brown', 'green', 'cyan', 'yellow', 'purple', 'black', 'orange', 'blue', 'pink']

# Taking a valid input form user
def get_number_of_turtle():
    racer = 0
    while True:
        racers = input("How many turtles you want have race with?(2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Enter a valid input")
            continue
        if 2 <= racers <= 8:
            return racers
        else:
            print("Numbers are not in range!! Try again.")
def race(colors):
    turtles = create_turtle(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

def create_turtle(colors):
    turtles = []
    spacingx = WIDTH // (len(colors)+1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i+1) * spacingx, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles



# creating a screen
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Tutle Racer')
racers = get_number_of_turtle()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
print(winner)
print("The winner is: ", winner)
# time.sleep(1)
turtle.TK.messagebox.showinfo(title="Winner", message=winner)
turtle.exitonclick()
