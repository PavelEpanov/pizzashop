from __future__ import print_function
from pizzar import PizzaRobot, Server

class Customer:
    def __init__(self, name):
        self.name = name
    def order(self, server):
        print(self.name, "orders from", server) # заказы от
    def pay(self, server):
        print(self.name, "pays for item to", server) # плата за единицу
class Oven:
    def bake(self):
        print("oven bakes") # духовой шкаф выпекает
class PizzaShop:
    def __init__(self):
        self.server = Server("John", 40000) # Внедрить другие объекты
        self.chef = PizzaRobot("Patrick")
        self.oven = Oven()
    def order(self, name):
        customer = Customer(name) # Активизировать другие объекты
        customer.order(self.server) # Заказы клиента, принятые официантом
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

if __name__ == "__main__":
    scene = PizzaShop() # Создать составной объект
    scene.order("Homer") # Эмулировать заказ Гомера
    print("."*8)
    scene.order("Lui") # Эмулировать заказ Луи
