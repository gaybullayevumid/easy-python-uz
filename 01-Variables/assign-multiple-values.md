# Assign multiple values

Pythonda bir nechta qiymatlarni bir nechta o'zgaruvchilarga bitta qatorda berish mumkin.

# Assigning the same value

Bir nechta o'zgaruvchilarga bitta qiymat saqlash.

```python
a = b = c = 100
print(a, b, c)
```

# Assigning different values

Bir nechta o'zgaruvchilarga har xil qiymat saqlash.

```python
a, b, c = 20, 2.5, "Python"
print(a)  # 20
print(b)  # 2.5
print(c)  # "Python"
```

# Using string slicing

Matndagi so'zlarni index orqali kesib olib har bir nechta o'zgaruvchilarga saqlash.

```python
text = "Easy Python"
a, b = text[0:5], text[5:]
print(a)
print(b)
```

# Using * for arbitrary values

* operatorini ishlatib, bir nechta qiymatni bitta o‘zgaruvchiga saqlash mumkin.

```python
numbers = (10, 20, 30, 40, 50)
x, *y, z = numbers
print(x)  # 10
print(y)  # [20, 30, 40]
print(z)  # 50
```