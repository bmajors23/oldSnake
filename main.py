import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Snake")
icon = pygame.image.load("../newSnake/001-snake.png")
pygame.display.set_icon(icon)

enemyImg = pygame.image.load("001-square.png")
enemyImg = pygame.transform.scale(enemyImg, (10, 10))
enemyX = random.randint(2, 78) * 10
enemyY = random.randint(2, 58) * 10

playerImg = pygame.image.load("001-black-square.png")
playerImg = pygame.transform.scale(playerImg, (10, 10))
playerX = 390
playerY = 280
playerX_change = 0
playerY_change = 0

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

Length_of_snake = 0
tailX_change = 0
tailY_change = 0




def player(x, y):
    screen.blit(playerImg, (x, y))


def tail(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))


running = True
while running:

    clockobject = pygame.time.Clock()
    clockobject.tick(30)
    screen.fill((200, 200, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                playerY_change = -10
                playerX_change = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                playerY_change = +10
                playerX_change = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -10
                playerY_change = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                playerX_change = +10
                playerY_change = 0

    playerX += playerX_change
    if playerX <= -1:
        playerX = 800
    if playerX >= 801:
        playerX = 0

    playerY += playerY_change
    if playerY <= -1:
        playerY = 600
    if playerY >= 601:
        playerY = 0

    tailX = playerX - playerX_change
    tailY = playerY - playerY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    show_score(textX, textY)

    if Length_of_snake >= 1:
        tail(tailX - tailX_change, tailY - tailY_change)
    if Length_of_snake >= 2:
        tail(tailX - tailX_change, tailY - tailY_change)
    if Length_of_snake >= 3:
        tail(tailX - tailX_change, tailY - tailY_change)
    if Length_of_snake >= 4:
        tail(tailX - tailX_change, tailY - tailY_change)
    if Length_of_snake >= 5:
        tail(tailX - tailX_change, tailY - tailY_change)
    if Length_of_snake >= 6:
        tail(tailX - tailX_change, tailY - tailY_change)
    if Length_of_snake >= 7:
        tail(tailX - tailX_change, tailY - tailY_change)
    if Length_of_snake >= 8:
        tail(tailX - tailX_change, tailY - tailY_change)
    if Length_of_snake >= 9:
        tail(tailX - tailX_change, tailY - tailY_change)



    if playerX == enemyX and playerY == enemyY:
        enemyX = random.randint(2, 78) * 10
        enemyY = random.randint(2, 58) * 10
        score_value += 1
        Length_of_snake += 1

    print(tailX_change)


    pygame.display.update()
