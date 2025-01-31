import pygame
from constants import WIDTH, HEIGHT, BLUE


# levels.py
class Level:
    def __init__(self):
        self.current_level = 1

    def advance(self):
        self.current_level += 1

    def draw(self, surface):
        level_text = pygame.font.SysFont("Arial", 24).render(
            f"Level: {self.current_level}", True, BLUE
        )
        surface.blit(level_text, (WIDTH - 100, 10))

    def increase_level(self):
        self.current_level += 1
        self.speed += 2

    def get_speed(self):
        return self.speed

    def get_level(self):
        return self.current_level
