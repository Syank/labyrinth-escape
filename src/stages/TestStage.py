from src.behaviors.Stage import Stage
from src.enumerations.WorldObjectsTypes import WorldObjectsTypes
from src.objects.Point import Point


class TestStage(Stage):
    def __init__(self):
        pass

    def loadStage(self, worldObjects):
        point1 = Point(100, 100)

        worldObjects[WorldObjectsTypes.DRAWABLES.name].append(point1)
