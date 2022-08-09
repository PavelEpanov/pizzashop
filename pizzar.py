from __future__ import print_function

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def giveRaise(self, percent):
        self.salary = self.salary + (self.salary * percent)
    def work(self):
        print(self.name, " does stuff") # делает что то
    def __repr__(self):
        return f"Employee: {self.name}, salary: {self.salary}"
class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 50000)
    def work(self):
        print(self.name, " maskes food") # готовит еду
class Server(Employee):
    def init(self, name):
        Employee.__init__(self, name, 40000)
    def work(self):
        print(self.name, " interfaces with customer") # Взаимодействует с клиентом
class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)
    def work(self):
        print(self.name, " makes pizza")



if __name__ == "__main__":
    X = Employee()
    print(X)

    bob = PizzaRobot("Bob") # Создать робота по имени боб
    print(bob) # Выполняется унаследованный метод __repr__
    bob.work() # Выполняется действие, специфичное для типа
    bob.giveRaise(0.3) # Повысить зарплату роботу на 30%
    print(bob);print()

    for klass in Employee, Chef, Server, PizzaRobot:
        obj = klass(klass.__name__)
        obj.work()
