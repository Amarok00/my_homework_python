from abc import ABC 
from homework_02.exceptions import LowFuelError, NotEnoughFuel



class Vehicle(ABC):#Создаем класс транспорт с параметром АБС
    
    def __init__(self,weight,fuel,fuel_consumption): # Инициализируем класс (с параметрами по умлч.)
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False #Здесь ставим стартед на фалс т.к. машина не заведённая

    
    def start(self): # метод старт 
        if not self.started: # Если НЕ старт то
            if self.fuel > 0: # Если бензин больше 0
                self.started = True # возращается тру ( иначе заведена)
            else:
                raise LowFuelError ('Falled min fuel') # Если бенза мало то исключение LowFuelError
        else:
            return True # А если заведена то сразу возвращаем тру 

    
    def move(self,distance): #Создаем метод движение ( с параметром дистанция )
        fuel_need = distance * self.fuel_consumption # получаем сколько нам нужно бенза = дист*расход
        if fuel_need <= self.fuel: # Создаем условие если бенза_надо меньше чем у нас 
            self.fuel -= fuel_need # То убавляем наш бенз (вычитаем из нашего -  бенз на движение )
        else:
            raise NotEnoughFuel('No fuel') # Ну и когда закончится то возвращаем исключение 
