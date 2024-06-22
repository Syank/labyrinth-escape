from src.behaviors.Stage import Stage
from src.enumerations.WorldObjectsTypes import WorldObjectsTypes
from src.objects.Player import Player
from src.objects.Point import Point


class TestStage(Stage):
    def __init__(self):
        pass

    def loadStage(self, worldObjects):
        player = Player(200, 200, 50, 50)
        point1 = Point(100, 100)

        worldObjects[WorldObjectsTypes.PLAYER.name] = player

        worldObjects[WorldObjectsTypes.DRAWABLES.name].append(point1)
        worldObjects[WorldObjectsTypes.DRAWABLES.name].append(player)

        worldObjects[WorldObjectsTypes.KEY_LISTENERS.name].append(player)
