# PYTHON DASTURLASH ASOSLARI

## TUPLES

Qatorlar (`tuples`) Pythonda `o'zgarmas` ma'lumot tuzilmasi bo'lib, ularni bir marta yaratgandan keyin o'zgartirib bo'lmaydi. Ular ro'yxatlar (`lists`) ga o'xshash, lekin qatorlar bir marta yaratib olingandan keyin o'zgartirilmaydi, ya'ni ularga yangi element qo'shib bo'lmaydi, mavjud elementlarni o'chirib bo'lmaydi yoki o'zgartirib bo'lmaydi. Qatorlar ko'pincha o'zgarmas ma'lumotlar to'plamini saqlash uchun ishlatiladi.

### TUPLE YARATISH

```python
# Oddiy tuple yaratish
my_tuple = (1, 2, 3)
print(my_tuple)  # (1, 2, 3)

# list dan tuple yaratish
another_tuple = tuple([4, 5, 6])
print(another_tuple)  # (4, 5, 6)

# bo'sh tuple yaratish
empty_tuple = ()
print(empty_tuple)  # ()

# bitta elementli tuple yaratish uchun vergul qo'yish kerak
single_element_tuple = (1,)
print(single_element_tuple)  # (1,)
```

### TUPLE XUSUSIYATLARI
- **O'zgarmasligi (Immutable):** `Tuple` yaratilgandan so'ng, uning elementlarini `o'zgartirib` yoki `o'chirib` bo'lmaydi.
- **Tartiblanganligi:** `Tuple` ichidagi elementlar `tartiblangan` holda saqlanadi.
- **Qayta ishlash:** `Tuple` ichidagi ma'lumotlar o'z tartibini saqlaydi va turli xil ma'lumot turlarini saqlashi mumkin (masalan, `number`, `string` va boshqalar).

### TUPLENING AFZALLIKLARI
- **O‘zgarmasligi:** Tupleni `himoyalangan` yoki `o‘zgartirilmas` ma’lumotlar saqlash uchun ishlatish mumkin.
- **Tezligi:** Tuplelar ro‘yxatlarga qaraganda `tezroq` ishlovchi ma'lumot turi hisoblanadi.

### TUPLE E'LEMENTLARIGA MUROJAT QILISH

`Tuple` elementlariga ham `list`larga o'xshab indeks orqali murojaat qilish mumkin. Indekslar `0` dan boshlanadi:

```python
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[0])  # 10
print(my_tuple[2])  # 30
print(my_tuple[-1]) # 50 (oxirgi element)
```

### TUPLE USTIDA AMALLAR
> [!NOTE]
> Tuple o'zgarmas bo'lganligi sababli, uni `o'zgartirib bo'lmaydi`. Lekin uni boshqa `tuple`lar bilan `birlashtirish` yoki `takrorlash` mumkin.

1. Tuplelarni birlashtirish:
    - Tuple'lar o'zgarmas (`immutable`) ma'lumot turi bo'lganligi uchun birlashtirish jarayonida asl `tuple`lar o'zgarmaydi. Yangi tuple yaratiladi.

    ```python
    tuple1 = (1, 2)
    tuple2 = (3, 4)
    new_tuple = tuple1 + tuple2
    print(new_tuple)  # (1, 2, 3, 4)
    ```
    - Agar siz bir tupleni o'z-o'ziga birlashtirishni xohlasangiz, yana bir tuple qo'shib berishingiz kerak bo'ladi.
    ```python
    tuple1 = (1, 2, 3)

    # tuple1 ni o'z-o'zidan ikki marta birlashtirish
    result = tuple1 + tuple1
    print(result)
    ```

#### TUPLENI BOSHQA MALUMOT TURLARI BILAN BIRLASHTIRISH

2. Tupleni ko‘paytirish:
```python
tuple1 = ("hello",)
new_tuple = tuple1 * 3
print(new_tuple)  # ('hello', 'hello', 'hello')
```

### TUPLE UZUNLIGINI ANIQLASH

`Tuple`dagi elementlar sonini aniqlash uchun `len()` funksiyasidan foydalaniladi:

```python
my_tuple = (1, 2, 3, 4, 5)
print(len(my_tuple))  # 5
```

### TUPLEDA `in` OPERATORI
- Biror qiymat tupleda bor yoki yo‘qligini `in` operatori yordamida tekshirish mumkin:
```python
my_tuple = ("apple", "banana", "cherry")
print("banana" in my_tuple)  # True
```

### TUPLENI QIYMATLARGA AJRATISH(`Unpacking`)
- Tuplening barcha qiymatlarini o‘zgaruvchilarga ajratib olish mumkin:
```python
my_tuple = ("apple", "banana", "cherry")
(fruit1, fruit2, fruit3) = my_tuple
print(fruit1)  # 'apple'
print(fruit2)  # 'banana'
print(fruit3)  # 'cherry'
```

### TUPLE ICHIDA TUPLE
- Tuple ichida yana boshqa tuplelar saqlanishi mumkin:
```python
nested_tuple = (1, 2, (3, 4), 5)
print(nested_tuple[2])  # (3, 4)
```
### TUPLE BILAN ISHLASHDA FOYDALI FUNKSIYALAR
1. `.count():` Tuple ichida biror qiymat necha marta takrorlanganini aniqlaydi.
```python
my_tuple = (1, 2, 2, 3)
print(my_tuple.count(2))  # 2
```

2. `.index():` Tuple ichida berilgan qiymatning indeksini topadi.
```python
my_tuple = (1, 2, 3)
print(my_tuple.index(2))  # 1
```

> [!NOTE]
> Agar Tuple ga o'zgartirish talab qilinsa, yagona yo'li o'zgarmas ro'yxatni `list()` funksiyasi yordamida `List` (oddiy ro'yxat) ko'rinishiga keltirib olish, o'zgarishlarni bajarsih va qaytarib `tuple()` funktsiyasi yordamida o'zgarmas ro'yxatga o'tkazish mumkin:

```python
toys = ('bus','car','bear','dino','snake','lizard') # o'zgarmas ro'yxat
toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# Ro'yxatga o'zgartirishlar kiritamiz
toys.append('dragon')
toys.remove('bus')
toys[1] = 'mcqueen'
toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
print(toys)
```

# AMALIYOT

1. **Tuple yaratish va qiymatlarni chiqarish.**
    ```python
    # 1. Quyidagi tuple'ni yarating va har bir elementini ekranga chiqaring.
    my_tuple = (10, 20, 30, 40, 50)
    ```
    **Natija:**
    ```shell
    (10, 20, 30, 40, 50)
    ```
2. **Tuple elementlariga indeks orqali murojaat qilish.**
    ```python
    # 2. Quyidagi tuple'dan birinchi va oxirgi elementni ekranga chiqaring.
    my_tuple = ('apple', 'banana', 'cherry', 'date', 'elderberry')
    ```
    **Natija:**
    ```shell
    Birinchi element: apple
    Oxirgi element: elderberry
    ```
3. **Tuple’larni birlashtirish.**
    ```python
    # 3. Ikkita tuple'ni birlashtirib, yangi tuple yarating.
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    ```
    **Natija:**
    ```shell
    (1, 2, 3, 4, 5, 6)
    ```

4. **Tuple uzunligini aniqlash.**
    ```python
    # 4. Quyidagi tuple'ning uzunligini aniqlang.
    my_tuple = ('cat', 'dog', 'rabbit', 'parrot')
    ```
    **Natija:**
    ```shell
    4
    ```

5. **Tuple ichidagi elementlarning qiymatini sanash.**
    ```python
    # 5. Tuple ichida necha marta 'apple' so‘zi mavjudligini aniqlang.
    fruits = ('apple', 'banana', 'cherry', 'apple', 'apple', 'banana')
    ```
    **Natija:**
    ```shell
    3
    ```
6. **Tuple ichida qiymat mavjudligini tekshirish.**
    ```python
    # 6. Tuple ichida 'banana' bor-yo‘qligini tekshiring.
    fruits = ('apple', 'banana', 'cherry')
    ```
    **Natija:**
    ```shell
    True
    ```