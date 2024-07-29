from tkinter import *
import random
from Snake import *
from Food import *
from General_settings import *

#Initialize the game settings by using an object
general = Generals()
GAME_WIDTH = general.GAME_WIDTH
GAME_HEIGHT = general.GAME_HEIGHT
SPEED = general.SPEED
SPACE_SIZE = general.SPACE_SIZE
BODY_PARTS = general.BODY_PARTS
SNAKE_COLOR = general.SNAKE_COLOR
FOOD_COLOR = general.FOOD_COLOR
BACKGROUND_COLOR = general.BACKGROUND_COLOR

def next_turn(snake, food):

    x, y = snake.coordinates[0]

    if direction == "up":
         y -= SPACE_SIZE

    elif direction == "down":

        y += SPACE_SIZE

    elif direction == "left":

        x -= SPACE_SIZE

    elif direction == "right":

        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        label.config(text="Score:{}".format(score))

        canvas.delete("food") #via tag

        food = Food(canvas, general)
    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_colisions(snake):

        game_over()

    else:

        window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):

    global direction #the old direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction


def check_colisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >=  GAME_WIDTH:
        print("Game over!")
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        print("Game over!")
        return True

    for body_part in snake.coordinates[1:]: #everything after the head of the snake
        if x == body_part[0] and y == body_part[1]:
            print("Game over!")
            return True
    return False



def game_over():

    canvas.delete(ALL)
    canvas.create_text((canvas.winfo_width()/2), (canvas.winfo_height()/2), font=('consolas',70), text="GAME OVER", fill="blue", tag="game")

window = Tk()

window.title("Snake game")
window.resizable(False,False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score),font=('consolas',40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

#Here, I try to place the game window as much in the center of the screen as possible
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

#Here I set the keyboard events for changing the snake's directions
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Down>', lambda event: change_direction('down'))
window.bind('<Up>', lambda event: change_direction('up'))

snake = Snake(canvas, general)
food = Food(canvas, general)

next_turn(snake,food)

window.mainloop()