import pygame
from constants import GAME_WIDTH, GAME_HEIGHT, BLUE, FONT_PATH, FONT_SIZE


class Level:
    def __init__(self):
        self.level = 1

    def advance(self):
        self.level += 1

    def draw(self, surface):
        level_text = pygame.font.Font(FONT_PATH, FONT_SIZE).render(
            f"Level: {self.level}", True, BLUE
        )
        surface.blit(level_text, (GAME_WIDTH - 100, 10))
