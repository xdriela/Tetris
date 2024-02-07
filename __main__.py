import pygame

pygame.init() # initialises pygame (always have this before doing anything pygame releated)
screen = pygame.display.set_mode((800,400)) # requires a tuple (2 arguments)

while True:
    
    pygame.display.flip() # tell pygame to refresh display