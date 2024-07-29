from tkinter import *
import random
from General_settings import *

class Snake:

    def __init__(self, canvas, general):

        self.body_size = general.BODY_PARTS

        self.coordinates = []

        self.squares = []

        for i in range(0,general.BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x +
                                             general.SPACE_SIZE,
                                             y + general.SPACE_SIZE,
                                             fill=general.SNAKE_COLOR,
                                             tag="snake")
            self.squares.append(square)

