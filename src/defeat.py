from settings import *
import button
import sys
from menu import show_menu

fonte = pygame.font.SysFont('arial', 40, True, True)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
restart_derrota_button = button.Button(300, 420, derrota_button_img, 1)
quit_derrota_button = button.Button(300, 500, quit_derrota_img, 1)

def show_defeat():
    screen.blit(derrota_img, (0, 0))

    mensage_defeat = "VOCÊ PERDEU!"
    defeat_format = fonte.render(mensage_defeat, False, (255, 255, 255))
    
    if restart_derrota_button.draw(screen):
        pass
    
    if quit_derrota_button.draw(screen):
        pygame.quit()
        sys.exit()