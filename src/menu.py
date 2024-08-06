import pygame
import button

def show_menu(screen):
    game_mute = False
    menu_state = "main"

    pygame.mixer.music.load("audios/highoctane.mp3")
    pygame.mixer.music.play(-1)

    background_img = pygame.image.load("assets/backgrounds/castelo.jpg")
    hellcinfe_img = pygame.image.load("assets/backgrounds/hellcinfe_logo.png")

    som_ativado = pygame.image.load("assets/assetsmenu/somativado.png")
    som_desativado = pygame.image.load("assets/assetsmenu/somdesativado.png")

    play_img = pygame.image.load("assets/assetsmenu/playbutton.png").convert_alpha()
    quit_img = pygame.image.load("assets/assetsmenu/quitbutton.png").convert_alpha()

    play_button = button.Button(430, 405, play_img, 1)
    quit_button = button.Button(430, 605, quit_img, 1)
    sound_button = button.Button(850, 600, som_ativado, 1)

    run = True
    while run:
        screen.fill((52, 78, 91))

        if menu_state == "main":
            screen.blit(background_img, (0, 0))
            screen.blit(hellcinfe_img, (340, 150))
            
            if quit_button.draw(screen):
                run = False

            if play_button.draw(screen):
                return "play"

            if sound_button.draw(screen):
                if not game_mute:
                    pygame.mixer.music.set_volume(0)
                    sound_button = button.Button(850, 600, som_desativado, 1)
                    game_mute = True
                else:
                    pygame.mixer.music.set_volume(1)
                    sound_button = button.Button(850, 600, som_ativado, 1)
                    game_mute = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    
    pygame.mixer.music.stop()
    pygame.quit()

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")
pygame.mixer.init()