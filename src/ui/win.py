import ui.button as button
from settings import *
import pygame
import sys

fonte = pygame.font.SysFont('arial', 40, True, True)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
restart_button = button.Button(300, 420, derrota_button_img, 1)
quit_button = button.Button(300, 500, quit_derrota_img, 1)


def show_win():
    screen.blit(WIN_SCREEN, (0, 0))

    mensage_win = "VOCÊ VENCEU!"
    win_format = fonte.render(mensage_win, False, (255, 255, 255))

    if restart_button.draw(screen):
        return "restart"

    if quit_button.draw(screen):
        pygame.quit()
        sys.exit()
