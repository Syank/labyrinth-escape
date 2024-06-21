import pygame.draw

from src.behaviors.Drawable import Drawable


class Point(Drawable):
    def __init__(self, xPosition, yPosition, color = (255, 255, 255)):
        self._xPosition = xPosition
        self._yPosition = yPosition

        self._width = 2
        self._height = 2

        self._color = color

    def draw(self, screenToDrawOn):
        pointSpecifications = (self._xPosition, self._yPosition, self._width, self._height)

        pygame.draw.rect(screenToDrawOn, self._color, pointSpecifications)
