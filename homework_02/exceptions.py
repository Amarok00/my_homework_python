class VehicleException(Exception):
    pass

class LowFuelError(VehicleException):
    pass

class NotEnoughFuel(VehicleException):
    pass

class CargoOverload(VehicleException):
    pass
