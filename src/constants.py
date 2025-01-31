import os

WIDTH = 800
HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

WHITE = (255, 255, 255)
GREEN = (76, 175, 80)  # Material Design Green
RED = (244, 67, 54)  # Material Design Red
BLACK = (33, 33, 33)  # Material Design Dark
BLUE = (33, 150, 243)  # Material Design Blue

# Ruta a la fuente Roboto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = os.path.join(BASE_DIR, "fonts", "Roboto-Regular.ttf")
FONT_SIZE = 24
