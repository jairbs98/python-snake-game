import pygame
import random
from constants import GRID_SIZE, RED, GAME_WIDTH, GAME_HEIGHT


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = (
            random.randint(0, (GAME_WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
            random.randint(0, (GAME_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE,
        )

    def draw(self, surface):
        pygame.draw.circle(
            surface,
            RED,
            (self.position[0] + GRID_SIZE // 2, self.position[1] + GRID_SIZE // 2),
            GRID_SIZE // 2,
        )
