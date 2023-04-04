from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, load_cargo):
        if self.cargo + load_cargo > self.max_cargo:
            raise CargoOverload
        self.cargo += load_cargo


    def remove_all_cargo(self):
        cargo_before = self.cargo
        self.cargo = 0
        return cargo_before
