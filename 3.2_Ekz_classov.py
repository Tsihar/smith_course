# 1
class Person():
    """"Создаём человека"""
    def __init__(self, name, age, height, weight):
        """"Инициализируем атрибуты человека"""
        # ниже перечисляем атрибуты ссылкой на класс Person
        self.name = name # указывая переменную (из конструкции __init__) мы начинаем ее использовать (поэтому она подсвечивается при создании)
        self.age = age
        self.height = height
        self.weight = weight
        # ниже создадим метод, который выводит инфу об экземпляре класса Person

    def description_person(self):
        """"Получение описания человека"""
        description = f'{self.name}. {self.age} лет. {self.height} см. {self.weight} кг.'
        print(f'Нового человека зовут: {description}')

    # ниже создадим метод, который будет выводить вес созданного человека
    def get_weight(self):
        w = f'{self.weight} кг'
        print(w)

man = Person('Игорь', 30, 190, 82)

man.description_person()
man.get_weight()

# 2 при инициализации атрибутов мы можем задать значения атрибутов по умолчанию
# class Person():
#     """"Создаём человека"""
#     def __init__(self, name): # удалили необяз атрибуты иначе система выдаст ошибку
#         """"Инициализируем атрибуты человека по умолчанию"""
#         self.name = name
#         self.age = 29 # задали возраст и ниже вес с ростом дефолтные, это значит что новые созданные экземпляры классов будут иметь дефолтные значения как указано в атрибутах класса
#         self.height = 190
#         self.weight = 82
#
#     def description_person(self):
#         """"Получение описания человека"""
#         description = f'{self.name}. {self.age} лет. {self.height} см. {self.weight} кг.'
#         print(f'Нового человека зовут: {description}')
#
#     def get_weight(self):
#         w = f'{self.weight} кг'
#         print(w)

# man = Person("Игорь") # убрали значения для age, height и weight, так как уже задали их по дефолту в атрибутах класса
#
# man.get_weight()

# 3.1 Хотим проапдейтить вес (когда он задан по дефолту) для определенного экземпляра класса

# class Person():
#     """"Создаём человека"""
#     def __init__(self, name):
#         """"Инициализируем атрибуты человека по умолчанию"""
#         self.name = name
#         self.age = 29
#         self.height = 190
#         self.weight = 82
#
#     def description_person(self):
#         """"Получение описания человека"""
#         description = f'{self.name}. {self.age} лет. {self.height} см. {self.weight} кг.'
#         print(f'Нового человека зовут: {description}')
#
#     def get_weight(self):
#         """"Получение веса человека"""
#         w = f'{self.weight} кг'
#         print(w)
#
#     def update_weight(self, kg): # задаем обяз атрибут метода update_weight, который заменит обяз атрибут всего класса
#         self.weight = kg # говорим, что новый атрибут kg заменит обяз атрибут self.weight класса Person (значение нового атрибута укажется при обращении к методу)
#
# man = Person("Игорь")
# woman = Person("Лена")
# man.description_person()
# man.update_weight(85) # перезапись дефолтного значения self.weight
# man.get_weight()
#
# woman.description_person()
# woman.update_weight(52)
# woman.get_weight()
#
# #3.2 Также можно перезаписать вес человека (или другой атрибут класса) напрямую через экземпляр класса
# man.weight = 89 # экз класса, потом его атрибут, потом его значение, но это не совсем корректный подход
# man.get_weight()


class Triangle():

    def __init__(self, height, side1, side2):
        self.height = height
        self.basement = 4
        self.side1 = side1
        self.side2 = side2

    def area(self):
        a = self.height * self.basement / 2
        print(f'Площадь треугольника равна: {a}')

    def perimeter(self):
        p = self.side1 + self.side2 + self.basement
        print(f'Периметр треугольника равен: {p}')

    def update_basement(self, new_v):
        self.basement = new_v

values = Triangle(5, 3, 4)

# values.update_basement(5)
values.basement = 6
values.area()

# values.perimeter()
