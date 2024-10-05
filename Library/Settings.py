import pygame


def StartMenu():
    width=1100
    height=550
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    background_image = pygame.image.load("./Source/Img/Bck/bck1.jpeg")
    background_image = pygame.transform.scale(background_image, (width, height))
    screen.blit(background_image, (0, 0))
    pygame.display.flip()