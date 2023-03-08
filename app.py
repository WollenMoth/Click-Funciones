"""Dibujar diferentes funciones con origen en la posición del mouse"""

import pygame
from colors import BLACK
from functions import linear, sin, quadratic
from player import Player

WIDTH, HEIGHT = 800, 600

FPS = 60

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Click - Funciones")


def draw(player: Player) -> None:
    """Dibuja todos los elementos en la pantalla"""
    player.draw(screen)

    pygame.display.flip()


def main() -> None:
    """Función principal del juego"""
    running = True

    clock = pygame.time.Clock()

    player = Player((0, 0), linear)

    while running:
        while running:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break

            left, middle, right = pygame.mouse.get_pressed()
            pos = pygame.mouse.get_pos()

            if left:
                player = Player(pos, linear)
            elif middle:
                player = Player(pos, sin)
            elif right:
                player = Player(pos, quadratic)

            if any((left, middle, right)):
                break

        screen.fill(BLACK)

        while player.x <= WIDTH:
            draw(player)
            player.update()

    pygame.quit()


if __name__ == "__main__":
    main()
