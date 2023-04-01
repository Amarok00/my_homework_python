"""
create dataclass `Engine`
"""
from dataclasses import dataclass

class Engine(): # Создаем класс двигатель 
    def __init__(self,volume,pistons):# Инициализируем (с параметрами объем , поршни )
        self.volume = volume 
        self.pistons = pistons

@dataclass  #Соответственно создаем датакласс
class Engine:
    volume: int
    pistons: int 