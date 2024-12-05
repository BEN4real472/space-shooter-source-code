import pygame
import sys
import math
from random import randint
from pygame import mixer

from pygame.constants import K_LEFT, KEYDOWN
pygame.init()

screen = pygame.display.set_mode((800,600))



font = pygame.font.Font("font/GameOfSquids.ttf" , 25)
fontX = 10
fontY = 10

bullet_state = None


def showHiScore():  
      fileo = open("highscore.txt" )
      hiscore_value = fileo.readline()
      hiscore = font.render("High-Score : " + str(hiscore_value) , True , (255,255,255))
      screen.blit(hiscore , (500,10))
 
def showScore(x,y,score_value):
     score = font.render("Score : " + str(score_value), True , (255,255,255))
     screen.blit(score , (x,y))
 
 
def isCollision(enemyX , enemyY , bulletX , bulletY):
     dist = math.sqrt(math.pow((enemyX - bulletX),2) + math.pow((bulletY - enemyY),2))
     if dist<35:
         return True
     else:
         return False
 
def player(x,y,playerImg):
     screen.blit(playerImg , (x, y))
 
def bullet():
      global bullet_state
      bullet_state = "fire"
     #  screen.blit(bulletImg , (x, y))
  
def enemy(x,y,enemyImg):
     screen.blit(enemyImg , (x, y))
 



pygame.display.set_caption("Space Shooter Game")
    
icon = pygame.image.load("images/logo.jpg")

pygame.display.set_icon(icon)


def main():
    global bullet_state
        
    mixer.music.load("music/background.wav")
    mixer.music.play(1000)  #-1 for infinte playing of the song
    
    
    over = False
    score_value = 0
    fileo = open("highscore.txt" )
    hiscore_value = fileo.readline()
    
    
    backgroundImg = pygame.image.load("images/background.png")
    backgroundX = 0
    backgroundY = 0
    
    
    playerImg = pygame.image.load("images/player.png")
    playerX = 370
    playerY = 500  
    playerX_change = 0
    
    
    ii=0
    j=0

    
    
    bulletImg = pygame.image.load("images/bullet.png") 
    bulletX = 0
    bulletY = 500
    bulletY_change = 10
    bullet_state = "ready"
    
    
    enemyImg = []
    enemyImg.append(pygame.image.load("enemy/1.png"))
    enemyImg.append(pygame.image.load("enemy/1.png"))
    enemyImg.append(pygame.image.load("enemy/3.png"))
    enemyImg.append(pygame.image.load("enemy/4.png"))
    enemyImg.append(pygame.image.load("enemy/2.png"))
    enemyImg.append(pygame.image.load("enemy/3.png"))
    enemyImg.append(pygame.image.load("enemy/2.png"))
    enemyImg.append(pygame.image.load("enemy/4.png"))
    
    enemyX = []
    enemyY = []
    enemyX_change = []
    enemyY_change = []
    number_of_enemies = 8
    for i in range(number_of_enemies):
            enemyX.append(randint(0,720))
            enemyY.append(randint(10,150))
            enemyX_change.append(2)
            enemyY_change.append(0)
    
    
    blastImg = pygame.image.load("images/blast.png")
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_LEFT:
                      playerX_change = -4
                if event.key == pygame.K_RIGHT:
                     playerX_change = 4
                if event.key == pygame.K_SPACE:
                    if bullet_state is "ready":
                      bullet_sound = mixer.Sound("music/laser.wav")
                      bullet_sound.play()
                      bulletX = playerX - 5
                      bullet()
            if event.type == pygame.MOUSEBUTTONDOWN:
                       pos = pygame.mouse.get_pos()
                    #    print(replayImg.get_rect().collidepoint(pos))
                       if (pos[0]>330 and pos[0]<422) and (pos[1]>340 and pos[1]<372):
                           return 
                    
            if event.type == pygame.KEYUP:
                    if event.key == K_LEFT or event.key == pygame.K_RIGHT:
                        playerX_change = 0
              
    
        screen.blit(backgroundImg , (0, 0))
        
        # print(playerX)
          
        if bullet_state is "fire":
            screen.blit(bulletImg , (bulletX , bulletY))
            bulletY -= bulletY_change
            if bulletY == 0:
                bullet_state = "ready"
                bulletY = 500
                i =0