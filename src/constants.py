import os

# Dimensiones de la ventana
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Dimensiones del área de juego
GAME_WIDTH = 800
GAME_HEIGHT = 600

GRID_SIZE = 20
GRID_WIDTH = GAME_WIDTH // GRID_SIZE
GRID_HEIGHT = GAME_HEIGHT // GRID_SIZE

WHITE = (255, 255, 255)
GREEN = (76, 175, 80)  # Material Design Green
RED = (244, 67, 54)    # Material Design Red
BLACK = (33, 33, 33)   # Material Design Dark
BLUE = (33, 150, 243)  # Material Design Blue
GRAY = (158, 158, 158) # Material Design Gray
DARK_GRAY = (50, 50, 50) # Dark Gray for background

# Ruta a la fuente Roboto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = os.path.join(BASE_DIR, "fonts", "Roboto-Regular.ttf")

FONT_SIZE = 24

# Ruta al archivo de récords
RECORD_FILE_PATH = "high_score.txt"