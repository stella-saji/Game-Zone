import pygame

pygame.init()

# Screen
width, height = 800, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game 🏓")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Paddle
paddle_width, paddle_height = 10, 80
player_y = height // 2 - paddle_height // 2
ai_y = height // 2 - paddle_height // 2
paddle_speed = 6

# Ball
ball_x, ball_y = width // 2, height // 2
ball_size = 10
ball_dx, ball_dy = 4, 4

clock = pygame.time.Clock()

def draw():
    screen.fill(black)

    # Player paddle
    pygame.draw.rect(screen, white, (10, player_y, paddle_width, paddle_height))

    # AI paddle
    pygame.draw.rect(screen, white, (width - 20, ai_y, paddle_width, paddle_height))

    # Ball
    pygame.draw.rect(screen, white, (ball_x, ball_y, ball_size, ball_size))

    pygame.display.update()

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= paddle_speed
    if keys[pygame.K_DOWN] and player_y < height - paddle_height:
        player_y += paddle_speed

    # Ball movement
    ball_x += ball_dx
    ball_y += ball_dy

    # Bounce top/bottom
    if ball_y <= 0 or ball_y >= height - ball_size:
        ball_dy *= -1

    # Paddle collision
    if (ball_x <= 20 and player_y < ball_y < player_y + paddle_height) or \
       (ball_x >= width - 30 and ai_y < ball_y < ai_y + paddle_height):
        ball_dx *= -1

    # Reset if out of bounds
    if ball_x < 0 or ball_x > width:
        ball_x, ball_y = width // 2, height // 2

    # Simple AI
    if ai_y + paddle_height // 2 < ball_y:
        ai_y += paddle_speed
    elif ai_y + paddle_height // 2 > ball_y:
        ai_y -= paddle_speed

    draw()

pygame.quit()
