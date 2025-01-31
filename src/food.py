import pygame
import random
from constants import GRID_SIZE, RED, WIDTH, HEIGHT


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = (
            random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
            random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE,
        )

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (*self.position, GRID_SIZE, GRID_SIZE))
