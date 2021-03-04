# import math
# Class and object
    # noun -> object
    # adjective -> attribute (property)(state)
    # verb/action -> behaviour (method)
# Inheritance
# Encapsulation (Data hiding process)
# Polymorphism
# Abstraction
# Access Modifier
# Accessor and Mutator (functions)

# class Car:
#     # initialiser function
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model

#     def start(self):
#         print(f"{self.model} started")

# bmw = Car("black", "BMW001")
# # print(bmw.__dict__)
# # bmw.start()
# audi = Car("red", "A009")
# # print(audi.__dict__)
# audi.start()
# mer = Car("army green", "AGM1")
# # print(mer.__dict__)
# mer.start()

class Product:

    def __init__(self, name, price, qty):
        self.name = name
        self.__price = price # Name mangaling
        self.qty = qty

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price > 0:
            self.__price = price
        else:
            raise ValueError("Price can not be less than zero")

    def __str__(self):
        return f"{self.name} / {self.price}"

    def __eq__(self, obj):
        return self.qty == obj.qty


tshirt = Product("T-Shirt", 1000, 5)
pant = Product("Pant", 1500, 6)
shoes = Product("Shoes", 1600, 6)

print(shoes == pant) # Operator overloading
print(shoes.__eq__(pant))
# print(pant)
# print(shoes)

# print("Price Before:", tshirt.price)
# try:
#     tshirt.price = 500
# except ValueError as err:
#     print(err)
# print("Price after: ", tshirt.price)

# class Student:
#     # static or class variable
#     college_name = "ABC College"
#     def __init__(self, _id, name):
#         # instance variable
#         self._id = _id
#         self.name = name

# st = Student("001", "Ram")
# st2 = Student("002", "Shyam")
# print(st2.college_name)

# class Calculator:

#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#     def add(self): # instance method
#         return self.num1 + self.num2

#     def difference(self):
#         return self.num1 - self.num2

#     @staticmethod
#     def square_root(num):
#         return num ** 0.5

# c = Calculator(10, 20)
# print(c.add())
# print(c.difference())
# print(Calculator.square_root(25))


