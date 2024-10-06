import pygame
from Library.Settings import StartMenu
def main():
    screen = StartMenu()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
if __name__ == "__main__":
    main()

    #gestione mondi file come librerie o ...
    #ricerca ambiente (assets)
    #personaggi MAX 5+2
    #musiche


#schermata creazione gioco (save o load)-> no file new game, si file load