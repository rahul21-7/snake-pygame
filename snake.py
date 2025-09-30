import pygame
import random
pygame.init()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

snake_x = 100
snake_y = 100
snake_vel = 5

snake_length = 1
snake_width = 20
snake_vel_x = snake_vel
snake_vel_y = 0
fruit_x, fruit_y = random.randint(1, screen_width), random.randint(1, screen_width)

snake_body = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    screen.fill("black")
    # snake_length += snake_vel
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        snake_vel_y = -snake_vel
        snake_vel_x = 0
    elif keys[pygame.K_DOWN]:
        snake_vel_y = snake_vel
        snake_vel_x = 0
    elif keys[pygame.K_RIGHT]:
        snake_vel_x = snake_vel
        snake_vel_y = 0
    elif keys[pygame.K_LEFT]:
        snake_vel_x = -snake_vel
        snake_vel_y = 0

    snake_x += snake_vel_x
    snake_y += snake_vel_y

    snake_body.append((snake_x, snake_y))
    if len(snake_body) > snake_length:
        del snake_body[0]
    
    head_rect = pygame.Rect(snake_x, snake_y, snake_width, snake_width)
    fruit_rect = pygame.Rect(fruit_x, fruit_y, snake_width, snake_width)
    for pos in snake_body:
        if head_rect.colliderect(fruit_rect):
            snake_length += 1
            fruit_x = random.randint(0, screen_width)
            fruit_y = random.randint(0, screen_width)
        px, py = pos
        pygame.draw.rect(screen, "red", (px, py, snake_width, snake_width))
    
    pygame.draw.rect(screen, "blue", (fruit_x, fruit_y,snake_width, snake_width))
    
    pygame.display.flip()

    clock.tick(60)