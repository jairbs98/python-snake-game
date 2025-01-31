import pygame

from constants import GRID_SIZE, GREEN, WIDTH, HEIGHT


class Snake:
    def __init__(self):
        self.segments = [(100, 100), (80, 100), (60, 100)]
        self.direction = (1, 0)
        self.grow_next = False

    def move(self):
        head_x, head_y = self.segments[0]
        dx, dy = self.direction
        new_head = (
            (head_x + dx * GRID_SIZE) % WIDTH,
            (head_y + dy * GRID_SIZE) % HEIGHT,
        )
        self.segments.insert(0, new_head)
        if self.grow_next:
            self.grow_next = False
        else:
            self.segments.pop()

    def grow(self):
        self.grow_next = True

    def check_collision(self):
        return self.segments[0] in self.segments[1:]

    def draw(self, surface):
        for segment in self.segments:
            pygame.draw.rect(surface, GREEN, (*segment, GRID_SIZE, GRID_SIZE))
