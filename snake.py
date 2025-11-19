import pygame
import random

def snake_game():
    game_over = False
    pygame.init()
    font = pygame.font.SysFont(None, 60)

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

        if game_over:
            screen.fill("black")
            msg = font.render("YOU LOST!", True, (255, 0, 0))
            screen.blit(msg, (screen_width//2 - msg.get_width()//2,
                              screen_height//2 - msg.get_height()//2))
            pygame.display.flip()
            continue
        #Refresh the page
        screen.fill("black")

        #Out of screen
        if snake_x>=screen_width:
            snake_x -= screen_width
        if snake_x<=0:
            snake_x +=screen_width
        if snake_y<=0:
            snake_y += screen_height
        if snake_y>=screen_height:
            snake_y -= screen_height

#Keyboard input
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


#update the postion of the snake's head
        snake_x += snake_vel_x
        snake_y += snake_vel_y

        #end the game
        if (snake_x, snake_y) in snake_body:
            game_over = True
            pygame.display.set_caption("You lost :(")
            screen.fill("black")
            continue

        #increase length after moving and delete the previous last part of the tail
        snake_body.append((snake_x, snake_y))
        if len(snake_body) > snake_length:
            del snake_body[0]
        
        head_rect = pygame.Rect(snake_x, snake_y, snake_width, snake_width)
        fruit_rect = pygame.Rect(fruit_x, fruit_y, snake_width, snake_width)
        if head_rect.colliderect(fruit_rect):
            snake_length += 1
            fruit_x = random.randint(0, screen_width)
            fruit_y = random.randint(0, screen_width)
        for pos in snake_body:
            px, py = pos
            pygame.draw.rect(screen, "red", (px, py, snake_width, snake_width))
        
        pygame.draw.rect(screen, "blue", (fruit_x, fruit_y,snake_width, snake_width))
        
        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    snake_game()