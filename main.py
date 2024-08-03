from tkinter import *
import random
from tkinter import colorchooser
from Snake import *
from Food import *
from SpecialFood import *
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
wasSettingsClicked = 0
rareSpecialFood = 0 #in order to count special food, so that they appear randomly


def personalize_game():
    global wasSettingsClicked
    wasSettingsClicked = 1
    root.destroy()

    window = Tk()

    window.title("Snake game settings")
    window.resizable(False, False)

    window.geometry("600x400")

    x = IntVar()
    y = IntVar()
    z = IntVar()
    q = IntVar()

    #options for Background color -----------------------------------------------------------------------

    Label(window, text="Background color", font=('consolas', 30)).grid(row=0, column=0, columnspan=5)
    Radiobutton(window, text="black", variable=x, font=('consolas', 10), value=1, indicatoron=False,
                command=lambda: set_background(x)).grid(row=1, column=0)
    Radiobutton(window, text="red", variable=x, font=('consolas', 10), value=2, indicatoron=False,
                command=lambda: set_background(x)).grid(row=1, column=1)
    Radiobutton(window, text="blue", variable=x, font=('consolas', 10), value=3, indicatoron=False,
                command=lambda: set_background(x)).grid(row=1, column=3)
    Radiobutton(window, text="pink", variable=x, font=('consolas', 10), value=13, indicatoron=False,
                command=lambda: set_background(x)).grid(row=1, column=4)
    Radiobutton(window, text="custom", variable=x, font=('consolas',10), value=16, indicatoron=False,
                command=lambda: set_background(x)).grid(row=1, column=5)

    #options for Snake color -------------------------------------------------------------------------

    Label(window, text="Snake color", font=('consolas', 30)).grid(row=2, column=0, columnspan=5)
    Radiobutton(window, text="black", variable=y, indicatoron=False, value=4, font=('consolas', 10),
                command=lambda: set_snake_color(y)).grid(row=3,
                                                         column=0)
    Radiobutton(window, text="red", variable=y, indicatoron=False, value=5, font=('consolas', 10),
                command=lambda: set_snake_color(y)).grid(row=3, column=1)
    Radiobutton(window, text="blue", variable=y, indicatoron=False, value=6, font=('consolas', 10),
                command=lambda: set_snake_color(y)).grid(row=3, column=3)
    Radiobutton(window, text="pink", variable=y, indicatoron=False, value=14, font=('consolas', 10),
                command=lambda: set_snake_color(y)).grid(row=3, column=4)
    Radiobutton(window, text="custom", variable=y, indicatoron=False, value=17, font=('consolas', 10),
                command=lambda: set_snake_color(y)).grid(row=3, column=5)

    #options for Food color -------------------------------------------------------------------------

    Label(window, text="Food color", font=('consolas', 30)).grid(row=4, column=0, columnspan=5)
    Radiobutton(window, text="black", variable=z, indicatoron=False, value=7, font=('consolas', 10),
                command=lambda: set_food_color(z)).grid(row=5, column=0)
    Radiobutton(window, text="red", variable=z, indicatoron=False, value=8, font=('consolas', 10),
                command=lambda: set_food_color(z)).grid(row=5, column=1)
    Radiobutton(window, text="blue", variable=z, indicatoron=False, value=9, font=('consolas', 10),
                command=lambda: set_food_color(z)).grid(row=5,column=3)
    Radiobutton(window, text="pink", variable=z, indicatoron=False, value=15, font=('consolas', 10),
                command=lambda: set_food_color(z)).grid(row=5, column=4)
    Radiobutton(window, text="custom", variable=z, indicatoron=False, value=18, font=('consolas',10),
                command=lambda: set_food_color(z)).grid(row=5, column=5)

    #options for Speed -------------------------------------------------------------------------------

    Label(window, text="Speed", font=('consolas', 30)).grid(row=6, column=0, columnspan=5)
    Radiobutton(window, text="slow", variable=q, indicatoron=False, value=10, font=('consolas', 10),
                command=lambda: set_speed(q)).grid(row=7, column=0)
    Radiobutton(window, text="medium", variable=q, indicatoron=False, value=11, font=('consolas', 10),
                command=lambda: set_speed(q)).grid(row=7,column=1)
    Radiobutton(window, text="fast", variable=q, indicatoron=False, value=12, font=('consolas', 10),
                command=lambda: set_speed(q)).grid(row=7, column=3)
    Radiobutton(window, text="super fast", variable=q, indicatoron=False, value=16, font=('consolas', 10),
                command=lambda: set_speed(q)).grid(row=7, column=4)
    Radiobutton(window, text="custom", variable=q, indicatoron=False, value=19, font=('consolas',10),
                command=lambda: set_speed(q)).grid(row=7, column=5)

    button = Button(window, text="Start game", command=lambda: done_with_settings(window))
    button.place(relx=0.3, rely=0.9, anchor="n")

    window.mainloop()

def done_with_settings(window):
    window.destroy()
    create_game()


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
    elif x.get() == 16:
        color = colorchooser.askcolor()
        general.BACKGROUND_COLOR = color[1] #color in hexadecimal value
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
    elif y.get() == 17:
        color = colorchooser.askcolor()
        general.SNAKE_COLOR = color[1] #Hex value of the color
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
    elif z.get()==18:
        color = colorchooser.askcolor()
        general.FOOD_COLOR = color[1] #Hex value of returned color
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
    elif q.get() ==19:
        fereastra = Toplevel()

        window_width = 120
        window_height = 440
        screen_width = fereastra.winfo_screenwidth()
        screen_height = fereastra.winfo_screenheight()

        #move window a little to the right
        x = int((screen_width / 2) - (window_width / 2)) + 100  #+100 to move further right
        y = int((screen_height / 2) - (window_height / 2))

        fereastra.geometry(f"{window_width}x{window_height}+{x}+{y}")

        fastImage = PhotoImage(file="fast.png")
        fastLabel = Label(fereastra, image=fastImage)
        fastLabel.pack()

        scale = Scale(fereastra,
                      from_=30,
                      to=150,
                      length=200,
                      troughcolor='black')
        scale.set(70)
        scale.pack()

        slowImage = PhotoImage(file="slow.png")
        slowLabel = Label(fereastra,image=slowImage)
        slowLabel.pack()

        button = Button(fereastra, text='submit',command=lambda: setSpeed(scale,fereastra))
        button.pack()

        fereastra.mainloop()

def setSpeed(scale,fereastra):
    global SPEED
    general.SPEED = scale.get()
    SPEED = general.SPEED
    fereastra.destroy()

def create_game():
    global wasSettingsClicked
    if wasSettingsClicked == 0:
        root.destroy()
    else:
        pass

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
    special_food = SpecialFood(canvas, general)

    next_turn(snake, food, special_food, canvas, label, window)

    window.mainloop()


def next_turn(snake, food, special_food, canvas, label, window):

    #the head of the snake
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

    #insert x,y at the head of the snake
    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    global score, rareSpecialFood

    #snake head and food are overlapping
    if x == food.coordinates[0] and y == food.coordinates[1]:

        score += 1

        #if the normal food is eaten before the special one,
        #the special one expires
        canvas.delete("specialfood")

        rareSpecialFood +=1

        #special food is created randomly
        if rareSpecialFood == random.randint(1,2):
            special_food = SpecialFood(canvas, general)
            rareSpecialFood = 0
        elif rareSpecialFood > 2:
            rareSpecialFood=0

        #update the score label
        label.config(text="Score:{}".format(score))

        canvas.delete("food")  #via tag

        #another food object is created
        food = Food(canvas, general)

    elif x == special_food.coordinates[0] and y == special_food.coordinates[1]:

        score += 3

        label.config(text="Score:{}".format(score))

        canvas.delete("specialfood")

    else:

        #deletes the coordinates of the last part of the snake, to create the moving action
        del snake.coordinates[-1]

        #update the canvas
        canvas.delete(snake.squares[-1])

        #deletes the last square of the snake
        del snake.squares[-1]

    if check_collisions(snake):

        game_over(canvas)

    else:

        window.after(SPEED, next_turn, snake, food, special_food, canvas, label, window)


def change_direction(new_direction):
    # the old direction
    global direction

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

def check_collisions(snake):

    #head of the snake
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        print("Game over!")
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        print("Game over!")
        return True

    # everything after the head of the snake
    for body_part in snake.coordinates[1:]:
        #if the head of the snake touches another part of its body
        if x == body_part[0] and y == body_part[1]:
            print("Game over!")
            return True
    return False


def game_over(canvas):
    canvas.delete(ALL)
    canvas.create_text((canvas.winfo_width() / 2),
                       (canvas.winfo_height() / 2),
                       font=('consolas', 70),
                       text="GAME OVER",
                       fill="blue",
                       tag="game")


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
