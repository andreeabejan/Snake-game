from tkinter import *
import random
from General_settings import *

class SpecialFood:
    def __init__(self, canvas, general):

        x = random.randint(0, int(general.GAME_WIDTH / general.SPACE_SIZE) - 1) * general.SPACE_SIZE
        y = random.randint(0, int(general.GAME_HEIGHT / general.SPACE_SIZE) - 1) * general.SPACE_SIZE

        self.coordinates = [x,y]

        canvas.create_arc(x,y,
                          x + general.SPACE_SIZE,
                          y + general.SPACE_SIZE,
                          fill="#FFD700", #GOLD
                          tag="specialfood")
