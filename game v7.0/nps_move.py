import pygame
pygame.init()

screen = pygame.display.set_mode((900, 500))

pygame.display.set_caption('Wondering')

x_np = 0
y_np = 0
np_place = 0

npsWalkRight = [pygame.image.load('nps0.png'),
                pygame.image.load('nps1.png')]

npsStay = [pygame.image.load('nps2.png')]


npsWalkLeft = [pygame.image.load('nps3.png'),
               pygame.image.load('nps4.png')]

animCout = 0
def move():
    
    
