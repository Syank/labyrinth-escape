import pygame

from src.behaviors.Drawable import Drawable


class Rectangle(Drawable):
    def __init__(self, xPosition, yPosition, width, height, color = (255, 255, 255)):
        self._xPosition = xPosition
        self._yPosition = yPosition

        self._width = width
        self._height = height

        self._color = color

    def draw(self, screenToDrawOn):
        pointSpecifications = (self._xPosition, self._yPosition, self._width, self._height)

        pygame.draw.rect(screenToDrawOn, self._color, pointSpecifications)
