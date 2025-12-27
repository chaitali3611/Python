# python3 ./inheritance.py




# Intro
class Car:
    color = "black"
    @staticmethod
    def start():
        print("Car strated..")

    @staticmethod
    def stop():
        print("Car stopped..")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.color)


# single Inheritance
class Car:
    color = "black"
    @staticmethod
    def start():
        print("Car strated..")

    @staticmethod
    def stop():
        print("Car stopped..")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.color)

# multi-level Inheritance
class Car:
    @staticmethod
    def start():
        print("Car strated..")

    @staticmethod
    def stop():
        print("Car stopped..")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()

# Multiple Inheritance
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A, B):
    varC = "welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varA)
print(c1.varB)
