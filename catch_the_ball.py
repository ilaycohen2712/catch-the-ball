
import pygame
import random

pygame.init()

window_width = 500
window_height = 500
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Catch the Ball")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

font = pygame.font.SysFont("Arial", 25)
score = 0

clock = pygame.time.Clock()

basket_width = 100
basket_height = 50
basket_x = (window_width - basket_width) / 2
basket_y = window_height - basket_height
basket_speed = 10

ball_size = 50
ball_x = random.randint(ball_size, window_width - ball_size)
ball_y = 0


game_running = True
while game_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    elif keys[pygame.K_RIGHT] and basket_x < window_width - basket_width:
        basket_x += basket_speed

    ball_y += 5
    if ball_y > window_height:
        ball_x = random.randint(ball_size, window_width - ball_size)
        ball_y = 0
        score -= 1

    if ball_y + ball_size > basket_y and ball_x > basket_x and ball_x < basket_x + basket_width:
        ball_x = random.randint(ball_size, window_width - ball_size)
        ball_y = 0
        score += 1

    game_window.fill(white)
    pygame.draw.rect(game_window, black, [
                     basket_x, basket_y, basket_width, basket_height])
    pygame.draw.circle(game_window, red, (ball_x, ball_y), ball_size)

    score_text = font.render("Score: " + str(score), True, black)
    game_window.blit(score_text, (10, 10))

    pygame.display.update()

    clock.tick(60)

pygame.quit()
