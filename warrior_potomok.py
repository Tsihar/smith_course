# обратимся из другого модуля(warrior_potomok) к классу-потомку

# from base_per import Warrior
#
# warrior = Warrior("Конан", 32, 200) # экземпляр необходимо тоже в другой модуль переносить иначе даст ошибку
# print(f'Нового воина зовут: {warrior.description_person()}')

#6 Можем хранить класс-потомок в отдельном модуле (родитель в одном модуле, а к прим, все потомки в другом)
from base_per import Person

class Warrior(Person):
    """"Создаём класс воина"""
    def __init__(self, name, age, height):
        """"Инициализируем атрибуты класса родителя"""
        super().__init__(name, age, height)
        self.rage = 100

    def get_rage(self):
        """"Получение заряда ярости воина"""
        print("Заряд ярости равен: " + str(self.rage))

    def description_person(self):
        """"Переопределение метода родителя"""
        description = f'{self.name}. {self.age} лет. {self.rage} ярости.' # осталось 2 старых атрибута и добавился один новый, кот есть только у класса-потомка
    #     print(f'Нового воина зовут: {description}')
        return description