import random
from abc import ABC, abstractmethod
from collections import Counter


class IGameItem(ABC):
    @abstractmethod
    def open(self):
        pass


class IGameFabric(ABC):
    @abstractmethod
    def create_item(self):
        pass


class Gold(IGameItem):
    def open(self):
        print("This is gold!")


class Gem(IGameItem):
    def open(self):
        print("This is gem!")


class Silver(IGameItem):
    def open(self):
        print("This is silver!")


class Platinum(IGameItem):
    def open(self):
        print("This is platinum!")


class Diamond(IGameItem):
    def open(self):
        print("This is diamond!")


class Emerald(IGameItem):
    def open(self):
        print("This is emerald!")


class Titanium(IGameItem):
    def open(self):
        print("This is titanium!")


class GoldGeneator(IGameFabric):
    def create_item(self):
        return Gold()


class GemGeneator(IGameFabric):
    def create_item(self):
        return Gem()


class SilverGeneator(IGameFabric):
    def create_item(self):
        return Silver()


class PlatinumGeneator(IGameFabric):
    def create_item(self):
        return Platinum()


class DiamondGeneator(IGameFabric):
    def create_item(self):
        return Diamond()


class EmeraldGeneator(IGameFabric):
    def create_item(self):
        return Emerald()


class TitaniumGeneator(IGameFabric):
    def create_item(self):
        return Titanium()


if __name__ == "__main__":
    generators = [SilverGeneator()] * 10 + [PlatinumGeneator()] * 10 + [DiamondGeneator()] * 10 + [
        TitaniumGeneator()] * 10 + [EmeraldGeneator()] * 10 + [GoldGeneator()] * 3 + [GemGeneator()]

    rewards = []

    counter = Counter()

    for _ in range(1_000_000):
        rewards.append(item := random.choice(generators).create_item())
        item_name = type(item).__name__
        counter[item_name] += 1

    print(counter)
