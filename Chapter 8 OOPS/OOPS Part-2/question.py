# python3 ./question.py




# question 1
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 22/7 * self.radius ** 2

    def perimeter(self):
        return 2 * 22/7 *self.radius

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())

# question 2
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails1(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")

    def showDetails2(self):
        print("name =", self.name)
        print("age =", self.age)

engg1 = Engineer("Shubham", 24)
engg1.showDetails1()
engg1.showDetails2()

# question 3
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    
    def __gt__(self, ord2):
        return self.price > ord2.price

odr1 = Order("chips", 20)
odr2 = Order("tea", 15)

print(odr1 > odr2)