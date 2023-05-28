# class Car():
#     """"Создаём автомобиль"""
#     def __init__(self, model, release_year, engine_volume, price, mileage):
#         """"Инициализируем атрибуты автомобиля"""
#         self.model = model
#         self.release_year = release_year
#         self.engine_volume = engine_volume
#         self.price = price
#         self.mileage = mileage
#         self.car_wheels_num = 4
#
#     def description_car(self):
#         """"Получаем описание автомобиля"""
#         print(f'Автомобиль: {self.model}\nГод выпуска: {self.release_year} г.\nОбъем двигателя: {self.engine_volume} литра/ов\nЦена: {self.price} у.е\nПробег: {self.mileage} км\nКоличество колес: {self.car_wheels_num}\n')
#
#     def complement(self):
#         if self.price <= 30000:
#             print(f'Базовая комплектация')
#         elif self.price > 30000 and self.price < 40000:
#             print(f'Частичная комплектация')
#         else:
#             print(f'Полная комплектация')
#
# class Truck(Car):
#     """"Создаём класс Грузовик"""
#     def __init__(self, model, release_year, engine_volume, price, mileage):
#         """"Инициализируем атрибуты грузовика"""
#         super().__init__(model, release_year, engine_volume, price, mileage)
#         self.truck_wheels_num = 8
#
#     def description_truck(self):
#         """"Переопределение метода класса-родителя для грузовика"""
#         description = f'Грузовик: {self.model}\nГод выпуска: {self.release_year} г.\nОбъем двигателя: {self.engine_volume} литра/ов\nЦена: {self.price} у.е\nПробег: {self.mileage} км\nКоличество колес: {self.truck_wheels_num}\n'
#         return description
#
#
# car = Car('Volkswagen', 2022, 1.9, int(input("Введите цену авто: ")), 50532)
# truck = Truck('DAF', 2020, 12.9, int(input("Введите цену фуры: ")), 300000)
#
# car.description_car()
# car.complement()
#
# print(truck.description_truck())
# truck.complement()

class Human():
    def __init__(self, name):
        self.name = name

    def answer_question(self, question):
        print('Очень интересный вопрос! Не знаю.')

class Student(Human):
    def __init__(self, name):
        super().__init__(name)

    def ask_question(self):
        print(f'{self.name}, каким способом лучше решить задачу?')


class Mentor(Human):
    def __init__(self, name):
        super().__init__(name)

    def answer_question(self):
        print(f'Держись, всё получится. Хочешь видео с котиками?')


class CodeReviewer(Human):
    def __init__(self, name):
        super().__init__(name)

    def answer_question(self):
        print(f'Отдохни и возвращайся с вопросами по теории.')


class Curator(Human):
    def __init__(self, name):
        super().__init__(name)

    def answer_question(self):
        print(f'О, вопрос про проект, это я люблю.')

