import pygame

from src.enumerations.Stages import Stages
from src.enumerations.WorldObjectsTypes import WorldObjectsTypes
from src.stages.TestStage import TestStage


class LabyrinthEscape:
    def __init__(self):
        pygame.init()

        self._screenWidth = 800
        self._screenHeight = 600
        self._isGameRunning = True
        self._frameRate = 30
        self._backgroundColor = (0, 0, 0)  # Black
        self._currentStage = Stages.TEST_STAGE.name

        self._screenProportions = (self._screenWidth, self._screenHeight)

        self._screen = pygame.display.set_mode(self._screenProportions)
        self._fps = pygame.time.Clock()

        self._worldObjects = {
            WorldObjectsTypes.PLAYER.name: None,
            WorldObjectsTypes.DRAWABLES.name: []
        }

        self._stages = {
            Stages.TEST_STAGE.name: TestStage()
        }

        self._loadStage(self._currentStage)

    def _gameLoop(self):
        while self._isGameRunning:
            self._executeUserInputs()
            self._drawFrame()

            self._fps.tick(self._frameRate)

    def _drawFrame(self):
        self._screen.fill(self._backgroundColor)

        for drawable in self._worldObjects[WorldObjectsTypes.DRAWABLES.name]:
            drawable.draw(self._screen)

        pygame.display.flip()

    def _executeUserInputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._isGameRunning = False

        pressedKeys = pygame.key.get_pressed()

        self._dispatchPressedKeyEvent(pressedKeys)

    def _dispatchPressedKeyEvent(self, pressedKeys):
        pass

    def _loadStage(self, stageName):
        self._stages[stageName].loadStage(self._worldObjects)

    def startGame(self):
        self._gameLoop()

        pygame.quit()
