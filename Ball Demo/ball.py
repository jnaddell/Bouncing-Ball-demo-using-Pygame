import os, sys
import pygame
from pygame.locals import *




speed = [1,1]


screen = pygame.display.set_mode((800,600))



ball = pygame.image.load("ball.jpg")
ballrect = ball.get_rect()


pygame.time.Clock(40)


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > 800:
		speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > 600:
		speed[1] = -speed[1] 
	screen.blit(ball, ballrect)
	pygame.display.flip()
	