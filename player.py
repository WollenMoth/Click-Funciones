"""Módulo de la clase Player"""

from typing import Callable
import pygame
from colors import WHITE
from common import Coordinate


class Player:
    """Clase Player"""

    def __init__(self, pos: Coordinate, func: Callable[[int], int]) -> None:
        """Constructor de la clase Player"""
        self.h = pos[0]
        self.k = -pos[1]
        self.func = func
        self.x = 0
        self.y = self.calc(self.x)
        self.radius = 1
        self.color = WHITE

    def draw(self, screen: pygame.Surface) -> None:
        """Dibuja el player en la pantalla"""
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def calc(self, x: int) -> int:
        """Calcula la posición del player"""
        return -(self.func(x - self.h) + self.k)

    def update(self) -> None:
        """Actualiza la posición del player"""
        self.x += 1
        self.y = self.calc(self.x)
