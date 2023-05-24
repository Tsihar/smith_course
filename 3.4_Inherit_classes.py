# Наследование классов - это процесс когда один класс наследует атрибуты и методы другого класса
# у кого наследуют - родитель, суперкласс или предок
# который наследует свойства родиетльского класса - потомок или подкласс
# вместо того, чтобы создавать класс с нуля можно обратится к существующему

class Person():
    """"Создаём человека"""
    def __init__(self, name, age, height):
        """"Инициализируем атрибуты человека по умолчанию"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = 82

    def description_person(self):
        """"Получение описания человека"""
        description = f'{self.name}. {self.age} лет. {self.height} см. {self.weight} кг.'
        print(f'Нового человека зовут: {description}')

    def get_weight(self):
        """"Получение веса человека"""
        w = f'{self.weight} кг'
        print(w)

    def update_weight(self, kg): # задаем обяз атрибут метода update_weight, который заменит обяз атрибут всего класса
        """"Обновление веса человека"""
        self.weight = kg # говорим, что новый атрибут kg заменит обяз атрибут self.weight класса Person (значение нового атрибута укажется при обращении к методу)

# создадим класс потомок

class Warrior(Person): # в скобках надо указать родительский класс
    """"Создаём класс воина"""


man = Person("Игорь")
woman = Person("Лена")
man.description_person()
man.update_weight(85) # перезапись дефолтного значения self.weight
man.get_weight()

woman.description_person()
woman.update_weight(52)
woman.get_weight()