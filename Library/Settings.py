import pygame
import sys

# Funzione per gestire il menu delle impostazioni
def Settings(screen, width, height, font, button_color, border_color, text_color, hover_color):
    # Dimensioni e posizione del rettangolo (più largo e più alto)
    rect_width, rect_height = 400, 450  # Rettangolo delle impostazioni
    rect_x = (width - rect_width) // 2

    # Rettangolo sotto la scritta "Haki's Adventure" (esempio: posizionato a 25% dell'altezza)
    rect_y = int(height * 0.25)
    settings_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

    # Disegna il bordo
    pygame.draw.rect(screen, border_color, settings_rect)
    inner_settings_rect = settings_rect.inflate(-6, -6)  # Riduci per creare bordo
    pygame.draw.rect(screen, button_color, inner_settings_rect)

    # Crea un rettangolo trasparente
    transparent_surface = pygame.Surface((rect_width - 6, rect_height - 6), pygame.SRCALPHA)  # Crea una superficie trasparente
    transparent_surface.fill((0, 0, 0, 128))  # Imposta il colore con alpha (0-255), 128 per 50% di trasparenza

    # Disegna il rettangolo trasparente sopra
    screen.blit(transparent_surface, (rect_x + 3, rect_y + 3))  # Offset di 3 px per allineare il bordo

    # Posiziona il testo "Settings" appena sotto il bordo superiore del rettangolo
    text_surface = font.render("Settings", True, text_color)
    text_rect = text_surface.get_rect(center=(rect_x + rect_width // 2, rect_y + 40))  # Offset di 40 px dal bordo superiore
    screen.blit(text_surface, text_rect)

    # Crea il bottone "BACK"
    back_button_width, back_button_height = 200, 60
    back_button_x = (width - back_button_width) // 2
    back_button_y = rect_y + rect_height - 80  # Posiziona il bottone 80 px sopra il fondo del rettangolo
    back_button_rect = pygame.Rect(back_button_x, back_button_y, back_button_width, back_button_height)

    # Disegna il bottone "BACK"
    draw_button(screen, back_button_rect, "BACK", font, button_color, border_color, text_color, hover_color)

    return back_button_rect  # Restituisci il rettangolo del bottone BACK

# Funzione per disegnare i bottoni con bordo bianco e interno nero
def draw_button(screen, rect, text, font, button_color, border_color, text_color, hover_color, hover=False):
    # Disegna il bordo (bianco)
    pygame.draw.rect(screen, hover_color if hover else border_color, rect)
    # Riduci il rettangolo per disegnare l'interno (nero)
    inner_rect = rect.inflate(-6, -6)  # Riduce il rettangolo di 6 pixel per creare il bordo
    pygame.draw.rect(screen, button_color, inner_rect)

    # Disegna il testo centrato
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

# Funzione per gestire il menu principale
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
    title_color = (240, 255, 255)  # Colore per il testo del titolo
    title_border_color = (0, 0, 0)  # Colore del bordo del titolo

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

    # Variabile di stato
    current_state = "menu"  # "menu" for main menu, "settings" for settings screen

    # Funzione per disegnare il titolo con bordo
    def draw_title(text):
        # Disegna il contorno del titolo
        title_surface_border = title_font.render(text, True, title_border_color)
        title_rect_border = title_surface_border.get_rect(center=(width // 2, height // 5.5))
        screen.blit(title_surface_border, title_rect_border)

        # Disegna il titolo sopra il contorno
        title_surface = title_font.render(text, True, title_color)
        title_rect = title_surface.get_rect(center=(width // 2, height // 6))
        screen.blit(title_surface, title_rect)

    # Loop principale
    while True:
        screen.blit(background_image, (0, 0))  # Disegna lo sfondo
        mouse_pos = pygame.mouse.get_pos()  # Posizione del mouse

        # Disegna il titolo (sempre visibile)
        draw_title("Haki's Adventure")

        # Disegna la schermata in base allo stato
        if current_state == "menu":
            # Disegna i bottoni del menu principale con hover effect
            draw_button(screen, play_button_rect, "Play", font, button_color, border_color, text_color, hover_color, play_button_rect.collidepoint(mouse_pos))
            draw_button(screen, settings_button_rect, "Settings", font, button_color, border_color, text_color, hover_color, settings_button_rect.collidepoint(mouse_pos))
            draw_button(screen, exit_button_rect, "Exit", font, button_color, border_color, text_color, hover_color, exit_button_rect.collidepoint(mouse_pos))

        elif current_state == "settings":
            # Usa la funzione Settings() per gestire la schermata delle impostazioni
            back_button_rect = Settings(screen, width, height, font, button_color, border_color, text_color, hover_color)

        # Gestisci eventi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if current_state == "menu":
                    if play_button_rect.collidepoint(mouse_pos):
                        print("Play button clicked")
                        # Inserisci qui la funzione che vuoi eseguire per il bottone "Play"
                    elif settings_button_rect.collidepoint(mouse_pos):
                        print("Settings button clicked")
                        current_state = "settings"  # Cambia stato al menu delle impostazioni
                    elif exit_button_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()
                elif current_state == "settings":
                    # Controlla se il bottone BACK è stato cliccato
                    if back_button_rect.collidepoint(mouse_pos):
                        current_state = "menu"  # Torna al menu principale

        pygame.display.update()

# Avvia il menu principale
StartMenu()