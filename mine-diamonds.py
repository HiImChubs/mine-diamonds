# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# stages
START = 0
PLAYING = 1
END = 2
WIN = 3

#Images
diamond = pygame.image.load('img/diamond.png')
wall = pygame.image.load('img/wall.png')
startscreen = pygame.image.load("img/start.jpg")
endscreen = pygame.image.load("img/end.jpg")
winscreen = pygame.image.load("img/winscreen.jpg")
# Window
WIDTH = 960
HEIGHT = 720
SIZE = (WIDTH, HEIGHT)
TITLE = "Mine Diamonds"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)
#Sounds
slap = pygame.mixer.Sound("sounds/slap.ogg")
death = pygame.mixer.Sound("sounds/death.ogg")
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

player_img = pygame.image.load("img/steve.png")
evil_img = pygame.image.load("img/creeper.png")
vel1 = [0, 0]
vel2 = [0, 0]
player1_speed = 3.5
player2_speed = 3.8
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
wall12 = [96, 312, 24, 48]
wall13 = [120, 312, 72, 48]
wall14 = [120, 360, 72, 48]
wall15 = [168, 408, 24, 72]
wall16 = [72, 432, 96, 48]
wall17 = [48, 456, 24, 24]
wall19 = [48, 312, 24, 96]
wall20 = [288, 336, 144, 144]
wall21 = [384, 216, 48, 120]
wall22 = [432, 216, 72, 48]
wall23 = [456, 48, 48, 92]
wall25 = [96, 552, 96, 48]
wall26 = [552, 96, 96, 48]
wall27 = [600, 72, 48, 24]
wall28 = [144, 528, 360, 48]
wall29 = [96, 624, 192, 24]
wall30 = [240, 600, 48, 48]
wall31 = [348, 600, 96, 48]
wall33 = [504, 528, 24, 168]
wall35 = [552, 216, 144, 48]
wall36 = [696, 96, 48, 168]
wall37 = [744, 96, 72, 48]
wall38 = [768, 48, 48, 48]
wall39 = [792, 144, 24, 72]
wall40 = [792, 216, 24, 432]
wall41 = [744, 240, 48, 24]
wall42 = [816, 504, 72, 48]
wall43 = [840, 432, 72, 48]
wall44 = [840, 624, 48, 24]
wall46 = [624, 312, 96, 48]
wall47 = [490, 312, 96, 48]
wall48 = [464, 384, 48, 48]
wall49 = [476, 456, 48, 48]
wall50 = [576, 480, 48, 48]
wall51 = [552, 384, 96, 48]
wall52 = [672, 456, 48, 48]
wall53 = [696, 384, 72, 48]
wall54 = [672, 552, 72, 48]
wall55 = [576, 600, 48, 48]


walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10,
         wall11, wall13, wall14, wall16, wall19, wall20,
         wall21, wall22, wall23, wall25, wall26, wall27, wall28, wall29, wall30,
         wall31, wall33, wall35, wall36, wall37, wall39, wall40, wall41,
         wall42, wall43, wall44, wall46, wall47, wall48, wall49, wall50, wall51,
         wall52, wall53, wall54, wall55]

# Make coins
coin1 = [48, 432, 24, 24]
coin2 = [462, 612, 24, 24]
coin3 = [852, 648, 24, 24]

coins = [coin1, coin2, coin3]

def setup():
    global stage, coins, walls, player1, player2, vel1, vel2
    vel1= [0,0]
    vel2= [0,0]
    walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10,
         wall11, wall13, wall14, wall16, wall19, wall20,
         wall21, wall22, wall23, wall25, wall26, wall27, wall28, wall29, wall30,
         wall31, wall33, wall35, wall36, wall37, wall39, wall40, wall41,
         wall42, wall43, wall44, wall46, wall47, wall48, wall49, wall50, wall51,
         wall52, wall53, wall54, wall55]
    coins = [coin1, coin2, coin3]
    pygame.mixer.music.play(-1)
    player1 =  [48, 48, 24, 24]
    player2 =  [768, 648, 24, 24]

    stage = START
    

    
# Game loop
setup()
win = False
done = False


while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:

            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
            if stage == END:
                if event.key == pygame.K_SPACE:
                    setup()
            if stage == WIN:
                if event.key == pygame.K_SPACE:
                    setup()
            if stage == WIN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if stage == END:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if stage == START:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

    pressed = pygame.key.get_pressed()

    up = pressed[pygame.K_UP]
    down = pressed[pygame.K_DOWN]
    left = pressed[pygame.K_LEFT]
    right = pressed[pygame.K_RIGHT]

    up1 = pressed[pygame.K_w]
    down1 = pressed[pygame.K_s]
    left1 = pressed[pygame.K_a]
    right1 = pressed[pygame.K_d]

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

    if left1:
        vel2[0] = -player2_speed
    elif right1:
        vel2[0] = player2_speed
    else:
        vel2[0] = 0

    if up1:
        vel2[1] = -player2_speed
    elif down1:
        vel2[1] = player2_speed
    else:
        vel2[1] = 0
        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the player in horizontal direction '''
    player1[0] += vel1[0]
    player2[0] += vel2[0]

    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player1, w):        
            if vel1[0] > 0:
                player1[0] = w[0] - player1[2]
            elif vel1[0] < 0:
                player1[0] = w[0] + w[2]
    for w in walls:
        if intersects.rect_rect(player2, w):        
            if vel2[0] > 0:
                player2[0] = w[0] - player2[2]
            elif vel2[0] < 0:
                player2[0] = w[0] + w[2]

    ''' move the player in vertical direction '''
    player1[1] += vel1[1]
    player2[1] += vel2[1]
    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(player1, w):                    
            if vel1[1] > 0:
                player1[1] = w[1] - player1[3]
            if vel1[1]< 0:
                player1[1] = w[1] + w[3]
    for w in walls:
        if intersects.rect_rect(player2, w):                    
            if vel2[1] > 0:
                player2[1] = w[1] - player2[3]
            if vel2[1]< 0:
                player2[1] = w[1] + w[3]


    ''' here is where you should resolve player collisions with screen edges '''

    ''' Player Collision'''
    hit_list = []
    if intersects.rect_rect(player1, player2):
        death.play()
        stage = END

    for hit in hit_list:
        stage = END

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
        stage = WIN

    ''' get player1 edges (makes collision resolution easier to read) '''
    left = player1[0]
    right = player1[0] + player1[2]
    top = player1[1]
    bottom = player1[1] +player1[3]
    left1 = player2[0]
    right1 = player2[0] + player2[2]
    top1 = player2[1]
    bottom1 = player2[1] + player2[3]

    ''' if the player1 is moved out of the window, nudge it back on. '''
    if left < 0:
        player1[0] = 0
    elif right > WIDTH:
        player1[0] = WIDTH - player1[2]

    if top < 0:
        player1[1] = 0
    elif bottom > HEIGHT:
        player1[1] = HEIGHT - player1[3]

    if left1 < 0:
        player2[0] = 0
    elif right1 > WIDTH:
        player2[0] = WIDTH - player2[2]

    if top1 < 0:
        player2[1] = 0
    elif bottom1 > HEIGHT:
        player2[1] = HEIGHT - player2[3]


    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    
    loc = player1[:2]
    screen.blit(player_img, loc)

    loc = player2[:2]
    screen.blit(evil_img, loc)
    
    for w in walls:
        pygame.draw.rect(screen, RED, w)
        for y in range(w[1], w[1] + w[3], 24):
            for x in range(w[0], w[0] + w[2], 24):
                loc = x, y
                screen.blit(wall, loc)

    for c in coins:
        loc = c[0], c[1]
        screen.blit(diamond, loc)
        
    if win:
        font = pygame.font.Font(None, 48)
        text = font.render("You Win!", 1, GREEN)
        screen.blit(text, [400, 200])

    ''' begin/end game text '''
    if stage == START:
        screen.blit(startscreen, (0, 0))
    elif stage == END:
        screen.blit(endscreen, (0,0))
        pygame.mixer.music.stop()
    elif stage == WIN:
        screen.blit(winscreen, (0,0))
        pygame.mixer.music.stop()
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
