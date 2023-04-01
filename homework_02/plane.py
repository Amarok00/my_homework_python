"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import  CargoOverload

class Plane(Vehicle): # Создаем класс самолет и наследуем от транспорта 
    def __init__(self, weight, fuel, fuel_consumption,max_cargo):
        super().__init__(weight, fuel, fuel_consumption) # Наследуемся от родительского класса 
        self.cargo = 0 # добавляем атрибут груз которая изначально равна 0 
        self.max_cargo = max_cargo # И атрибут максимальный груз
    
    def load_cargo(self,load_cargo):  # Создаем метод загрузка груза 
        if self.cargo + load_cargo <= self.max_cargo: # Если груз + загрузочный груз будет меньше макс.груза
            self.cargo += load_cargo # То груз плюсуем  с загрузкой груза 
        else:
            raise CargoOverload # Иначе исключение 
        
    def remove_all_cargo(self): # Метод разгрузка всего груза 
        cargo_before = self.cargo # присваем груз до и груз сейчас 
        self.cargo = 0 # присваиваем груз = 0 , а так как до = грузу соответсвенно он становится 0
        return cargo_before # и возращаем бефор т.к. он равен 0 
