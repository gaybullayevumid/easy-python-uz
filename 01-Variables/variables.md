# Variables

**O'zgaruvchi** — bu ma’lumotlarni vaqtincha saqlash uchun ishlatiladigan nomlangan konteynerlardir. O‘zgaruvchilar yordamida ma’lumotlar bilan ishlash, ularni saqlash va qayta ishlatish qulaylashadi.

![alt text](images/image.png)

# Creating Variables

Python dasturlash tilida o'zgaruvchi yaratadigan `keyword` yo'q.

O'zgaruvchi unga birinchi marta qiymat berilganda yaratiladi.

```python
x = 5 # int -> Integer
y = 3.14 # float -> Floating point number
name = "Alice"  # str -> String
is_active = True  # bool -> Boolean
print(x)
print(y)
print(name)
print(is_active)
```

`variable` diyilishini sababi uning qiymati istalgan payt o'zgarishi mumkin.

```python
x = 5
x = "Hello world"
print(x)
```

# Casting

Python dasturlash tilida o'zgaruvchilar turini bir ma'lumot turidan boshqa ma'lumot turiga o'zgartirish jarayoni `type casting` deb ataladi.

```python
x = str(3)    # x -> '3'
y = int(3)    # y -> 3
z = float(3)  # z -> 3.0
```

# Get the Type

`type()` funksiyasi yordamida o'zgaruvchilarning malumot turini olish mumkin.

```python
x = 5
y = "John"
print(type(x))
print(type(y))
```

# Single or Double Quotes?

O'zgaruvchilar uchun single quote (`''`) yoki duble quote (`""`) ishlatishni farqi yo'q. Ikkalasi ham bir xil ishlaydi.

Single quote
```python
name = 'John'
```

Duble quote
```python
name = "John"
```

```python
# Single quotes ishlatamiz:
message = 'He said, "Python is awesome!"'
print(message)  # Natija: He said, "Python is awesome!"

# Double quotes ishlatamiz:
message = "It's a beautiful day!"
print(message)  # Natija: It's a beautiful day!
```

