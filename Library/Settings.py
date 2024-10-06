import pygame
import sys
from Library.manager import SettingsManager

# Funzione per gestire il menu delle impostazioni
def Settings(screen, width, height, font, button_color, border_color, text_color, hover_color):
    # Crea un'istanza di SettingsManager
    settings_manager = SettingsManager('./Log/general.xml')
    current_resolution = settings_manager.get_current_resolution()
    current_master_volume = settings_manager.get_current_master_volume()
    current_effects_volume = settings_manager.get_current_effects_volume()

    # Dimensioni e posizione del rettangolo (più largo e più alto)
    rect_width, rect_height = 400, 450  # Rettangolo delle impostazioni
    rect_x = (width - rect_width) // 2
    rect_y = int(height * 0.25)
    settings_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

    # Disegna il bordo
    pygame.draw.rect(screen, border_color, settings_rect)
    inner_settings_rect = settings_rect.inflate(-6, -6)  # Riduci per creare bordo
    pygame.draw.rect(screen, button_color, inner_settings_rect)

    # Crea un rettangolo trasparente
    transparent_surface = pygame.Surface((rect_width - 6, rect_height - 6), pygame.SRCALPHA)
    transparent_surface.fill((0, 0, 0, 128))
    screen.blit(transparent_surface, (rect_x + 3, rect_y + 3))

    # Posiziona il testo "Settings" appena sotto il bordo superiore del rettangolo
    text_surface = font.render("Settings", True, text_color)
    text_rect = text_surface.get_rect(center=(rect_x + rect_width // 2, rect_y + 40))
    screen.blit(text_surface, text_rect)

    # Lista delle risoluzioni disponibili
    resolutions = [
        "1100x1150",
        "1920x1080",
        "1280x720",
        "1366x768",
        "2560x1440",
        "3840x2160"
    ]
    current_resolution_index = resolutions.index(current_resolution)

    # Variabile per il volume master e gli effetti
    master_volume = current_master_volume
    effects_volume = current_effects_volume

    # Funzione per disegnare i bottoni
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

    # Loop principale per il menu delle impostazioni
    while True:
        # Aggiorna lo schermo
        screen.blit(transparent_surface, (rect_x + 3, rect_y + 3))

        # Disegna le impostazioni
        resolution_text_surface = font.render(f"Resolution: {resolutions[current_resolution_index]}", True, text_color)
        screen.blit(resolution_text_surface, (rect_x + 20, rect_y + 100))
        master_volume_text_surface = font.render(f"Master Volume: {master_volume}%", True, text_color)
        effects_volume_text_surface = font.render(f"Effects Volume: {effects_volume}%", True, text_color)
        screen.blit(master_volume_text_surface, (rect_x + 20, rect_y + 150))
        screen.blit(effects_volume_text_surface, (rect_x + 20, rect_y + 200))

        # Disegna il bottone "BACK"
        back_button_width, back_button_height = 200, 60
        back_button_x = (width - back_button_width) // 2
        back_button_y = rect_y + rect_height - 80
        back_button_rect = pygame.Rect(back_button_x, back_button_y, back_button_width, back_button_height)
        draw_button(back_button_rect, "BACK", back_button_rect.collidepoint(pygame.mouse.get_pos()))

        # Gestisci eventi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(pygame.mouse.get_pos()):
                    # Torna al menu principale
                    settings_manager.update_master_volume(master_volume)
                    settings_manager.update_effects_volume(effects_volume)
                    settings_manager.update_resolution(resolutions[current_resolution_index])
                    return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:  # Freccia su per aumentare il volume master
                    master_volume = min(master_volume + 10, 100)
                elif event.key == pygame.K_DOWN:  # Freccia giù per diminuire il volume master
                    master_volume = max(master_volume - 10, 0)
                elif event.key == pygame.K_LEFT:  # Freccia sinistra per diminuire la risoluzione
                    current_resolution_index = (current_resolution_index - 1) % len(resolutions)
                elif event.key == pygame.K_RIGHT:  # Freccia destra per aumentare la risoluzione
                    current_resolution_index = (current_resolution_index + 1) % len(resolutions)

        pygame.display.update()

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

    # Funzione per disegnare i bottoni
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

    # Loop principale
    while True:
        screen.blit(background_image, (0, 0))  # Disegna lo sfondo
        mouse_pos = pygame.mouse.get_pos()  # Posizione del mouse

        # Disegna il titolo (sempre visibile)
        draw_title("Haki's Adventure")

        # Disegna la schermata in base allo stato
        if current_state == "menu":
            # Disegna i bottoni del menu principale con hover effect
            draw_button(play_button_rect, "Play", play_button_rect.collidepoint(mouse_pos))
            draw_button(settings_button_rect, "Settings", settings_button_rect.collidepoint(mouse_pos))
            draw_button(exit_button_rect, "Exit", exit_button_rect.collidepoint(mouse_pos))

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

