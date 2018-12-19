import pygame
def home_page(name):
    background = pygame.image.load("image/background.png").convert()
    background = pygame.transform.scale(background, (400, 600))
    name.blit(background, (0, 0))