"""Módulo de funciones"""

import math


def linear(x: int) -> int:
    """Función lineal"""
    return x


def sin(x: int) -> int:
    """Función seno"""
    return int(50 * math.sin(0.02 * x))


def quadratic(x: int) -> int:
    """Función cuadrática"""
    return int((0.075 * x) ** 2)
