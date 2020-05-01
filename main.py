import pygame
import math
import random
import time



pygame.init()

# Creat Screen Size
screen = pygame.display.set_mode((800, 600))

# Title And Icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)


ballImg = pygame.image.load('football.png')
ballX = random.randint(0, 768)
ballY = 100
ballX_change = 40
ballY_change = 5
def ball_m(x,y):
    screen.blit(ballImg, (ballX, ballY))



# Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
Num_Of_Enemies = 10
for x in range(Num_Of_Enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(10)
    enemyY_change.append(40)


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


# Background
Background = pygame.image.load('background.png')


# Bullet
BulletImg = pygame.image.load('bullet.png')
BulletX = 0
BulletY = 480
BulletX_change = 0
BulletY_change = 50
Bullet_state = "ready"


def fire_bullet(x, y):
    global Bullet_state
    Bullet_state = "fire"
    screen.blit(BulletImg, (x + 16, y + 10))
# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf",32)

textX = 10
textY = 10


# Game Over Text
Game_Over = pygame.font.Font('freesansbold.ttf',64)


def Over_text():
    Game = Game_Over.render("GAME OVER" ,True,(255, 255, 255))
    screen.blit(Game,(200,250))


def show_score(x, y):
    score = font.render("Score : " + str(score_value),True, (255, 255, 255))
    screen.blit(score, (x, y))


# Collision
def iscollision(enemyX,enemyY,BulletX,BulletY):
    distance = math.sqrt((math.pow(enemyX - BulletX,2))+(math.pow(enemyY - BulletY,2)))

    if distance < 27:
        return True
    else:
        return False

def ball_c(ballX,ballY,BulletX,BulletY):
    distance_ball = math.sqrt((math.pow(ballX - BulletX, 2)) + (math.pow(ballY - BulletY, 2)))

    if distance_ball <27:
        return True
    else:
        return False


running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(Background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            playerX_change = 15
        if event.key == pygame.K_LEFT:
            playerX_change = -15
        if event.key == pygame.K_SPACE:
            if Bullet_state is "ready":
                BulletX = playerX
                fire_bullet(BulletX, BulletY)
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
            playerX_change = 0
    if playerX >= 736:
        playerX = 736
    elif playerX <= 0:
        playerX = 0

    # Enemy Movement
    for i in range(Num_Of_Enemies):

        # Game Over
        if enemyY[i] >= 480:
            for j in range(Num_Of_Enemies):
                ballY = 2000
                enemyY[j] = 2000
            Over_text()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 14
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -14
            enemyY[i] += enemyY_change[i]

        collision = iscollision(enemyX[i], enemyY[i], BulletX, BulletY)
        if collision:
            BulletY = 480
            Bullet_state = "ready"
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)
            score_value += 1
        enemy(enemyX[i], enemyY[i], i)
        ballX += ballX_change
        if ballX <= 0:
            ballX_change = 2
            ballY += ballY_change
        elif ballX >= 736:
            ballX_change = -2
            ballY += ballY_change

        ball_col = ball_c(ballX,ballY,BulletX,BulletY)
        if ball_col:
            BulletY = 480
            Bullet_state = "ready"
            ballX = random.randint(0,768)
            ballY += 5
            score_value += 5
            ball_m(ballX,ballY)

    # Bullet Movement
    if BulletY <= 0:
        BulletY = 480
        Bullet_state = "ready"
    if Bullet_state is 'fire':
        fire_bullet(BulletX, BulletY)
        BulletY -= BulletY_change




    # 5 = 5 - 0.8
    # 5 = 5 + 0.8
    playerX += playerX_change
    ball_m(ballX,ballY)
    show_score(textX, textY)
    player(playerX, playerY)
    pygame.display.update()
