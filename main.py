# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    base_x = 128
    base_y = 64
    vec = 364
    pygame.draw.rect(screen, "black", [base_x, base_y, 300, 500], 4)
    pygame.draw.rect(screen, "black", [base_x + (vec), base_y, 300, 500], 4)
    pygame.draw.rect(screen, "black", [base_x + 2*(vec), base_y, 300, 500], 4)
    pygame.draw.line(screen, "red", [640, 0], [640, 720], 1)


    if pygame.mouse.get_pressed():
        menu_option_vec = 18

        font = pygame.font.SysFont(None, 24)
        img = font.render(f'Nationality: Polish', True, "blue")
        screen.blit(img, (base_x + (vec) + (300/2)-72, base_y+(500/2)))

        font = pygame.font.SysFont(None, 24)
        img = font.render(f'Personality: Timid', True, "blue")
        screen.blit(img, (base_x + (vec) + (300/2)-72, base_y+(500/2) + (menu_option_vec)))

        font = pygame.font.SysFont(None, 24)
        img = font.render(f'Class: Ranger', True, "blue")
        screen.blit(img, (base_x + (vec) + (300/2)-72, base_y+(500/2) + (menu_option_vec*2)))
        # pygame.draw.rect(screen, "black", [base_x, base_y, 300, 500], 4)
    

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()