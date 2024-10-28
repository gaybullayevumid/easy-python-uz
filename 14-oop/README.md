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
## Inheritance(Meros olish)
Meros olish uchun yangi `class`ni yaratishda mavjud class nomini qavs ichiga yozamiz. Quyidagi misolda `ElectricCar` classi `Car` classidan meros oladi:
```python
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
    
    def display_info(self):
        print(f"Model: {self.model}, Color: {self.color}")
        
class ElectricCar(Car):
    def __init__(self, model, color, battery_size):
        super().__init__(model, color)
        self.battery_size = battery_size
    
    def display_battery(self):
        print(f"Battery size: {self.battery_size} kWh")
```
Yuqorida `ElectricCar` classi `Car` classining xususiyatlarini olgan va qo'shimcha sifatida `battery_size` maydonini qo'shgan. Bu yerda `super()` orqali ota klassning `__init__` metodini chaqirib, `model` va `color` xususiyatlarini o'rnatamiz.




