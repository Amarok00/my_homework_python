from abc import ABC 
from homework_02.exceptions import LowFuelError, NotEnoughFuel



class Vehicle(ABC):
    
    def __init__(self,weight,fuel,fuel_consumption): 
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False 
    
    def start(self): 
        if not self.started: 
            if self.fuel > 0: 
                self.started = True 
            else:
                raise LowFuelError ('Falled min fuel') 
        else:
            return True 

    
    def move(self,distance): 
        fuel_need = distance * self.fuel_consumption 
        if fuel_need <= self.fuel: 
            self.fuel -= fuel_need 
        else:
            raise NotEnoughFuel('No fuel') 
