from abc import ABC, abstractmethod


class Stage(ABC):
    @abstractmethod
    def loadStage(self, worldObjects):
        pass