from abc import ABC, abstractmethod


class Car:
    brand: str
    model: str
    color: str
    body_type: str
    wheel_count: int
    fuel_type: str
    transmission_type: str
    engine_capacity: float

    def __init__(self, brand: str, model: str, color: str, body_type: str, wheel_count: int, fuel_type: str,
                 transmission_type: str, engine_capacity: float):
        self.engine_capacity = engine_capacity
        self.transmission_type = transmission_type
        self.fuel_type = fuel_type
        self.wheel_count = wheel_count
        self.body_type = body_type
        self.color = color
        self.model = model
        self.brand = brand

    def move(self):
        pass

    def maintenance(self):
        pass

    def gear_shifting(self):
        pass

    def turn_lights_on(self):
        pass

    def turn_wipers_on(self):
        pass


class IFuelStation(ABC):
    @abstractmethod
    def fill(self):
        pass


class ICarWash(ABC):
    @abstractmethod
    def weep_windshield(self):
        pass

    @abstractmethod
    def weep_headlights(self):
        pass

    @abstractmethod
    def weep_mirror(self):
        pass
