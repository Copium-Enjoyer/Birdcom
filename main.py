# Example file showing a basic pygame "game loop"
import pygame
import sys
import os

classes = ["Ranger", "Specialist", "Sniper", "Bruiser", "Hunter"]
nations = ["French", "Polish", "German", "American", "Australian"]
personalities = ["Timid", "Brave", "Calm", "Cautious", "Obsessive"]
# these are indexes for looping through the lists above
i, j, k = 0, 0, 0 
picture_index = 0

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# ["welcome", "trait_picker", "game", "the_end"]
scene = "welcome"
base_x = 128
base_y = 64
vec = 364

class Player():

    def __init__(self, nationality, personality, game_class, picture):
        self.nationality = nationality
        self.personality = personality
        self.game_class = game_class
        self.picture = picture

        # respawn position
        self.x = 1280/2
        self.y = 720/2

    # method to print out the state of our player
    def __str__(self) -> str:
        return f"{self.nationality} {self.personality} {self.game_class} on position {self.x}, {self.y}"

    def shoot(self):
        print(f"{self.nationality} {self.personality} {self.game_class} has shot!")
        


class Enemy():
    pass

def welcome_scene():
    screen.fill("black")
    font = pygame.font.SysFont(None, 54)
    img = font.render(f'Hello', True, "blue")
    screen.blit(img, (base_x + (vec) + (300/2)-150, base_y+(500/2)))
    font = pygame.font.SysFont(None, 38)
    img = font.render(f'Press any key to continue', True, "blue")
    screen.blit(img, (base_x + (vec) + (300/2)-150, base_y+(500/2) + 38 + 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            btn=pygame.mouse
            print ("x = {}, y = {}".format(pos[0], pos[1]))
        if event.type == pygame.KEYDOWN:
            global scene
            scene = "trait_picker"
                
            

def trait_picker_scene():
    global i, j, k, picture_index
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # pygame.draw.rect(screen, "black", [base_x, base_y, 300, 500], 4)
    pygame.draw.rect(screen, "black", [base_x + (vec), base_y, 300, 500], 4)
    # pygame.draw.rect(screen, "black", [base_x + 2*(vec), base_y, 300, 500], 4)
    # pygame.draw.line(screen, "red", [640, 0], [640, 720], 1)
    
    spacing = 18
    y_vec = 50

    
    pictures = os.listdir(r"img\birds\100")
    # render the profile picture of a character
    imp = pygame.image.load(rf"img\birds\100\{pictures[picture_index]}").convert_alpha()
    screen.blit(imp, (base_x + (vec) + (300/2) - 50, base_y+(500/2) + y_vec - 150))

    # render fonts for the customization of a character
    font = pygame.font.SysFont(None, 24)
    img = font.render(f'Nationality:  {nations[i]}', True, "blue")
    screen.blit(img, (base_x + (vec) + (300/2)-100, base_y+(500/2) + y_vec))

    font = pygame.font.SysFont(None, 24)
    img = font.render(f'Personality: {personalities[j]}', True, "blue")
    screen.blit(img, (base_x + (vec) + (300/2)-100, base_y+(500/2) + (spacing)+ y_vec))

    font = pygame.font.SysFont(None, 24)
    img = font.render('Class:' + 13*" " + f'{classes[k]}', True, "blue")
    screen.blit(img, (base_x + (vec) + (300/2)-100, base_y+(500/2) + (spacing*2) + y_vec ))
    
    # render buttons for the customization
    button_vec = 90

    # plus
    font = pygame.font.SysFont(None, 24)
    img = font.render(f'[+]', True, "black")
    screen.blit(img, (base_x + (vec) + (300/2) + button_vec, base_y+(500/2) + y_vec))

    font = pygame.font.SysFont(None, 24)
    img = font.render(f'[+]', True, "black")
    screen.blit(img, (base_x + (vec) + (300/2) + button_vec, base_y+(500/2) + (spacing) + y_vec ))
    
    font = pygame.font.SysFont(None, 24)
    img = font.render(f'[+]', True, "black")
    screen.blit(img, (base_x + (vec) + (300/2) + button_vec, base_y+(500/2) + (spacing*2) + y_vec ))


    font = pygame.font.SysFont(None, 50)
    img = font.render(f'PRESS SPACE TO START', True, "blue")
    screen.blit(img, (base_x + (vec) + (300/2)- 200, base_y+(500/2) + y_vec + 250))
    font = pygame.font.SysFont(None, 25)
    img = font.render(f'W, A, S, D to move, arrow keys to shoot', True, "blue")
    screen.blit(img, (base_x + (vec) + (300/2)- 160, base_y+(500/2) + y_vec + 285))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            btn=pygame.mouse
            print ("x = {}, y = {}".format(pos[0], pos[1]))
            # if position is going to be in area of buttons we'll change the values
            # i - class, j - nationality, k - personality
            if 750 >= pos[0] >= 725 and 375 >= pos[1] >= 355:
                i += 1
                if i > 4:
                    i = 0
                picture_index += 1
                if picture_index > len(pictures)-1:
                    picture_index = 0
                
            if 750 >= pos[0] >= 725 and 396 >= pos[1] >= 380:
                j += 1
                if j > 4:
                    j = 0
                picture_index += 1
                if picture_index > len(pictures)-1:
                    picture_index = 0
            if 750 >= pos[0] >= 725 and 415 >= pos[1] >= 400:
                k += 1
                if k > 4:
                    k = 0
                picture_index += 1
                if picture_index > len(pictures)-1:
                    picture_index = 0
            imp = pygame.image.load(rf"img\birds\100\{pictures[picture_index]}").convert_alpha()
            screen.blit(imp, (base_x + (vec) + (300/2) - 50, base_y+(500/2) + y_vec - 150))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                global scene, player
                player = Player(nations[i], personalities[j], classes[k], pictures[picture_index])
                # print(player)
                scene = "game"
                
                # create the player object
                # change the scene

            

                





while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    screen.fill(0)

    if scene == "welcome":
        welcome_scene()
    if scene == "trait_picker":
        trait_picker_scene()
    if scene == "game":
        print(player)
        
    


            


    # flip() the display to put your work on screen
    pygame.display.flip()

    # ticks can be changed in order to have more responsive interface
    clock.tick(60)  # limits FPS to 60

pygame.quit()