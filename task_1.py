# Задача 3
class Money:
    def __init__(self, rubles: int, kopecks: int):
        self.rubles = rubles
        self.rubles += kopecks // 100
        self.kopecks = kopecks % 100

    def __str__(self):
        return f'Стоимость товара {self.rubles} рублей, {self.kopecks} копеек'


class Good(Money):
    def __init__(self, rubles: int, kopecks: int, procent: int):
        super().__init__(rubles, kopecks)
        self.procent = procent

    def sale(self):
        self.rubles -= self.rubles * self.procent * 0.01
        self.kopecks -= self.kopecks * self.procent * 0.01

    def __str__(self):
        return f'Стоимость товара с учетом скидки {self.rubles} рублей, {self.kopecks} копеек'


good_1 = Money(100, 120)
good_2 = Good(1000, 10, 20)
good_2.sale()
print(good_1)
print(good_2)

# Задача 2
import random

class Man:
    def __init__(self, name, age, endurance):
        self.name = name
        self.age = age
        if endurance > 100:
            print('Максимальное значение выносливости: 100. Попробуйте снова')
        else:
            self.endurance = endurance

    def sleep(self):
        pass



class Student(Man):
    def __init__(self, name, age, endurance):
        super().__init__(name, age, endurance)
        self.course = random.randint(1,6)

    def how_much_time(self):
        count_of_pairs = 1
        self.endurance = self.endurance*(1 - 0.1*(self.course-1))
        while self.endurance > 20:
            if count_of_pairs == 1:
                print(f'На {count_of_pairs} паре значение выносливости: {self.endurance}')
                self.endurance -= 15
            else:
                print(f'На {count_of_pairs} паре значение выносливости: {self.endurance}')
                self.endurance -= 15 * 1.25 * (count_of_pairs - 1)
            count_of_pairs += 1
        print(f'{self.name} уснул на {count_of_pairs} паре')


    def __str__(self):
        return f'{self.name} учится на {self.course} курсе'

Studen_1 = Student('Ivan', '21', 120)
Studen_2 = Student('Ivan', '21', 100)
print(Studen_2)
Studen_2.how_much_time()

# Задача 1
class Car:
    def __init__(self, x, y): #инициализация
        self.x = x
        self.y = y


    def move(self, x1, y1): #метод, возвращающий расстояние
        self.distantion = ((x1-self.x)**2 +(y1-self.y)**2)**0.5
        self.x = x1
        self.y = y1
        return self.distantion


class Bus(Car): #класс автобус, наследующийся от класса машина
    def __init__(self, x, y):
        super().__init__(x, y)
        self.passengers = 0
        self.money = 0

    def enter(self, count_passengers): #метод, добавляющий определенное количество пассажиров
        self.passengers+= count_passengers

    def quit(self, count_passengers): #метод, убирающи определенное количество пассажиров
        self.passengers -= count_passengers


    def count_money(self): #метод, считающий полную прибыль при заданной стоимости поездки (50)
        return self.passengers * 50 * self.distantion


    def __str__(self): #метод, переопределяющий функцию print()
        return f'{self.count_money()}'

BUS_1 = Bus(0, 0)
BUS_1.move(3, 4)
BUS_1.enter(10)

print(BUS_1)