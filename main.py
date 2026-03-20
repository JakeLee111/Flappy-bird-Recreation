import pygame
from random import randint

pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
running = True
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
RED = (255, 0 ,0)
BLACK = (0, 0 , 0)
clock = pygame.time.Clock()

TUBE_VELOCITY = 3
TUBE_WIDTH = 50
TUBE_GAP = 150

tube1_x = 600
tube2_x = 800
tube3_x = 1000

tube1_height = randint(100, 400)
tube2_height = randint(100, 400)
tube3_height = randint(100, 400)

tube1_pass = False
tube2_pass = False
tube3_pass = False

pausing = False

BIRD_X = 50
bird_y = 400
BIRD_WIDTH = 35
BIRD_HIEGHT = 35
bird_drop_velocity = 0
GRAVITY = 0.5

score = 0
font = pygame.font.SysFont("sans", 20)

background_image = pygame.image.load("background 2.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
bird_image = pygame.image.load("fqdxNT.png")
bird_image = pygame.transform.scale(bird_image, (BIRD_WIDTH, BIRD_HIEGHT))

while running:
    clock.tick(60)
    screen.fill(GREEN)
    screen.blit(background_image, (0, 0))

    # Draw tubes
    tube1_rect = pygame.draw.rect(screen, GREEN, (tube1_x, 0, TUBE_WIDTH, tube1_height))
    tube2_rect = pygame.draw.rect(screen, GREEN, (tube2_x, 0, TUBE_WIDTH, tube2_height))
    tube3_rect = pygame.draw.rect(screen, GREEN, (tube3_x, 0, TUBE_WIDTH, tube3_height))

    # Draw tubes inverse
    tube1_rect_inverse = pygame.draw.rect(screen, GREEN, (tube1_x, tube1_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - tube1_height - TUBE_GAP))
    tube2_rect_inverse = pygame.draw.rect(screen, GREEN, (tube2_x, tube2_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - tube2_height - TUBE_GAP))
    tube3_rect_inverse = pygame.draw.rect(screen, GREEN, (tube3_x, tube3_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - tube3_height - TUBE_GAP))

    # Draw top and bottom
    top = pygame.draw.rect(screen, BLUE, (0 , -49, WIDTH, 50))
    bottom = pygame.draw.rect(screen, BLUE, (0, 550, WIDTH, 50))

    # Move tubes to the left
    tube1_x = tube1_x - TUBE_VELOCITY
    tube2_x = tube2_x - TUBE_VELOCITY
    tube3_x = tube3_x - TUBE_VELOCITY

    # Draw bird
    bird_rect = screen.blit(bird_image, (BIRD_X, bird_y))

    # Bird falls
    bird_y += bird_drop_velocity
    bird_drop_velocity += GRAVITY

    # Generate new tubes
    if tube1_x < -TUBE_WIDTH:
        tube1_x = 550
        tube1_height = randint(100, 400)
        tube1_pass = False
    if tube2_x < -TUBE_WIDTH:
        tube2_x = 550
        tube2_height = randint(100, 400)
        tube2_pass = False
    if tube3_x < -TUBE_WIDTH:
        tube3_x = 550
        tube3_height = randint(100, 400)
        tube3_pass = False

    score_txt = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_txt, (5, 5))

    # Update score
    if tube1_x + TUBE_WIDTH <= BIRD_X and tube1_pass == False:
        score += 1
        tube1_pass = True
    if tube2_x + TUBE_WIDTH <= BIRD_X  and tube2_pass == False:
        score += 1
        tube2_pass = True
    if tube3_x + TUBE_WIDTH <= BIRD_X  and tube3_pass == False:
        score += 1
        tube3_pass = True

    # Check collision
    for tube in [tube1_rect, tube2_rect, tube3_rect, tube1_rect_inverse, tube2_rect_inverse, tube3_rect_inverse, top, bottom]:
        if bird_rect.colliderect(tube):
            pausing = True
            TUBE_VELOCITY = 0
            bird_drop_velocity = 0
            game_over_txt = font.render("Game over, score: " + str(score), True, BLACK)
            screen.blit(game_over_txt, (100, 250))
            press_space_txt = font.render("Press SPACE to continue", True, BLACK)
            screen.blit(press_space_txt, (100, 300))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:   
            if event.key == pygame.K_SPACE:
                # Reset
                if pausing:
                     bird_y = 400
                     TUBE_VELOCITY = 3
                     tube1_x = 600
                     tube2_x = 800
                     tube3_x = 1000
                     score = 0
                     pausing = False

                bird_drop_velocity = 0
                bird_drop_velocity -= 8


    pygame.display.flip()

pygame.quit()