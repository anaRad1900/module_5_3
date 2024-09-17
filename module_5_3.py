class House:
    # Метод __init__ для инициализации объекта с именем и количеством этажей
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    # Метод go_to для перемещения на новый этаж
    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    # Специальный метод __len__ для возвращения количества этажей
    def __len__(self):
        return self.number_of_floors

    # Специальный метод __str__ для возвращения строки с названием и количеством этажей
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    # Перегрузка операторов сравнения по количеству этажей
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    # Перегрузка операторов сложения
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __iadd__(self, value):
        return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# Вывод объектов
print(h1)  # Ожидаемый результат: "Название: ЖК Эльбрус, кол-во этажей: 10"
print(h2)  # Ожидаемый результат: "Название: ЖК Акация, кол-во этажей: 20"

# Сравнение по количеству этажей
print(h1 == h2)  # Ожидаемый результат: False

# Увеличение количества этажей
h1 = h1 + 10  # Ожидаемый результат: h1 теперь имеет 20 этажей
print(h1)
print(h1 == h2)  # Ожидаемый результат: True

h1 += 10  # Ожидаемый результат: h1 теперь имеет 30 этажей
print(h1)

h2 = 10 + h2  # Ожидаемый результат: h2 теперь имеет 30 этажей
print(h2)

# Сравнения
print(h1 > h2)  # Ожидаемый результат: False
print(h1 >= h2)  # Ожидаемый результат: True
print(h1 < h2)  # Ожидаемый результат: False
print(h1 <= h2)  # Ожидаемый результат: True
print(h1 != h2)  # Ожидаемый результат: False
