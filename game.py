#module imports
import pygame, sys, time, pygame.mixer
from pygame import *
pygame.init()

black = 0,0,0

character = pygame.image.load("run1.png")

protobg = pygame.image.load("background.jpg")
bg = pygame.transform.scale(protobg, (1000, 650))

size = width, height = 1000, 650
screen = pygame.display.set_mode(size)


clock = pygame.time.Clock()
sound = pygame.mixer.Sound("sound.wav")


x = 0
y = 0


#gets mouse position
mx, my = pygame.mouse.get_pos()
        
while True:
    for event in pygame.event.get():
        #if pygame exits - whole program exit
        if event.type == pygame.QUIT:
            sys.exit
        #mouse button pressed - play sound
        elif event.type == pygame.MOUSEBUTTONDOWN:
            sound.play()
            mx, my = pygame.mouse.get_pos()
        #print hello when space is hit
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print("hello")

    #sets fps at 60 fps
    clock.tick(60)
    screen.blit(bg, (0,0))
    screen.blit(character, (mx, my))
    pygame.display.flip()
    
