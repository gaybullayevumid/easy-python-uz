# class Car:
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
#
#     def display_info(self):
#         print(f"Model: {self.model}, Color: {self.color}")


# class Car:
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
#
#     def display_info(self):
#         print(f"Model: {self.model}, Color: {self.color}")
#
#
# my_car = Car("Chevrolet", "Black")
# my_car.display_info()

#
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance  # private attribute
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"{amount} deposited. New balance: {self.__balance}")
#         else:
#             print("Invalid deposit amount")
#
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print(f"{amount} withdrawn. New balance: {self.__balance}")
#         else:
#             print("Insufficient funds")
#
# # BankAccount ob'ektini yaratamiz va unga pul qo'shamiz
# account = BankAccount(1000)
# account.deposit(500)      # 500 deposited. New balance: 1500
# account.withdraw(200)     # 200 withdrawn. New balance: 1300

#
# class Car:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
#
#     def drive(self):
#         print(f"{self.model} is driving")
#
#     def stop(self):
#         print(f"{self.model} has stopped")
#
# class ElectricCar(Car):
#     def __init__(self, model, color, year, battery_size):
#         super().__init__(model, color, year)  # Ota klass `Car` ning __init__ metodini chaqiramiz
#         self.battery_size = battery_size
#
#     def charge(self):
#         print(f"{self.model} is charging. Battery size: {self.battery_size} kWh")
#
# tesla = ElectricCar("Tesla Model S", "Red", 2023, 100)
# tesla.drive()      # Tesla Model S is driving
# tesla.charge()     # Tesla Model S is charging. Battery size: 100 kWh
# tesla.stop()       # Tesla Model S has stopped

#
# class Bird:
#     def sound(self):
#         print("Bird makes a sound")
#
# class Parrot(Bird):
#     def sound(self):
#         print("Parrot says hello")
#
# class Sparrow(Bird):
#     def sound(self):
#         print("Sparrow chirps")
#
# def make_sound(bird):
#     bird.sound()
#
# parrot = Parrot()
# sparrow = Sparrow()
#
# make_sound(parrot)   # Parrot says hello
# make_sound(sparrow)  # Sparrow chirps

#
# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
#
# class Dog(Animal):
#     def sound(self):
#         print("Woof!")
#
# class Cat(Animal):
#     def sound(self):
#         print("Meow!")
#
# class Horse(Animal):
#     def sound(self):
#         print("jaidjiawjdij")
#
# dog = Dog()
# cat = Cat()
# horse = Horse()
#
# dog.sound()  # Woof!
# cat.sound()  # Meow!
# horse.sound()

