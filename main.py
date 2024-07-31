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

score = 0
direction = 'down'


def personalize_game():
    window = Toplevel()

    window.title("Snake game settings")
    window.resizable(False, False)

    window.geometry("600x400")

    x = IntVar()
    y = IntVar()
    z = IntVar()
    q = IntVar()

    Label(window, text="Background color", font=('consolas', 30)).grid(row=0, column=0, columnspan=4)
    Radiobutton(window, text="black", variable=x, font=('consolas', 10), value=1, indicatoron=False,
                command=lambda: set_background(x)).grid(row=1, column=0)
    Radiobutton(window, text="red", variable=x, font=('consolas', 10), value=2, indicatoron=False,
                command=lambda: set_background(x)).grid(row=1, column=1)
    Radiobutton(window, text="blue", variable=x, font=('consolas', 10), value=3, indicatoron=False,
                command=lambda: set_background(x)).grid(row=1, column=3)
    Radiobutton(window, text="pink", variable=x, font=('consolas', 10), value=13, indicatoron=False,
                command=lambda: set_background(x)).grid(row=1, column=4)

    Label(window, text="Snake color", font=('consolas', 30)).grid(row=2, column=0, columnspan=4)
    Radiobutton(window, text="black", variable=y, indicatoron=False, value=4, font=('consolas', 10),
                command=lambda: set_snake_color(y)).grid(row=3,
                                                         column=0)
    Radiobutton(window, text="red", variable=y, indicatoron=False, value=5, font=('consolas', 10),
                command=lambda: set_snake_color(y)).grid(row=3, column=1)
    Radiobutton(window, text="blue", variable=y, indicatoron=False, value=6, font=('consolas', 10),
                command=lambda: set_snake_color(y)).grid(row=3, column=3)
    Radiobutton(window, text="pink", variable=y, indicatoron=False, value=14, font=('consolas', 10),
                command=lambda: set_snake_color(y)).grid(row=3, column=4)

    Label(window, text="Food color", font=('consolas', 30)).grid(row=4, column=0, columnspan=4)
    Radiobutton(window, text="black", variable=z, indicatoron=False, value=7, font=('consolas', 10),
                command=lambda: set_food_color(z)).grid(row=5, column=0)
    Radiobutton(window, text="red", variable=z, indicatoron=False, value=8, font=('consolas', 10),
                command=lambda: set_food_color(z)).grid(row=5, column=1)
    Radiobutton(window, text="blue", variable=z, indicatoron=False, value=9, font=('consolas', 10),
                command=lambda: set_food_color(z)).grid(row=5,column=3)
    Radiobutton(window, text="pink", variable=z, indicatoron=False, value=15, font=('consolas', 10),
                command=lambda: set_food_color(z)).grid(row=5, column=4)

    Label(window, text="Speed", font=('consolas', 30)).grid(row=6, column=0, columnspan=4)
    Radiobutton(window, text="slow", variable=q, indicatoron=False, value=10, font=('consolas', 10),
                command=lambda: set_speed(q)).grid(row=7, column=0)
    Radiobutton(window, text="medium", variable=q, indicatoron=False, value=11, font=('consolas', 10),
                command=lambda: set_speed(q)).grid(row=7,column=1)
    Radiobutton(window, text="fast", variable=q, indicatoron=False, value=12, font=('consolas', 10),
                command=lambda: set_speed(q)).grid(row=7, column=3)
    Radiobutton(window, text="super fast", variable=q, indicatoron=False, value=16, font=('consolas', 10),
                command=lambda: set_speed(q)).grid(row=7, column=4)

    button = Button(window, text="Start game", command=create_game)
    button.place(relx=0.3, rely=0.9, anchor="n")

    window.mainloop()


def set_background(x):
    global BACKGROUND_COLOR
    if x.get() == 1:
        general.BACKGROUND_COLOR = "#000000"
        BACKGROUND_COLOR = general.BACKGROUND_COLOR
    elif x.get() == 2:
        general.BACKGROUND_COLOR = "red"
        BACKGROUND_COLOR = general.BACKGROUND_COLOR
    elif x.get() == 3:
        general.BACKGROUND_COLOR = "blue"
        BACKGROUND_COLOR = general.BACKGROUND_COLOR
    elif x.get() == 13:
        general.BACKGROUND_COLOR = "pink"
        BACKGROUND_COLOR = general.BACKGROUND_COLOR


def set_snake_color(y):
    global SNAKE_COLOR
    if y.get() == 4:
        general.SNAKE_COLOR = "#000000"
        SNAKE_COLOR = general.SNAKE_COLOR
    elif y.get() == 5:
        general.SNAKE_COLOR = "red"
        SNAKE_COLOR = general.SNAKE_COLOR
    elif y.get() == 6:
        general.SNAKE_COLOR = "blue"
        SNAKE_COLOR = general.SNAKE_COLOR
    elif y.get() == 14:
        general.SNAKE_COLOR = "pink"
        SNAKE_COLOR = general.SNAKE_COLOR

def set_food_color(z):
    global FOOD_COLOR
    if z.get()==7:
        general.FOOD_COLOR = "#000000"
        FOOD_COLOR = general.FOOD_COLOR
    elif z.get()==8:
        general.FOOD_COLOR = "red"
        FOOD_COLOR = general.FOOD_COLOR
    elif z.get()==9:
        general.FOOD_COLOR = "blue"
        FOOD_COLOR = general.FOOD_COLOR
    elif z.get()==15:
        general.FOOD_COLOR = "pink"
        FOOD_COLOR = general.FOOD_COLOR

def set_speed(q):
    global SPEED
    if q.get()==10:
        general.SPEED = 150
        SPEED = general.SPEED
    elif q.get()==11:
        general.SPEED = 100
        SPEED = general.SPEED
    elif q.get()==12:
        general.SPEED = 50
        SPEED = general.SPEED
    elif q.get()==16:
        general.SPEED = 35
        SPEED = general.SPEED


def create_game():
    root.destroy()

    window = Tk()

    window.title("Snake game")
    window.resizable(False, False)

    label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
    label.pack()

    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
    canvas.pack()

    window.update()

    #Here, I try to place the game window as much in the center of the screen as possible
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    #essential line for keyboard events to work,
    #because initially focus is not on this window
    window.focus_force()

    #Here I set the keyboard events for changing the snake's directions
    window.bind('<Left>', lambda event: change_direction('left'))
    window.bind('<Right>', lambda event: change_direction('right'))
    window.bind('<Down>', lambda event: change_direction('down'))
    window.bind('<Up>', lambda event: change_direction('up'))

    snake = Snake(canvas, general)
    food = Food(canvas, general)

    next_turn(snake, food, canvas, label, window)

    window.mainloop()


def next_turn(snake, food, canvas, label, window):
    x, y = snake.coordinates[0]

    global direction

    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":

        y += SPACE_SIZE

    elif direction == "left":

        x -= SPACE_SIZE

    elif direction == "right":

        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        label.config(text="Score:{}".format(score))

        canvas.delete("food")  #via tag

        food = Food(canvas, general)
    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_colisions(snake):

        game_over(canvas)

    else:

        window.after(SPEED, next_turn, snake, food, canvas, label, window)


def change_direction(new_direction):
    global direction  #the old direction

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

    if x < 0 or x >= GAME_WIDTH:
        print("Game over!")
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        print("Game over!")
        return True

    for body_part in snake.coordinates[1:]:  #everything after the head of the snake
        if x == body_part[0] and y == body_part[1]:
            print("Game over!")
            return True
    return False


def game_over(canvas):
    canvas.delete(ALL)
    canvas.create_text((canvas.winfo_width() / 2), (canvas.winfo_height() / 2), font=('consolas', 70), text="GAME OVER",
                       fill="blue", tag="game")


root = Tk()
root.title("Snake game")
background_image = PhotoImage(file="snake.png")

# Here, I try to place the game window as much in the center of the screen as possible
window_width = background_image.width()
window_height = background_image.height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

button1 = Button(root, text="Play game", command=create_game)
button1.place(relx=0.3, rely=0.5, anchor="e")

button2 = Button(root, text="Settings", command=personalize_game)
button2.place(relx=0.8, rely=0.5, anchor="w")

root.mainloop()
