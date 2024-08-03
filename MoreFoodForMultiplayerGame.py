from tkinter import *
import random
from General_settings import *

#not used yet
class MoreFoodForMultiplayerGame:
    def __init__(self, canvas, general):
        #food object is placed randomly
        x = random.randint(2, int(general.GAME_WIDTH / general.SPACE_SIZE) - 2) * general.SPACE_SIZE
        y = random.randint(2, int(general.GAME_HEIGHT / general.SPACE_SIZE) - 2) * general.SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + general.SPACE_SIZE, y + general.SPACE_SIZE, fill="#00FF00", tag="morefood")
