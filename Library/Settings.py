import pygame
import sys

def StartMenu():
    width, height = 1100, 550
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Menu")
    background_image = pygame.image.load("./Source/Img/Bck/bck1.jpeg")
    background_image = pygame.transform.scale(background_image, (width, height))

    # Colori
    button_color = (0, 0, 0)  # Nero per l'interno del bottone
    border_color = (255, 255, 255)  # Bianco per il bordo
    hover_color = (255, 223, 0)  # Giallo sacro/mistico per l'evidenziazione
    text_color = (255, 255, 255)  # Colore del testo
    title_color = (240, 255, 255)  # Nero per il testo del titolo
    title_border_color = (0,0,0)  # Bianco per il bordo del titolo

    # Font per il testo
    font = pygame.font.Font("./Source/Font/Dialoghi.ttf", 35)
    title_font = pygame.font.Font("./Source/Font/Titolo.ttf", 70)  # Font per il titolo

    button_width, button_height = 225, 75
    button_x = (width - button_width) // 2
    button_y_start = (height - (3 * button_height + 40)) // 2  # Spaziatura tra i bottoni

    # Crea i rettangoli dei bottoni
    play_button_rect = pygame.Rect(button_x, button_y_start, button_width, button_height)
    settings_button_rect = pygame.Rect(button_x, button_y_start + button_height + 20, button_width, button_height)
    exit_button_rect = pygame.Rect(button_x, button_y_start + 2 * (button_height + 20), button_width, button_height)

    # Funzione per disegnare i bottoni con bordo bianco e interno nero
    def draw_button(rect, text, hover=False):
        # Disegna il bordo (bianco)
        pygame.draw.rect(screen, hover_color if hover else border_color, rect)
        # Riduci il rettangolo per disegnare l'interno (nero)
        inner_rect = rect.inflate(-6, -6)  # Riduce il rettangolo di 6 pixel per creare il bordo
        pygame.draw.rect(screen, button_color, inner_rect)

        # Disegna il testo centrato
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect)

    # Funzione per disegnare il titolo con bordo
    def draw_title(text):
        # Disegna il contorno del titolo (bianco)
        title_surface_border = title_font.render(text, True, title_border_color)
        title_rect_border = title_surface_border.get_rect(center=(width // 2, height // 5.5))
        screen.blit(title_surface_border, title_rect_border)

        # Disegna il titolo (nero) sopra il contorno
        title_surface = title_font.render(text, True, title_color)
        title_rect = title_surface.get_rect(center=(width // 2, height // 6))
        screen.blit(title_surface, title_rect)

    # Loop principale
    while True:
        screen.blit(background_image, (0, 0))  # Disegna lo sfondo

        # Disegna il titolo "Haki"
        draw_title("Haki's Adventure")

        mouse_pos = pygame.mouse.get_pos()  # Posizione del mouse

        # Disegna i bottoni con hover effect
        draw_button(play_button_rect, "Play", play_button_rect.collidepoint(mouse_pos))
        draw_button(settings_button_rect, "Settings", settings_button_rect.collidepoint(mouse_pos))
        draw_button(exit_button_rect, "Exit", exit_button_rect.collidepoint(mouse_pos))

        # Gestisci eventi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(mouse_pos):
                    print("Play button clicked")
                    # Inserisci qui la funzione che vuoi eseguire per il bottone "Play"
                elif settings_button_rect.collidepoint(mouse_pos):
                    print("Settings button clicked")
                    # Inserisci qui la funzione che vuoi eseguire per il bottone "Settings"
                elif exit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
StartMenu()