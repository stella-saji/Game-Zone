import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game 🐍")

# Colors
white = (255, 255, 255)
green = (0, 200, 0)
red = (200, 0, 0)
black = (0, 0, 0)

# Snake settings
snake_block = 10
snake_speed = 15

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

def show_score(score):
    value = font.render(f"Score: {score}", True, white)
    screen.blit(value, [10, 10])

def game_loop():
    game_over = False
    game_close = False

    x = width // 2
    y = height // 2

    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    food_x = random.randrange(0, width - snake_block, snake_block)
    food_y = random.randrange(0, height - snake_block, snake_block)

    while not game_over:

        while game_close:
            screen.fill(black)
            msg = font.render("Game Over! Press C to Play Again or Q to Quit", True, red)
            screen.blit(msg, [50, height // 2])
            show_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        screen.fill(black)

        pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])

        snake_head = [x, y]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_list)
        show_score(snake_length - 1)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = random.randrange(0, width - snake_block, snake_block)
            food_y = random.randrange(0, height - snake_block, snake_block)
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Run game
game_loop()
