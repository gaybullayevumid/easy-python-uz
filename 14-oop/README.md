# PYTHON DASTURLASH ASOSLARI

# 14-dars OOP(Object-Oriented Programming)

> [!NOTE]
> **Object-Oriented Programming** (`OOP`) Python dasturlash tilida muhim mavzulardan biri hisoblanadi va u orqali dasturlarni modulli, qayta foydalanish mumkin bo'lgan, tuzilmaviy kodlarni yaratish mumkin. Keling, OOPning asosiy tushunchalari va amaliy misollari bilan tanishib chiqamiz.

**OOP** ning asosiy tamoyillari quyidagilar:
1. **Encapsulation** (Inkapsulyatsiya) - Ma'lumotlarni va funksiyalarni (metodlarni) bitta birlikda, ya'ni ob'ekt ichida saqlashni ta'minlaydi. Bu ma'lumotlarni tashqi tomondan to'g'ridan-to'g'ri o'zgartirilmasligini ta'minlash uchun ishlatiladi.
2. **Inheritance** (Meros olish) - Bir klass (ota klass) xususiyatlarini boshqa klassga (farzand klass) o'tkazish imkoniyatini beradi, ya'ni yangi klassni mavjud klass asosida yaratish mumkin.
3. **Polymorphism** (Polimorfizm) - Bir xil nomdagi metodlarning turli xil sinflarda turlicha ishlash imkoniyatini beradi.
4. **Abstraction** (Abstraksiya) - Muhim detallarni ajratib olish va ortiqcha tafsilotlarni yashirishni ta'minlaydi.

# `class` nima?
> [!NOTE] 
> `class` bu ma'lumotlar va ularni qayta ishlovchi funksiyalarni birlashtiruvchi `shablon` yoki `qolip` hisoblanadi. class yordamida `obyektlar` yaratamiz. Har bir obyekt biror `class` ning nusxasi hisoblanadi.

# `class` qanday yaratiladi?
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

# Obyekt yaratish
class asosida obyekt yaratish uchun `class` nomiga qavs ichida kerakli parametrlarni yozamiz:
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
Bu kod `Car` klassidan yangi `my_car` obyektini yaratadi va uning ma'lumotlarini chop etadi. Natija quyidagicha bo'ladi:
```shell
Model: Chevrolet, Color: Black
```

