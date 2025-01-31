import pygame
import os
from constants import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    GAME_WIDTH,
    GAME_HEIGHT,
    WHITE,
    BLUE,
    BLACK,
    FONT_PATH,
    FONT_SIZE,
    RECORD_FILE_PATH,
    GRAY,
    DARK_GRAY,
    GRID_SIZE,
    GREEN,
    RED,
)
from snake import Snake
from food import Food
from levels import Level


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(FONT_PATH, FONT_SIZE)
        self.running = True
        self.playing = False
        self.high_score = 0
        self.high_score_name = ""
        self.load_high_score()

    def load_high_score(self):
        if os.path.exists(RECORD_FILE_PATH):
            with open(RECORD_FILE_PATH, "r") as file:
                data = file.read().split(",")
                if len(data) == 2:
                    self.high_score_name, self.high_score = data[0], int(data[1])

    def save_high_score(self):
        with open(RECORD_FILE_PATH, "w") as file:
            file.write(f"{self.high_score_name},{self.high_score}")

    def run(self):
        while self.running:
            self.show_menu()
            if self.playing:
                self.reset_game()
                self.game_loop()

        pygame.quit()

    def reset_game(self):
        self.snake = Snake()
        self.food = Food()
        self.level = Level()
        self.score = 0

    def game_loop(self):
        while self.playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.playing = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.snake.direction != (0, 1):
                        self.snake.direction = (0, -1)
                    elif event.key == pygame.K_DOWN and self.snake.direction != (0, -1):
                        self.snake.direction = (0, 1)
                    elif event.key == pygame.K_LEFT and self.snake.direction != (1, 0):
                        self.snake.direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT and self.snake.direction != (
                        -1,
                        0,
                    ):
                        self.snake.direction = (1, 0)

            self.snake.move()

            if self.snake.segments[0] == self.food.position:
                self.snake.grow()
                self.food.randomize_position()
                self.score += 10
                if self.score % 50 == 0:
                    self.level.advance()

            if self.snake.check_collision() or self.snake.segments[0] == (-1, -1):
                self.playing = False
                if self.score > self.high_score:
                    self.high_score = self.score
                    self.high_score_name = self.get_player_name()
                    self.save_high_score()

            self.screen.fill(DARK_GRAY)
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            self.level.draw(self.screen)
            self.draw_score()
            pygame.display.flip()
            self.clock.tick(10)

    def show_menu(self):
        menu_running = True
        while menu_running:
            self.screen.fill(DARK_GRAY)
            menu_text = self.font.render(
                "Game Over! Press Enter to Restart or Esc to Quit", True, WHITE
            )
            self.screen.blit(
                menu_text,
                (
                    WINDOW_WIDTH // 2 - menu_text.get_width() // 2,
                    WINDOW_HEIGHT // 2 - menu_text.get_height() // 2,
                ),
            )
            high_score_text = self.font.render(
                f"High Score: {self.high_score_name} - {self.high_score}", True, WHITE
            )
            self.screen.blit(
                high_score_text,
                (
                    WINDOW_WIDTH // 2 - high_score_text.get_width() // 2,
                    WINDOW_HEIGHT // 2 - high_score_text.get_height() // 2 + 50,
                ),
            )
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    menu_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.playing = True
                        menu_running = False
                    elif event.key == pygame.K_ESCAPE:
                        self.running = False
                        menu_running = False

    def get_player_name(self):
        name = ""
        input_active = True
        while input_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    input_active = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        name += event.unicode

            self.screen.fill(DARK_GRAY)
            prompt_text = self.font.render("Enter your name: " + name, True, WHITE)
            self.screen.blit(
                prompt_text,
                (
                    WINDOW_WIDTH // 2 - prompt_text.get_width() // 2,
                    WINDOW_HEIGHT // 2 - prompt_text.get_height() // 2,
                ),
            )
            pygame.display.flip()

        return name

    def draw_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
