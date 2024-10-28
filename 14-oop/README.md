# PYTHON DASTURLASH ASOSLARI

# 14-dars OOP(Object-Oriented Programming)

> [!NOTE]
> **Object-Oriented Programming** (`OOP`) Python dasturlash tilida muhim mavzulardan biri hisoblanadi va u orqali dasturlarni modulli, qayta foydalanish mumkin bo'lgan, tuzilmaviy kodlarni yaratish mumkin. Keling, OOPning asosiy tushunchalari va amaliy misollari bilan tanishib chiqamiz.

**Key OOP Principles:**
1. **Encapsulation** (Inkapsulyatsiya) - Ma'lumotlarni va funksiyalarni (metodlarni) bitta birlikda, ya'ni ob'ekt ichida saqlashni ta'minlaydi. Bu ma'lumotlarni tashqi tomondan to'g'ridan-to'g'ri o'zgartirilmasligini ta'minlash uchun ishlatiladi.
2. **Inheritance** (Meros olish) - Bir klass (ota klass) xususiyatlarini boshqa klassga (farzand klass) o'tkazish imkoniyatini beradi, ya'ni yangi klassni mavjud klass asosida yaratish mumkin.
3. **Polymorphism** (Polimorfizm) - Bir xil nomdagi metodlarning turli xil sinflarda turlicha ishlash imkoniyatini beradi.
4. **Abstraction** (Abstraksiya) - Muhim detallarni ajratib olish va ortiqcha tafsilotlarni yashirishni ta'minlaydi.

# What is a `class` in Python?
> [!NOTE] 
> `class` bu ma'lumotlar va ularni qayta ishlovchi funksiyalarni birlashtiruvchi `shablon` yoki `qolip` hisoblanadi. class yordamida `obyektlar` yaratamiz. Har bir obyekt biror `class` ning nusxasi hisoblanadi.

# Creating a Simple `class`
`class` yaratish uchun `class` kalit so'zidan foydalanamiz va unga `nom` beramiz.
```python
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
    
    def display_info(self):
        print(f"Model: {self.model}, Color: {self.color}")
```
Yuqoridagi misolda `Car` nomli `class` yaratilgan. `__init__` metodi har safar yangi obyekt yaratilganda avtomatik ravishda chaqiriladi. Bu metod obyektni boshlang'ich holatini o'rnatadi. `self` bu obyektning o'zi, ya'ni yaratilgan obyektga murojaat qilish uchun ishlatiladi.

# Creating an Object
`class` asosida obyekt yaratish uchun `class` nomiga qavs ichida kerakli parametrlarni yozamiz:
```python
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
    
    def display_info(self):
        print(f"Model: {self.model}, Color: {self.color}")
        
my_car = Car("Chevrolet", "Black")
my_car.display_info()
```
Bu kod `Car` classidan yangi `my_car` obyektini yaratadi va uning ma'lumotlarini qaytaradi. Natija quyidagicha bo'ladi:
```shell
Model: Chevrolet, Color: Black
```
## Encapsulation(Inkapsulyatsiya)
`Encapsulation` yordamida `class`dagi xususiyatlar (`property`) va metodlarni yashirish mumkin. Bu o'zgaruvchilarning to'g'ridan-to'g'ri o'zgartirilishini oldini olib, maxsus metodlar orqali ularga kirishni ta'minlaydi.
Pythonda private(`xususiy`) o'zgaruvchilarni yaratish uchun o'zgaruvchining nomi oldiga ikki pastki chiziq (`__`) qo'yamiz:
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn. New balance: {self.__balance}")
        else:
            print("Insufficient funds")

# BankAccount ob'ektini yaratamiz va unga pul qo'shamiz
account = BankAccount(1000)
account.deposit(500)      # 500 deposited. New balance: 1500
account.withdraw(200)     # 200 withdrawn. New balance: 1300
```
Yuqorida `__balance` xususiyati to'g'ridan-to'g'ri obyektdan kirish mumkin emas, faqat `deposit` va `withdraw` metodlari orqali o'zgartiriladi.

## Inheritance(Meros olish)
Meros olish boshqa `class`dan xususiyatlar va metodlarni `meros` qilib olish imkonini beradi, bu orqali kod qayta ishlatiladi. Keling, `Car` va `ElectricCar` misollarini yanada kengaytiramiz.
```python
class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

    def drive(self):
        print(f"{self.model} is driving")

    def stop(self):
        print(f"{self.model} has stopped")

class ElectricCar(Car):
    def __init__(self, model, color, year, battery_size):
        super().__init__(model, color, year)  # Ota klass `Car` ning __init__ metodini chaqiramiz
        self.battery_size = battery_size

    def charge(self):
        print(f"{self.model} is charging. Battery size: {self.battery_size} kWh")

tesla = ElectricCar("Tesla Model S", "Red", 2023, 100)
tesla.drive()      # Tesla Model S is driving
tesla.charge()     # Tesla Model S is charging. Battery size: 100 kWh
tesla.stop()       # Tesla Model S has stopped
```
Bu yerda `ElectricCar` classi `Car` classidan `meros` oladi va qo'shimcha `charge` metodini qo'shadi:

**Natija:**
```shell
Model: Tesla, Color: White
Battery size: 75 kWh
```
## Polymorphism(Polimorfizm)
Polimorfizm bir xil nomdagi metodlarning turli `class`larda turlicha ishlashini anglatadi. Bu `OOP` da muhim bo'lib, turli ob'ektlarga bir xil metodni qo'llash imkonini beradi.

```python
class Bird:
    def sound(self):
        print("Bird makes a sound")

class Parrot(Bird):
    def sound(self):
        print("Parrot says hello")

class Sparrow(Bird):
    def sound(self):
        print("Sparrow chirps")
```
Yuqorida `Parrot` va `Sparrow` classlari `Bird` classidan meros olgan, lekin har bir classda `sound` metodi turlicha bajariladi:

```python
class Bird:
    def sound(self):
        print("Bird makes a sound")

class Parrot(Bird):
    def sound(self):
        print("Parrot says hello")

class Sparrow(Bird):
    def sound(self):
        print("Sparrow chirps")
        
def make_sound(bird):
    bird.sound()

parrot = Parrot()
sparrow = Sparrow()

make_sound(parrot)   # Parrot says hello
make_sound(sparrow)  # Sparrow chirps
```
## Abstraction(Abstraksiya)
Abstraksiya yordamida foydalanuvchilar faqat kerakli `metod` va `atribut`larga kirishi mumkin bo'ladi. Pythonda to‘g‘ridan-to‘g‘ri abstrakt classlar mavjud emas, ammo **abc**(`Abstract Base Classes`) modulidan foydalanib, `abstrakt class` yaratish mumkin. Keling, hayvonlar misolida ko'ramiz:

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Woof!")

class Cat(Animal):
    def sound(self):
        print("Meow!")

dog = Dog()
cat = Cat()

dog.sound()  # Woof!
cat.sound()  # Meow!

```
Bu yerda `Animal class`i `abstract class` bo'lib, undagi `sound` metodi barcha farzand classlarida aniqlanishi kerak. `Dog` va `Cat` classlarida `sound` metodini har xil bajarish mumkin.

# AMALIYOT

1. `class` yaratish
   - `Book` classini yarating. U quyidagi atributlarga ega bo'lishi kerak:
     - **title**(`nomi`)
     - **author**(`muallifi`)
     - **year**(`nashr yili`)
   - Shuningdek, classda `display_info` metodini qo'shing, u kitob haqida ma'lumotlarni chiqarishi kerak.
```python
class Book:
    # Bu yerga kod yozing
```

2. Instansiya O'zgaruvchilarini Qo'llash
   - Yuqoridagi `Book` classini davom ettiring va unda `get_age` metodini qo'shing. Bu metod kitobning bugungi kunga nisbatan `yoshini` hisoblash kerak (`hozirgi yil - nashr yili`).
```python
class Book:
    # Bu yerga kod yozing
```

3. Meros Olish
   - Book classidan meros oluvchi `Ebook` classini yarating. `Ebook` classi quyidagi qo'shimcha atributga ega bo'lishi kerak:
     - **file_size**(`fayl o'lchami`)
   - `Ebook` classida `display_info` metodini yangilang va unda `fayl o'lchamini` ko'rsatish uchun ma'lumotlarni chiqarishi kerak.

```python
class Book:
    # Bu yerga kod yozing

class Ebook(Book):
    # Bu yerga kod yozing
```

4. Inkapsulyatsiya
   - `BankAccount` classini yarating, unda maxfiy `__balance` atributi bo'lishi kerak. classda quyidagi metodlar bo'lishi kerak:
     - **deposit**(`amount`) - hisobga pul qo'shish.
     - **withdraw**(`amount`) - hisobdan pul yechib olish.
     - **get_balance()** - hisobdagi mablag'ni ko'rsatish.

```python
class BankAccount:
    # Bu yerga kod yozing
```

5. classlararo Aloqa
   - `Author` classini yarating, unda `name` va `books` atributlari bo'lishi kerak. `books` - bu `Book` classidan iborat ro'yxat. `Author` classida quyidagi metodlar bo'lishi kerak:
     - **add_book**(`book`) - yangi kitob qo'shish.
     - **display_books()** - muallifga tegishli kitoblarni ko'rsatish.

```python
class Author:
    # Bu yerga kod yozing
```



