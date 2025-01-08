# Data Types

| Definition      | Type                               |
|-----------------|------------------------------------|
| Text Type       | `str`                              |
| Numeric Types   | `int`, `float`, `complex`          |
| Sequence Types  | `list`, `tuple`, `range`           |
| Mapping Type    | `dict`                             |
| Set Types       | `set`, `frozenset`                 |
| Boolean Type    | `bool`                             |
| Binary Types    | `bytes`, `bytearray`, `memoryview` |
| None Type       | `NoneType`                         |

# Getting the data type

`type()` funksiyasi yordamida hamma obyektni malumot turini olish mumkin.

```python
text = "Easy Python"
a = 20
b = 3.14
is_active = True
print(type(text))
print(type(a))
print(type(b))
print(type(is_active))
```

# Setting the data type

Python dasturlash tilida o'zgaruvchilarga qiymat saqlanganda malumot turini o'zi avtomatik qabul qiladi.

| Example                                      | Data type  |
|----------------------------------------------|------------|
| x = "Easy Python"                            | str        |
| x = 20                                       | int        |
| x = 20.5                                     | float      |
| x = 1j                                       | complex    |
| x = ["apple", "banana", "cherry"]            | list       |
| x = ("apple", "banana", "cherry")            | tuple      |
| x = range(6)                                 | range      |
| x = {"name" : "John", "age" : 36}            | dict       |
| x = {"apple", "banana", "cherry"}            | set        |
| x = frozenset({"apple", "banana", "cherry"}) | frozenset  |
| x = True                                     | bool       |
| x = b"Hello"                                 | bytes      |
| x = bytearray(5)                             | bytearray  |
| x = memoryview(bytes(5))                     | memoryview |
| x = None                                     | NoneType   |

