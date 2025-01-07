# Assign Multiple Values

Pythonda bir nechta qiymatlarni bir nechta o'zgaruvchilarga bitta qatorda berish mumkin.

# Assigning the Same Value

```python
a = b = c = 100
print(a, b, c)
```

# Assigning Different Values

```python
a, b, c = 20, 2.5, "Python"
print(a)  # 20
print(b)  # 2.5
print(c)  # "Python"
```

```python
text = "Easy Python"
a, b = text[0:5], text[5:]
print(a)
print(b)
```

# Using * for Arbitrary Values

* operatorini ishlatib, bir nechta qiymatni bitta o‘zgaruvchiga berish mumkin.

```python
numbers = (10, 20, 30, 40, 50)
x, *y, z = numbers
print(x)  # 10
print(y)  # [20, 30, 40]
print(z)  # 50
```