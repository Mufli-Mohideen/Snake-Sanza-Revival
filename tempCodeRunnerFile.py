from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
score = 0  # Initialize the score variable

def change(x, y):
    aim.x = x
    aim.y = y

def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    global score  # Access the global score variable
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        update()
        lose_message = f"You lost!\nBetter luck next time.\nScore: {score}"
        draw_message(lose_message)  # Show lose message on the screen
        return

    snake.append(head)

    if head == food:
        score += 5  # Increase the score by 5 points
        print("Score:", score)  # Print the updated score
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'green')  # Changed snake color to green
    square(food.x, food.y, 9, 'blue')     # Changed food color to blue
    update()
    ontimer(move, 100)

def draw_message(message):
    """Draw a message on the screen."""
    goto(0, 0)
    color('white')
    write(message, align='center', font=('Arial', 18, 'normal'))

setup(420, 420, 370, 0)
bgcolor('black')  # Changed background color to black
hideturtle()
tracer(False)

listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')  # Corrected the direction keys
onkey(lambda: change(0, 10), 'Up')     # Corrected the direction keys
onkey(lambda: change(0, -10), 'Down')  # Corrected the direction keys

move()
done()
