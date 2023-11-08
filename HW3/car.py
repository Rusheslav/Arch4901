from HW3.abstract_class import Car, IFuelStation, ICarWash


class PickUp(Car, IFuelStation, ICarWash):
    load_capacity: int

    def __init__(self, brand: str, model: str, color: str, body_type: str, wheel_count: int, fuel_type: str,
                 transmission_type: str, engine_capacity: float, load_capacity: int):
        super().__init__(brand, model, color, body_type, wheel_count, fuel_type, transmission_type, engine_capacity)
        self.load_capacity = load_capacity

    @staticmethod
    def sweep_street(self):
        print("Подметаееееееем, вжух-вжух")

    def fill(self):
        print("Заправляемся")

    def weep_windshield(self):
        print("Протираем лобовое стекло")

    def weep_headlights(self):
        print("Протираем фары")

    def weep_mirror(self):
        print("Протираем зеркало")
