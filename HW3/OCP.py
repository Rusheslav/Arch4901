from abc import ABC


class ISpeedCalculation(ABC):

    def calculate_allowed_speed(self):
        pass


class Vehicle:
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def get_max_speed(self):
        return self.max_speed

    def get_type(self):
        pass


class Car(Vehicle, ISpeedCalculation):
    def __init__(self, max_speed, type, brand):
        super().__init__(max_speed, type)
        self.brand = brand

    def calculate_allowed_speed(self):
        return 0.8 * self.max_speed

    def get_type(self):
        return "Car"


class Bus(Vehicle, ISpeedCalculation):
    def __init__(self, max_speed, brand, seats_count):
        super().__init__(max_speed, type)
        self.brand = brand
        self.seats_count = seats_count

    def calculate_allowed_speed(self):
        return 0.6 * self.max_speed

    def get_type(self):
        return "Bus"
