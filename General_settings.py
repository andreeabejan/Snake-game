
class Generals:
    GAME_WIDTH = None
    GAME_HEIGHT = None
    SPEED = None
    SPACE_SIZE = None
    BODY_PARTS = None
    SNAKE_COLOR = None
    FOOD_COLOR = None
    BACKGROUND_COLOR = None

    def __init__(self):
        self.GAME_WIDTH = 900
        self.GAME_HEIGHT = 400
        self.SPEED = 50
        self.SPACE_SIZE = 20
        self.BODY_PARTS = 3
        self.SNAKE_COLOR = "pink"
        self.FOOD_COLOR = "red"
        self.BACKGROUND_COLOR = "#000000"
    def reset(self, width, height, speed, space_size, body_parts, snake_color, food_color, background_color):
        self.GAME_WIDTH = width
        self.GAME_HEIGHT = height
        self.SPEED = speed
        self.SPACE_SIZE = space_size
        self.BODY_PARTS = body_parts
        self.SNAKE_COLOR = snake_color
        self.FOOD_COLOR = food_color
        self.BACKGROUND_COLOR = background_color
