import pygame

pygame.init()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

snake_length = 1
snake_width = 1


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    screen.fill("purple")
    snake_length += 1

    snake_surface = pygame.surface.Surface((snake_length, snake_width))
    snake_surface.blit(screen, (50, 50))

    pygame.display.flip()

    clock.tick(60)