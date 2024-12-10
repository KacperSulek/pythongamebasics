import pygame
import random
import time

snakeSpeed = 15

screenX = 720
screenY = 480

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()

screen = pygame.display.set_mode((screenX, screenY))

fps = pygame.time.Clock()


snakePos = [100, 50]

snakeBody = [
            [100, 50],
            [90, 50],
            [80, 50],
            [70, 50],
            ]

fruitPos = [
            random.randrange(1, (screenX//10)) * 10,
            random.randrange(1, (screenY//10)) * 10
            ]

fruitSpawn = True

dir = "Right"
changeDir = dir

score = 0

def showScore(choice, color, font, size):
    scoreFont = pygame.font.SysFont(font, size)

    scoreSurface = scoreFont.render("Score : " + str(score), True, color)

    scoreRect = scoreSurface.get_rect()

    screen.blit(scoreSurface, scoreRect)

def gameOver():

    myFont = pygame.font.SysFont("times new roman", 50)

    gameOverSurface = myFont.render("Your Score is : " + str(score), True, red)

    gameOverRect = gameOverSurface.get_rect()

    gameOverRect.midtop = (screenX/2, screenY/4)

    screen.blit(gameOverSurface, gameOverRect)
    
    pygame.display.flip()

    time.sleep(2)

    pygame.quit()

    quit()

while True:
    for event in pygame.event.get():
        if(event.type == pygame.KEYDOWN):
            if event.key == pygame.K_w:
                changeDir = "Up"
            if event.key == pygame.K_s:
                changeDir = "Down"
            if event.key == pygame.K_a:
                changeDir = "Left"
            if event.key == pygame.K_d:
                changeDir = "Right"
    
    if(changeDir == "Up" and dir != "Down"):
        dir = "Up"
    if(changeDir == "Down" and dir != "Up"):
        dir = "Down"
    if(changeDir == "Left" and dir != "Right"):
        dir = "Left"
    if(changeDir == "Right" and dir != "Left"):
        dir = "Right"

    if(dir == "Up"):
        snakePos[1] -= 10
    if(dir == "Down"):
        snakePos[1] += 10
    if(dir == "Left"):
        snakePos[0] -= 10
    if(dir == "Right"):
        snakePos[0] += 10
    
    snakeBody.insert(0, list(snakePos))
    if(snakePos[0] == fruitPos[0] and snakePos[1] == fruitPos[1]):
        score += 10
        fruitSpawn = False
    else:
        snakeBody.pop()

    if(not fruitSpawn):
        fruitPos = [
                    random.randrange(1, (screenX//10)) * 10,
                    random.randrange(1, (screenY//10)) * 10
                    ]

    fruitSpawn = True

    screen.fill(black)

    for pos in snakeBody:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(screen, white, pygame.Rect(fruitPos[0], fruitPos[1], 10, 10))

    if(snakePos[0] < 0 or snakePos[0] > score-10):
        gameOver()
    if(snakePos[1] < 0 or snakePos[1] > score-10):
        gameOver()

    for block in snakeBody[1:]:
        if(snakePos[0] == block[0] and snakePos[1] == block[1]):
            gameOver()

    showScore(1, white, "time new roman", 20)

    pygame.display.update()

    fps.tick(snakeSpeed)