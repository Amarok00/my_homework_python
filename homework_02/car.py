"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine
# Импортируем трансорт , и двигатель 

class Car(Vehicle): # Создаем класс и наследуем класс транспорт 
    def __init__(self, weight, fuel, fuel_consumption): #инициализируем все от класса  транспорт 
        super().__init__(weight, fuel, fuel_consumption) # все от родительского класса
        
    
    def set_engine(self, engine):# создаем метод установленный двигатель 
        self.engine = engine