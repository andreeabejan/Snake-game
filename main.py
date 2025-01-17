from tkinter import *
import random
from tkinter import colorchooser
from Snake import *
from SecondSnake import *
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
score_player_2 = 0
direction = 'down'
direction_player_2 = 'right'
wasSettingsClicked = 0
rareSpecialFood = 0  #in order to count special food, so that they appear randomly
MULTIPLAYER = 1
DIFFICULTY = "easy"
food = None
special_food = None


def personalize_game():
    global wasSettingsClicked
    wasSettingsClicked = 1
    root.destroy()

    window = Tk()

    window.title("Snake game settings")
    window.resizable(False, False)
    window.config(bg="lightblue")
    window.geometry("500x550")

    x = IntVar()
    y = IntVar()
    z = IntVar()
    q = IntVar()
    a = IntVar()
    b = IntVar()

    #options for Background color -----------------------------------------------------------------------

    Label(window, text="Background color", background="lightblue", font=('consolas', 30)).grid(row=0, column=0, columnspan=5)
    Radiobutton(window, text="black", variable=x, font=('consolas', 10), value=1, indicatoron=False,
                command=lambda: set_background(x)).grid(row=1, column=0)
    Radiobutton(window, text="red", variable=x, font=('consolas', 10), value=2, indicatoron=False,
                command=lambda: set_background(x)).grid(row=1, column=1)
    Radiobutton(window, text="blue", variable=x, font=('consolas', 10), value=3, indicatoron=False,
                command=lambda: set_background(x)).grid(row=1, column=3)
    Radiobutton(window, text="pink", variable=x, font=('consolas', 10), value=13, indicatoron=False,
                command=lambda: set_background(x)).grid(row=1, column=4)
    Radiobutton(window, text="custom", variable=x, font=('consolas', 10), value=16, indicatoron=False,
                command=lambda: set_background(x)).grid(row=1, column=5)

    #options for Snake color -------------------------------------------------------------------------

    Label(window, text="Snake color", background="lightblue", font=('consolas', 30)).grid(row=2, column=0, columnspan=5)
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

    Label(window, text="Food color", background="lightblue", font=('consolas', 30)).grid(row=4, column=0, columnspan=5)
    Radiobutton(window, text="black", variable=z, indicatoron=False, value=7, font=('consolas', 10),
                command=lambda: set_food_color(z)).grid(row=5, column=0)
    Radiobutton(window, text="red", variable=z, indicatoron=False, value=8, font=('consolas', 10),
                command=lambda: set_food_color(z)).grid(row=5, column=1)
    Radiobutton(window, text="blue", variable=z, indicatoron=False, value=9, font=('consolas', 10),
                command=lambda: set_food_color(z)).grid(row=5, column=3)
    Radiobutton(window, text="pink", variable=z, indicatoron=False, value=15, font=('consolas', 10),
                command=lambda: set_food_color(z)).grid(row=5, column=4)
    Radiobutton(window, text="custom", variable=z, indicatoron=False, value=18, font=('consolas', 10),
                command=lambda: set_food_color(z)).grid(row=5, column=5)

    #options for Speed -------------------------------------------------------------------------------

    Label(window, text="Speed", background="lightblue", font=('consolas', 30)).grid(row=6, column=0, columnspan=5)
    Radiobutton(window, text="slow", variable=q, indicatoron=False, value=10, font=('consolas', 10),
                command=lambda: set_speed(q)).grid(row=7, column=0)
    Radiobutton(window, text="medium", variable=q, indicatoron=False, value=11, font=('consolas', 10),
                command=lambda: set_speed(q)).grid(row=7, column=1)
    Radiobutton(window, text="fast", variable=q, indicatoron=False, value=12, font=('consolas', 10),
                command=lambda: set_speed(q)).grid(row=7, column=3)
    Radiobutton(window, text="super fast", variable=q, indicatoron=False, value=16, font=('consolas', 10),
                command=lambda: set_speed(q)).grid(row=7, column=4)
    Radiobutton(window, text="custom", variable=q, indicatoron=False, value=19, font=('consolas', 10),
                command=lambda: set_speed(q)).grid(row=7, column=5)

    #number of players -------------------------------------------------------------------------------------------------

    #not functional yet
    # Label(window, text="Number of players", background="lightblue", font=('consolas', 30)).grid(row=8, column=0, columnspan=5)
    # Radiobutton(window, text="single", variable=a, font=('consolas', 10), value=1, indicatoron=False,
    #             command=lambda: set_players(a)).grid(row=9, column=1)
    # Radiobutton(window, text="two player", variable=a, font=('consolas', 10), value=2, indicatoron=False,
    #             command=lambda: set_players(a)).grid(row=9, column=3)

    #difficulty -------------------------------------------------------------------------------------------------

    Label(window, text="Difficulty", background="lightblue", font=('consolas', 30)).grid(row=10, column=0, columnspan=5)
    Radiobutton(window, text="easy", variable=b, font=('consolas', 10), value=1, indicatoron=False,
                command=lambda: set_difficulty(b)).grid(row=11, column=1)
    Radiobutton(window, text="hard", variable=b, font=('consolas', 10), value=2, indicatoron=False,
                command=lambda: set_difficulty(b)).grid(row=11, column=3)

    button = Button(window, text="Start game", command=lambda: done_with_settings(window))
    button.place(relx=0.3, rely=0.9, anchor="n")

    window.mainloop()


def done_with_settings(window):

    global MULTIPLAYER
    global SPACE_SIZE

    window.destroy()
    if MULTIPLAYER == 1:
        create_game()
    else:
        #make space size smaller for two player game
        general.SPACE_SIZE = 15
        SPACE_SIZE = general.SPACE_SIZE
        multiplayer_game()


def set_players(a):

    global MULTIPLAYER

    if a.get() == 1:
        MULTIPLAYER = 1
    elif a.get() == 2:
        MULTIPLAYER = 2


def set_difficulty(b):

    global DIFFICULTY

    if b.get() == 1:
        DIFFICULTY = "easy"
    elif b.get() == 2:
        DIFFICULTY = "hard"


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
        general.BACKGROUND_COLOR = color[1]  #color in hexadecimal value
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
        general.SNAKE_COLOR = color[1]  #Hex value of the color
        SNAKE_COLOR = general.SNAKE_COLOR


def set_food_color(z):
    global FOOD_COLOR
    if z.get() == 7:
        general.FOOD_COLOR = "#000000"
        FOOD_COLOR = general.FOOD_COLOR
    elif z.get() == 8:
        general.FOOD_COLOR = "red"
        FOOD_COLOR = general.FOOD_COLOR
    elif z.get() == 9:
        general.FOOD_COLOR = "blue"
        FOOD_COLOR = general.FOOD_COLOR
    elif z.get() == 15:
        general.FOOD_COLOR = "pink"
        FOOD_COLOR = general.FOOD_COLOR
    elif z.get() == 18:
        color = colorchooser.askcolor()
        general.FOOD_COLOR = color[1]  #Hex value of returned color
        FOOD_COLOR = general.FOOD_COLOR


def set_speed(q):
    global SPEED
    if q.get() == 10:
        general.SPEED = 150
        SPEED = general.SPEED
    elif q.get() == 11:
        general.SPEED = 100
        SPEED = general.SPEED
    elif q.get() == 12:
        general.SPEED = 50
        SPEED = general.SPEED
    elif q.get() == 16:
        general.SPEED = 35
        SPEED = general.SPEED
    elif q.get() == 19:
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
        slowLabel = Label(fereastra, image=slowImage)
        slowLabel.pack()

        button = Button(fereastra, text='submit', command=lambda: submit_speed(scale, fereastra))
        button.pack()

        fereastra.mainloop()


def submit_speed(scale, fereastra):
    global SPEED
    general.SPEED = scale.get()
    SPEED = general.SPEED
    fereastra.destroy()


def multiplayer_game():
    window = Tk()

    window.title("Snake game")
    window.resizable(False, False)

    label = Label(window, text="   player1:{}  ||     player2:{}".format(score, score_player_2), font=('consolas', 40))
    label.pack()

    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
    canvas.pack()

    window.update()

    # Here, I try to place the game window as much in the center of the screen as possible
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # essential line for keyboard events to work,
    # because initially focus is not on this window
    window.focus_force()

    # Here I set the keyboard events for changing the first snake's directions
    window.bind('<Left>', lambda event: change_direction('left'))
    window.bind('<Right>', lambda event: change_direction('right'))
    window.bind('<Down>', lambda event: change_direction('down'))
    window.bind('<Up>', lambda event: change_direction('up'))

    # Here I set the keyboard events for changing the second snake's directions
    window.bind('a', lambda event: change_second_direction('left'))
    window.bind('d', lambda event: change_second_direction('right'))
    window.bind('s', lambda event: change_second_direction('down'))
    window.bind('w', lambda event: change_second_direction('up'))

    global food, special_food

    snake = Snake(canvas, general)
    second_snake = SecondSnake(canvas, general)
    food = Food(canvas, general)
    special_food = SpecialFood(canvas, general)

    #loop for both snakes to work at the same time
    run_both_snakes(snake, second_snake, canvas, label, window)

    window.mainloop()


def run_both_snakes(snake, second_snake, canvas, label, window):

    global food, special_food

    next_turn_first_player(snake, canvas, label, window)
    next_turn_player_2(second_snake, canvas, label, window)
    window.after(1000, run_both_snakes, snake, second_snake, canvas, label, window)


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

    global food, special_food

    snake = Snake(canvas, general)
    food = Food(canvas, general)
    special_food = SpecialFood(canvas, general)

    next_turn(snake, canvas, label, window)

    window.mainloop()


def special_effect(snake, canvas):
    colors = ["red", "blue", "green", "yellow", "purple"]
    for i in range(len(snake.squares)):
        color = random.choice(colors)
        canvas.itemconfig(snake.squares[i], fill=color)
    #timer to reset the snake color after 4 seconds
    canvas.after(4000, snake.reset_color, canvas, general)


def next_turn(snake, canvas, label, window):
    #the head of the snake
    x, y = snake.coordinates[0]

    global direction, food, special_food

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

        rareSpecialFood += 1

        #special food is created randomly
        if rareSpecialFood == random.randint(1, 2):
            special_food = SpecialFood(canvas, general)
            rareSpecialFood = 0
        elif rareSpecialFood > 2:
            rareSpecialFood = 0

        #update the score label
        label.config(text="Score:{}".format(score))

        canvas.delete("food")  #via tag

        #another food object is created
        food = Food(canvas, general)

    elif x == special_food.coordinates[0] and y == special_food.coordinates[1]:

        score += 3

        special_effect(snake,canvas)

        label.config(text="Score:{}".format(score))

        canvas.delete("specialfood")

    else:

        #deletes the coordinates of the last part of the snake, to create the moving action
        del snake.coordinates[-1]

        #update the canvas
        canvas.delete(snake.squares[-1])

        #deletes the last square of the snake
        del snake.squares[-1]

    if check_collisions(snake, canvas):

        game_over(canvas)

    else:

        window.after(50, next_turn, snake, canvas, label, window)


def next_turn_first_player(snake, canvas, label, window):

    # the head of the snake
    x, y = snake.coordinates[0]

    global direction, food, special_food

    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":

        y += SPACE_SIZE

    elif direction == "left":

        x -= SPACE_SIZE

    elif direction == "right":

        x += SPACE_SIZE

    # insert x,y at the head of the snake
    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    global score, score_player_2, rareSpecialFood

    # snake head and food are overlapping
    if x == food.coordinates[0] and y == food.coordinates[1]:

        score += 1

        # if the normal food is eaten before the special one,
        # the special one expires
        canvas.delete("specialfood")

        rareSpecialFood += 1

        # special food is created randomly
        if rareSpecialFood == random.randint(1, 2):
            special_food = SpecialFood(canvas, general)
            rareSpecialFood = 0
        elif rareSpecialFood > 2:
            rareSpecialFood = 0

        # update the score label
        label.config(text="   player1:{}  ||     player2:{}".format(score, score_player_2))

        canvas.delete("food")  # via tag

        # another food object is created
        food = Food(canvas, general)

    elif x == special_food.coordinates[0] and y == special_food.coordinates[1]:

        score += 3

        label.config(text="   player1:{}  ||     player2:{}".format(score, score_player_2))

        canvas.delete("specialfood")

    else:

        # deletes the coordinates of the last part of the snake, to create the moving action
        del snake.coordinates[-1]

        # update the canvas
        canvas.delete(snake.squares[-1])

        # deletes the last square of the snake
        del snake.squares[-1]

    if check_collisions(snake, canvas):

        canvas.delete(ALL)

        score -= 5
        label.config(text="   player1:{}  ||     player2:{}".format(score, score_player_2))
        if score > score_player_2:
            canvas.create_text((canvas.winfo_width() / 2),
                               (canvas.winfo_height() / 2),
                               font=('consolas', 50),
                               text="First player wins!",
                               fill="yellow",
                               tag="game")
        elif score == score_player_2:
            canvas.create_text((canvas.winfo_width() / 2),
                               (canvas.winfo_height() / 2),
                               font=('consolas', 50),
                               text="Tie!",
                               fill="yellow",
                               tag="game")
        else:
            canvas.create_text((canvas.winfo_width() / 2),
                               (canvas.winfo_height() / 2),
                               font=('consolas', 50),
                               text="Second player wins!",
                               fill="yellow",
                               tag="game")

    else:

        window.after(300, next_turn_first_player, snake, canvas, label, window)


def next_turn_player_2(second_snake, canvas, label, window):
    # the head of the snake
    x, y = second_snake.coordinates[0]

    global direction_player_2, food, special_food

    if direction_player_2 == "up":
        y -= SPACE_SIZE

    elif direction_player_2 == "down":

        y += SPACE_SIZE

    elif direction_player_2 == "left":

        x -= SPACE_SIZE

    elif direction_player_2 == "right":

        x += SPACE_SIZE

    # insert x,y at the head of the snake
    second_snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill="pink")
    second_snake.squares.insert(0, square)

    global score, score_player_2, rareSpecialFood

    # snake head and food are overlapping
    if x == food.coordinates[0] and y == food.coordinates[1]:

        score_player_2 += 1

        # if the normal food is eaten before the special one,
        # the special one expires
        canvas.delete("specialfood")

        rareSpecialFood += 1

        # special food is created randomly
        if rareSpecialFood == random.randint(1, 2):
            special_food = SpecialFood(canvas, general)
            rareSpecialFood = 0
        elif rareSpecialFood > 2:
            rareSpecialFood = 0

        # update the score label
        label.config(text="   player1:{}  ||     player2:{}".format(score, score_player_2))

        canvas.delete("food")  # via tag

        # another food object is created
        food = Food(canvas, general)

    elif x == special_food.coordinates[0] and y == special_food.coordinates[1]:

        score_player_2 += 3

        label.config(text="   player1:{}  ||     player2:{}".format(score, score_player_2))

        canvas.delete("specialfood")

    else:

        # deletes the coordinates of the last part of the snake, to create the moving action
        del second_snake.coordinates[-1]

        # update the canvas
        canvas.delete(second_snake.squares[-1])

        # deletes the last square of the snake
        del second_snake.squares[-1]

    if check_collisions(second_snake, canvas):

        canvas.delete(ALL)

        score_player_2 -= 5
        label.config(text="   player1:{}  ||     player2:{}".format(score, score_player_2))
        if score < score_player_2:
            canvas.create_text((canvas.winfo_width() / 2),
                               (canvas.winfo_height() / 2),
                               font=('consolas', 50),
                               text="Second player wins!",
                               fill="yellow",
                               tag="game")
        elif score == score_player_2:
            canvas.create_text((canvas.winfo_width() / 2),
                               (canvas.winfo_height() / 2),
                               font=('consolas', 50),
                               text="Tie!",
                               fill="yellow",
                               tag="game")
        else:
            canvas.create_text((canvas.winfo_width() / 2),
                               (canvas.winfo_height() / 2),
                               font=('consolas', 50),
                               text="First player wins!",
                               fill="yellow",
                               tag="game")


    else:

        window.after(300, next_turn_player_2, second_snake, canvas, label, window)


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


def change_second_direction(new_direction):
    # the old direction
    global direction_player_2

    if new_direction == 'left':
        if direction_player_2 != 'right':
            direction_player_2 = new_direction
    elif new_direction == 'right':
        if direction_player_2 != 'left':
            direction_player_2 = new_direction
    elif new_direction == 'up':
        if direction_player_2 != 'down':
            direction_player_2 = new_direction
    elif new_direction == 'down':
        if direction_player_2 != 'up':
            direction_player_2 = new_direction


def check_collisions(snake, canvas):
    #head of the snake
    x, y = snake.coordinates[0]

    global DIFFICULTY

    if (x < 0 or x >= GAME_WIDTH) or (y < 0 or y >= GAME_HEIGHT):
        if DIFFICULTY == "easy":
            teleport(snake, canvas)
            return False
        else:
            print("Game over!")
            return True

    # everything after the head of the snake
    for body_part in snake.coordinates[1:]:
        #if the head of the snake touches another part of its body
        if x == body_part[0] and y == body_part[1]:
            print("Game over!")
            return True
    return False


def teleport(snake, canvas):
    # head of the snake
    x, y = snake.coordinates[0]

    # Adjust x coordinate if out of bounds
    if x < 0:
        x = GAME_WIDTH - SPACE_SIZE
    elif x >= GAME_WIDTH:
        x = 0

    # Adjust y coordinate if out of bounds
    if y < 0:
        y = GAME_HEIGHT - SPACE_SIZE
    elif y >= GAME_HEIGHT:
        y = 0

    # Update the snake's head coordinates
    snake.coordinates[0] = (x, y)

    # Move the snake's head square to the new coordinates
    canvas.coords(snake.squares[0], x, y, x + SPACE_SIZE, y + SPACE_SIZE)


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
