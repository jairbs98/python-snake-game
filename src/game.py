import pygame
from constants import WIDTH, HEIGHT, WHITE, BLUE, BLACK, FONT_PATH, FONT_SIZE
from snake import Snake
from food import Food
from levels import Level


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(FONT_PATH, FONT_SIZE)
        self.running = True
        self.playing = False

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
                    elif event.key == pygame.K_RIGHT and self.snake.direction != (-1, 0):
                        self.snake.direction = (1, 0)

            self.snake.move()

            if self.snake.segments[0] == self.food.position:
                self.snake.grow()
                self.food.randomize_position()
                self.score += 10
                if self.score % 50 == 0:
                    self.level.advance()

            if self.snake.check_collision():
                self.playing = False

            self.screen.fill(BLACK)
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            self.level.draw(self.screen)
            self.draw_score()
            pygame.display.flip()
            self.clock.tick(10)

    def show_menu(self):
        menu_running = True
        while menu_running:
            self.screen.fill(BLACK)
            menu_text = self.font.render(
                "Game Over! Press Enter to Restart or Esc to Quit", True, WHITE
            )
            self.screen.blit(
                menu_text,
                (
                    WIDTH // 2 - menu_text.get_width() // 2,
                    HEIGHT // 2 - menu_text.get_height() // 2,
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

    def draw_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
