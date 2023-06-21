# Example file showing a basic pygame "game loop"
import pygame
import sys
import os
import random
import math

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


shots, enemies = [], []
last = 0
last_spawn = 0
score = 0
result = "not_decided"

# ["welcome", "trait_picker", "game", "the_end"]
scene = "welcome"
base_x = 128
base_y = 64
vec = 364

class Player():

    def __init__(self, nationality, personality, game_class, picture) -> None:
        self.nationality = nationality
        self.personality = personality
        self.game_class = game_class
        self.picture = picture

        # respawn position
        self.x = 1280/2
        self.y = 720/2
        self.speed = 5

        self.hitbox = 100

    # method to print out the state of our player
    def __str__(self) -> str:
        return f"{self.nationality} {self.personality} {self.game_class} on position {self.x}, {self.y}"

    def shoot(self):
        print(f"{self.nationality} {self.personality} {self.game_class} has shot!")
        

class Shot():

    shot_pictures = os.listdir(r"img\shots")

    def __init__(self, x, y, direction) -> None:
        self.x = x
        self.y = y
        self.direction = direction
        self.picture = random.choice(Shot.shot_pictures)
        self.picture_path = rf"img\shots\{self.picture}"
        self.velocity = 10

        self.hitbox = 48

        self.update_trajectory()
    
    def update_trajectory(self):
        
        if self.direction == "up":
            self.y -= self.velocity
        if self.direction == "down":
            self.y += self.velocity
        if self.direction == "left":
            self.x -= self.velocity
        if self.direction == "right":
            self.x += self.velocity

        self.draw()
        
        

        
        
    def draw(self):
        imp = pygame.image.load(self.picture_path).convert_alpha()
        screen.blit(imp, (self.x, self.y))


class Enemy():

    enemy_pictures = os.listdir(r"img\enemies")
    
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.picture = random.choice(Enemy.enemy_pictures)
        self.picture_path = rf"img\enemies\{self.picture}"
        self.speed = 4
        self.hitbox = 100

        self.update_position()

    def update_position(self):
        
        self.direction = random.choice(["up", "down", "left", "right"])

        if self.direction == "up":
            self.y -= self.speed
        if self.direction == "down":
            self.y += self.speed
        if self.direction == "left":
            self.x -= self.speed
        if self.direction == "right":
            self.x += self.speed

        self.draw()

    def draw(self):
        imp = pygame.image.load(self.picture_path).convert_alpha()
        screen.blit(imp, (self.x, self.y))

    


def welcome_scene():

    bg = pygame.image.load(r"img\backgrounds\Background_0.png")
    screen.blit(bg, (0, 0))
    
    font_color = (64, 44, 222)

    font = pygame.font.SysFont(None, 54)
    img = font.render(f'Hello', True, font_color)
    screen.blit(img, (base_x + (vec) + (300/2)-150, base_y+(500/2)))
    font = pygame.font.SysFont(None, 38)
    img = font.render(f'Press any key to continue', True, font_color)
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

    font_color = (131, 169, 110)
    
    pictures = os.listdir(r"img\birds\100")
    # render the profile picture of a character
    imp = pygame.image.load(rf"img\birds\100\{pictures[picture_index]}").convert_alpha()
    screen.blit(imp, (base_x + (vec) + (300/2) - 50, base_y+(500/2) + y_vec - 150))

    # render fonts for the customization of a character
    font = pygame.font.SysFont(None, 24)
    img = font.render(f'Nationality:  {nations[i]}', True, font_color)
    screen.blit(img, (base_x + (vec) + (300/2)-100, base_y+(500/2) + y_vec))

    font = pygame.font.SysFont(None, 24)
    img = font.render(f'Personality: {personalities[j]}', True, font_color)
    screen.blit(img, (base_x + (vec) + (300/2)-100, base_y+(500/2) + (spacing)+ y_vec))

    font = pygame.font.SysFont(None, 24)
    img = font.render('Class:' + 13*" " + f'{classes[k]}', True, font_color)
    screen.blit(img, (base_x + (vec) + (300/2)-100, base_y+(500/2) + (spacing*2) + y_vec ))
    
    # render buttons for the customization
    button_vec = 90

    # plus
    font = pygame.font.SysFont(None, 24)
    img = font.render(f'[+]', True, font_color)
    screen.blit(img, (base_x + (vec) + (300/2) + button_vec, base_y+(500/2) + y_vec))

    font = pygame.font.SysFont(None, 24)
    img = font.render(f'[+]', True, font_color)
    screen.blit(img, (base_x + (vec) + (300/2) + button_vec, base_y+(500/2) + (spacing) + y_vec ))
    
    font = pygame.font.SysFont(None, 24)
    img = font.render(f'[+]', True, font_color)
    screen.blit(img, (base_x + (vec) + (300/2) + button_vec, base_y+(500/2) + (spacing*2) + y_vec ))


    font = pygame.font.SysFont(None, 50)
    img = font.render(f'PRESS SPACE TO START', True, font_color)
    screen.blit(img, (base_x + (vec) + (300/2)- 200, base_y+(500/2) + y_vec + 250))
    font = pygame.font.SysFont(None, 25)
    img = font.render(f'W, A, S, D to move, arrow keys to shoot', True, font_color)
    screen.blit(img, (base_x + (vec) + (300/2)- 160, base_y+(500/2) + y_vec + 285))
    font = pygame.font.SysFont(None, 25)
    img = font.render(f'Kill 50 insects', True, font_color)
    screen.blit(img, (base_x + (vec) + (300/2)- 70, base_y+(500/2) + y_vec + 315))



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




def game_scene():
    global shots, last, last_spawn, enemies
    
    # set background
    bg = pygame.image.load(r"img\backgrounds\Background_1.png")
    screen.blit(bg, (0, 0))
    
    

    # spawn player
    imp = pygame.image.load(rf"img\birds\100\{player.picture}").convert_alpha()
    screen.blit(imp, (player.x, player.y))

    # spawn enemies
    enemy_spawn_cooldown = 1000*random.uniform(0.3, 0.9)
    now = pygame.time.get_ticks()
    if now - last_spawn >= enemy_spawn_cooldown:

        spawn_x, spawn_y = random.randint(0, 1200), random.randint(0, 720)

        # this will make sure that enemies do not spawn on us
        while math.dist([player.x, player.y], [spawn_x, spawn_y]) < 200:
            spawn_x, spawn_y = random.randint(0, 1200), random.randint(0, 720)
        
        enemies.append(Enemy(spawn_x, spawn_y))
        last_spawn = pygame.time.get_ticks()



    # player input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            btn=pygame.mouse
            # print ("x = {}, y = {}".format(pos[0], pos[1]))

    keys = pygame.key.get_pressed()

    # 180 ticks need to pass in order to shoot again
    shooting_cooldown = 180
    now = pygame.time.get_ticks()
    if now - last >= shooting_cooldown:

        if keys[pygame.K_LEFT]:
            shots.append(Shot(player.x, player.y, "left"))
            last = pygame.time.get_ticks()
        if keys[pygame.K_RIGHT]:
            shots.append(Shot(player.x, player.y, "right"))
            last = pygame.time.get_ticks()
        if keys[pygame.K_UP]:
            shots.append(Shot(player.x, player.y, "up"))
            last = pygame.time.get_ticks()
        if keys[pygame.K_DOWN]:
            shots.append(Shot(player.x, player.y, "down"))
            last = pygame.time.get_ticks()


    if keys[pygame.K_a]:
        player.x -= player.speed
    if keys[pygame.K_d]:
        player.x += player.speed
    if keys[pygame.K_w]:
        player.y -= player.speed
    if keys[pygame.K_s]:
        player.y += player.speed
            
    
def the_end():
    global enemies, shots, result, screen
    shots, enemies = [], []

    screen.fill(0)
    
    font = pygame.font.SysFont(None, 30)
    # bg = pygame.image.load(r"img\backgrounds\Background_1.png")
    # screen.blit(bg, (0, 0))
    


    if result == "win":
        img = font.render(f'Great job, {player}!', True, "white")
        screen.blit(img, (base_x + (vec) + (300/2)-300, base_y+(500/2) + 38 + 10))
        img = font.render(f'You have slain 50 enemies and freed yourself!', True, "white")
        screen.blit(img, (base_x + (vec) + (300/2)-300, base_y+(500/2) + 38 + 10 + 60))
        
        
    if result == "loss":

        img = font.render(f'Unfortunately, {player}!', True, "white")
        screen.blit(img, (base_x + (vec) + (300/2)-300, base_y+(500/2) + 38 + 10))
        img = font.render(f'You have lost against the insects, try again next time.', True, "white")
        screen.blit(img, (base_x + (vec) + (300/2)-300, base_y+(500/2) + 38 + 10 + 60))
        

    



# main loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    screen.fill(0)

    if scene == "welcome":
        welcome_scene()
    if scene == "trait_picker":
        trait_picker_scene()
    if scene == "game":
        # print(player)
        game_scene()
    
        if shots:
            for shot in shots:
                shot.update_trajectory()
                if enemies:
                    for enemy in enemies:
                        if enemy.x + enemy.hitbox > shot.x > enemy.x and enemy.y + enemy.hitbox > shot.y > enemy.y:
                            score += 1
                            # print(f"{player} has slain the enemy! {100 - score} left to escape!")
                            enemies.remove(enemy)
                            del enemy

                if not (1280 >= shot.x >= 0 and 720 >= shot.y >= 0):
                    # this line removes the shot from the shots list
                    shots.remove(shot)

                    # this should remove the shot from the program
                    del shot
                    # print(shots)
                
        if enemies:
            for enemy in enemies:
                enemy.update_position()

                if enemy.x + enemy.hitbox >= player.x >= enemy.x and enemy.y + enemy.hitbox >= player.y >= enemy.y:
                    scene = "the_end"
                    result = "loss"
                    the_end()
                    


                if not (1280 >= enemy.x >= 0 and 720 >= enemy.y >= 0):
                    enemies.remove(enemy)
                    del enemy

                    # print(enemies)

        font = pygame.font.SysFont(None, 30)            
        img = font.render(f'Score: {score}', True, "white")
        screen.blit(img, (20, 20))

        if score == 50:
            scene = "the_end"
            result = "win"
            the_end()
            
    if scene == "the_end":
        the_end()
            
    
        
    


    # flip() the display to put your work on screen
    pygame.display.update()
    pygame.display.flip()


    # print(pygame.time.get_ticks())

    # ticks can be changed in order to have more responsive interface
    clock.tick(256)  # limits FPS to 60

pygame.quit()