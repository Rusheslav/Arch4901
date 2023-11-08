from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def start(self):
        pass


class Car:
    def __init__(self, engine: Engine):
        self.engine = engine

    def start(self):
        self.engine.start()


class PetrolEngine(Engine):
    def start(self):
        pass
