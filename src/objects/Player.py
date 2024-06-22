import pygame

from src.behaviors.Drawable import Drawable
from src.behaviors.KeyListener import KeyListener


class Player(KeyListener, Drawable):
    def __init__(self, xPosition: int, yPosition: int, width: int, height: int, color = (255, 255, 255)):
        self._xPosition = xPosition
        self._yPosition = yPosition

        self._width = width
        self._height = height

        self._color = color

        self._moveSpeed = 3

    def onKeyPressed(self, pressedKeys):
        if pressedKeys[pygame.K_w]:
            self._yPosition -= self._moveSpeed
        if pressedKeys[pygame.K_s]:
            self._yPosition += self._moveSpeed
        if pressedKeys[pygame.K_a]:
            self._xPosition -= self._moveSpeed
        if pressedKeys[pygame.K_d]:
            self._xPosition += self._moveSpeed

    def draw(self, screenToDrawOn):
        pointSpecifications = (self._xPosition, self._yPosition, self._width, self._height)

        pygame.draw.rect(screenToDrawOn, self._color, pointSpecifications)
