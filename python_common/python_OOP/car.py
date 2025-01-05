class Car:
    """Класс по созданию и работе с машинами"""

    def __init__(self, model, year, engine_capacity, price, mileage, wheels_number = 4):
        self.model = model
        self.year = year    
        self.engine_capacity = engine_capacity    
        self.price = price    
        self.mileage = mileage
        self.wheels_number = wheels_number
        print('Машина создана')


toshiba = Car('Toshiba', 2010, 1.8, 5000000, 100000)

class Truck(Car):
    """Машины для перевозки груза - грузовики"""
    def __init__(self, model, year, engine_capacity, price, mileage, wheels_number = 8):
        super().__init__(model, year, engine_capacity, price, mileage, wheels_number)
        print('Грузовик создан')

    def description(self):
        """Получение описания грузовика"""
        return f'Модель грузовика - {self.model}, год выпуска - {self.year}г., объем двигателя - {self.engine_capacity} л., цена - {self.price} руб., пробег {self.mileage} км, кол-во колес {self.wheels_number} шт.'  

scania = Truck('Scania', 2015, 3.7, 6000000, 100000)
print(scania.description())         