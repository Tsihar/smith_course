class Car():
    """"Создаём автомобиль"""
    def __init__(self, model, release_year, engine_volume, price, mileage):
        """"Инициализируем атрибуты автомобиля"""
        self.model = model
        self.release_year = release_year
        self.engine_volume = engine_volume
        self.price = price
        self.mileage = mileage
        self.car_wheels_num = 4

    def description_car(self):
        """"Получаем описание автомобиля"""
        print(f'Автомобиль: {self.model}\nГод выпуска: {self.release_year} г.\nОбъем двигателя: {self.engine_volume} литра/ов\nЦена: {self.price} у.е\nПробег: {self.mileage} км\nКоличество колес: {self.car_wheels_num}\n')

class Truck(Car):
    """"Создаём класс Грузовик"""
    def __init__(self, model, release_year, engine_volume, price, mileage):
        """"Инициализируем атрибуты грузовика"""
        super().__init__(model, release_year, engine_volume, price, mileage)
        self.truck_wheels_num = 8

    def description_truck(self):
        """"Переопределение метода класса-родителя для грузовика"""
        description = f'Грузовик: {self.model}\nГод выпуска: {self.release_year} г.\nОбъем двигателя: {self.engine_volume} литра/ов\nЦена: {self.price} у.е\nПробег: {self.mileage} км\nКоличество колес: {self.truck_wheels_num}\n'
        return description


car = Car('Volkswagen', 2022, 1.9, 15000, 50532)
truck = Truck('DAF', 2020, 12.9, 50000, 300000)

car.description_car()
print(truck.description_truck())



