# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()

#Images
diamond = pygame.image.load('img/diamond.png')
# Window
WIDTH = 960
HEIGHT = 720
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)
#Sounds
slap = pygame.mixer.Sound("sounds/slap.ogg")
pygame.mixer.music.load("sounds/diamonds.ogg")

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)


# Make a player
player1 =  [200, 150, 24, 24]
vel1 = [0, 0]
player1_speed = 4
score1 = 0

# make walls
wall1 =  [24, 24, 24, 672]
wall2 =  [48, 24, 888, 24]
wall3 =  [912, 48, 24, 647]
wall4 =  [24, 672, 912, 24]
wall5 =  [48, 72, 144, 48]
wall6 =  [48, 240, 48, 24]
wall7 =  [96, 192, 96, 72] 
wall8 =  [264, 48, 24, 120]
wall9 =  [360, 120, 48, 48]
wall10 = [360, 72, 48, 48]
wall11 = [288, 144, 72, 120]
#This one disapears by a switch
wall12 = [96, 312, 24, 48]
#-----------------------------
wall13 = [120, 312, 72, 48]
wall14 = [120, 360, 72, 48]
wall15 = [168, 408, 24, 72]
wall16 = [72, 432, 96, 48]
wall17 = [48, 456, 24, 24]
wall19 = [48, 312, 48, 96]
wall20 = [288, 336, 144, 144]
wall21 = [384, 216, 48, 120]
wall22 = [432, 216, 72, 48]
wall23 = [456, 48, 48, 92]
wall25 = [96, 552, 96, 48]
wall26 = [552, 96, 96, 48]
wall27 = [600, 72, 48, 24]
wall28 = [144, 528, 312, 48]
wall29 = [96, 624, 192, 48]


walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10,
         wall11, wall12, wall13, wall14, wall15, wall16, wall17, wall19, wall20,
         wall21, wall22, wall23, wall25, wall26, wall27, wall28, wall29]

# Make coins
coin1 = [500, 300, 25, 25]
coin2 = [400, 200, 25, 25]
coin3 = [150, 150, 25, 25]

coins = [coin1, coin2, coin3]


# Game loop
win = False
done = False
pygame.mixer.music.play(-1)

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    up = pressed[pygame.K_UP]
    down = pressed[pygame.K_DOWN]
    left = pressed[pygame.K_LEFT]
    right = pressed[pygame.K_RIGHT]

    if left:
        vel1[0] = -player1_speed
    elif right:
        vel1[0] = player1_speed
    else:
        vel1[0] = 0

    if up:
        vel1[1] = -player1_speed
    elif down:
        vel1[1] = player1_speed
    else:
        vel1[1] = 0
        
        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the player in horizontal direction '''
    player1[0] += vel1[0]

    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player1, w):        
            if vel1[0] > 0:
                player1[0] = w[0] - player1[2]
            elif vel1[0] < 0:
                player1[0] = w[0] + w[2]

    ''' move the player in vertical direction '''
    player1[1] += vel1[1]
    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(player1, w):                    
            if vel1[1] > 0:
                player1[1] = w[1] - player1[3]
            if vel1[1]< 0:
                player1[1] = w[1] + w[3]


    ''' here is where you should resolve player collisions with screen edges '''




    ''' get the coins '''
    hit_list = []

    for c in coins:
        if intersects.rect_rect(player1, c):
            hit_list.append(c)
     
    hit_list = [c for c in coins if intersects.rect_rect(player1, c)]
    
    for hit in hit_list:
        coins.remove(hit)
        score1 += 1
        slap.play()
        
    if len(coins) == 0:
        win = True

    ''' get player1 edges (makes collision resolution easier to read) '''
    left = player1[0]
    right = player1[0] + player1[2]
    top = player1[1]
    bottom = player1[1] +player1[3]

    ''' if the player1 is moved out of the window, nudge it back on. '''
    if left < 0:
        player1[0] = 0
    elif right > WIDTH:
        player1[0] = WIDTH - player1[2]

    if top < 0:
        player1[1] = 0
    elif bottom > HEIGHT:
        player1[1] = HEIGHT - player1[3]
    
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, player1)
    
    for w in walls:
        pygame.draw.rect(screen, RED, w)

    for c in coins:
        loc = c[0], c[1]
        screen.blit(diamond, loc)
        
    if win:
        font = pygame.font.Font(None, 48)
        text = font.render("You Win!", 1, GREEN)
        screen.blit(text, [400, 200])

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
