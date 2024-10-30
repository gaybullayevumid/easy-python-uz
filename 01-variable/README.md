# PYTHON DASTURLASH ASOSLARI

# VARIABLES AND DATA TYPES

>[!NOTE]
> Python dasturlash tilida `variables` — bu ma’lumotlarni `vaqtincha saqlash` uchun ishlatiladigan `nomlangan konteynerlardir`. O‘zgaruvchilar yordamida `ma’lumotlar bilan ishlash`, `ularni saqlash` va `qayta ishlatish` qulaylashadi.

## O'ZGARUVCHILAR

**O'zgaruvchi** - kompyuter xotirasida ma'lum bir qiymatni saqlash uchun ajratilgan joy.

![alt text](images/image.png)

**Example:**

Quyidagi misolda 4 ta o'zgaruvchi yaratdik (`x`, `y`, `name` va `is_student`) va ularga har xil ma'lumot yukladik.

```python
x = 5 # Butun son (int)
y = 3.14 # Haqiqiy son (float)
name = "Alice"  # Matn (str)
is_student = True  # Mantiqiy qiymat (bool)
print(x)
print(y)
print(name)
print(is_student)
```

**Result:**

`5` <br>
`3.14` <br>
`Alice` <br>
`True`

**Example:**

`variable` diyilishini sababi uning qiymati istalgan payt o'zgarishi mumkin:

```python
name = 'Alisher'
print(name)
name = "Muhammad"
print(name)
```

**Result:**

`Alisher` <br>
`Muhammad`

Yuqoridagi misolda `name` nomli o'zgaruvchiga avval `Alisher` keyin esa `Muhammad` deb qiymat berdik.

### O'ZGARUVCHILARNI NOMLASH
> [!CAUTION]
> O'zgaruvchilarga nom berishda quyidagi qoidalarga amal qiling:
> - O'zgaruvchi nomi harf yoki pastki chiziq (`_`) bilan boshlanishi kerak
> - O'zgaruvchi nomi raqam bilan boshlanishi mumkin emas
> - O'zgaruvchi nomida faqatgina lotin alifbosi harflari (`A-z`), raqamlar (`0-9`) va pastki chiziq (`_`) qatnashishi mumkin
> - O'zgaruvchi nomida bo'shliq (пробел) bo'lishi mumkin emas
> - O'zgaruvchi nomida katta-kichik harflar turlicha talqin qilinadi (`ism`, `ISM`, va `Ism` uchta turli o'zgaruvchi)

**Q'shimcha qoidalar:**
- O'zgaruvchi nomini kichik harflar bilan yozing.
- O'zgaruvchi nomida 2 va undan ortiq so'z qatnashsa ularning orasini pastki chiziq (`_`) bilan ajrating (`ism_sharif="Umid G'aybullayev"`) 
- O'zgaruvchiga tushunarli nom bering (`y=20` emas `yosh=20`, `d="Korea"` emas `davlat = "Korea"` va hokazo)
- Shuningdek o'zgaruvchilarga Pythonda ishlatiladigan funksiyalar va maxsus kalit so'zlarning(keywords) nomini bermang. Kalit so'zlar ro'yhatini ko'rish uchun python faylga  uyidagi kodni yozamiz:
```python
import keyword
print(keyword.kwlist)
```
Marhamat, ekraningizda Pythondagi maxsus kalit so'zlar ro'yhatini ko'ryapsiz:
![alt text](images/keyword.png)

## MA'LUMOT TURLARI
Python dasturlash tilida `7` ta ma'lumot turi bor, ular quyidagilar:

![alt text](images/data_types.png)

## STRING

- **String(str)** - Matnli ma'lumotlarni ifodalaydi. Masalan: `"hello"`, `'world'`, `"123"`.

**Example:**  

```python
# ikkitalik qo'shtirnoqlar bilan
text = "Hello world"
print(text)

# bittalik qo'shtirnoqlar bilan
text = 'Hello world'
print(text)

# Ko'p qatorli stringlar uchlik qo'shtirnoqlar bilan
text = """This is a
multiline string."""
print(text)

text = '''This is also a
multiline string.'''
print(text)
```
### STRING USTIDA AMALLAR
Matnlarni qo'shish uchun `+` operatoridan foydalanamiz.

**Example:**

```python
name = "Umid"
print("Mening ismim " + name)
```
**Result:** `Mening ismim Umid`

**Example:**

```python
first_name = "Umid"
last_name = "G'aybullayev"
print(first_name + last_name)
```
**Result:** `UmidG'aybullayev` <br>

Yuqoridagi kodimizda ism va familiya qo'shilib qoldi, uni to'g'irlash uchun quyidagi ko'rinishda yozamiz:

**Example:**

```python
ism = "Umid"
familiya = "G'aybullayev"
print(ism + ' ' + familiya)
```
**Result:** `Umid G'aybullayev`

### STRING UZUNLIGINI ANIQLASH
Matnlarimizni uzunligini topish uchun `len()` funksiyasidan foydalanamiz.

**Example:**

```python
text = "Hello, World!"
length = len(text)  # 13
print(length)
```
**Result:** `13`

### STRING E'LEMENTLARIGA MUROJAT QILISH
Matnlarimiz ichidan o'zimizga kerak bo'lgan harflarni ajratib olish uchun quyidagi usuldan foydalanamiz:

**Example:**

```python
text = "Hello world!"
first_char = text[0] # H
last_char = text[-1]  # '!'
substring = text[0:5]  # 'Hello'
print(first_char)
print(last_char)
print(substring)
```
**Result:** <br>
`H` <br>
`!` <br>
`Hello`

### STRINGLARNI KO'PAYTIRISH

**Example:**

```python
text = "Hello"
text_repeated = text * 3
print(text_repeated)
```
**Result:** `HelloHelloHello`

### F-STRING(Python 3.6+)

**Example:**

```python
ism = "Umid"
yosh = 20
text = f"Mening ismim {ism}, yoshim {yosh}da" #Mening ismim Umid, yoshim 20da
print(text)
```
**Result:** `Mening ismim Umid, yoshim 20da`

### STRING METODLARI
Python dasturlash tilida, stringlar ustida turli xil operatsiyalarni bajarish uchun bir qancha o'rnatilgan metodlar mavjud. Quyida eng ko'p qo'llaniladigan string metodlari va ularning misollari keltirilgan:

1. `.upper()` - Matndagi barcha harflarni katta harfga aylantiradi.

```python
text = "hello"
print(text.upper()) #HELLO
```
2. `.lower()` - Matndagi barcha harflarni kichik harfga aylantiradi.

```python
text = "HELLO"
print(text.lower()) #hello
```
3. `.capitalize()` - Matnning birinchi harfini katta harfga, qolganlarini kichik harfga aylantiradi.

```python
text = "hello world"
print(text.capitalize()) # Hello world
```
4. `.title()` - Matndagi har bir so'zning birinchi harfini katta harfga aylantiradi.

```python
text = "hello world"
print(text.title()) # Hello World
```

5. `.lstrip()` - Matnning faqat boshidagi bo'sh joylarni olib tashlaydi.

```python
text = "    hello world    "
print(text.lstrip()) # "hello world    "
```
6. `.rstrip()` - Matnning faqat oxiridagi bo'sh joylarni olib tashlaydi.

```python
text = "    hello world    "
print(text.rstrip()) # "    hello world"
```
7. `.strip()` - Matnning boshida va oxiridagi bo'sh joylarni olib tashlaydi.

```python
text = "    hello world    "
print(text.strip()) # "hello world"
```

8. `.replace()` - Matndagi ma'lum bir qatorni boshqa qator bilan almashtiradi.

```python
text = "hello world"
print(text.replace("world", "Python"))  # "hello Python"
```
9. `.split()` - Matnni ma'lum bir ajratgich bo'yicha qismlarga ajratadi va `ro'yxat` qaytaradi.

```python
text = "hello world"
print(text.split()) # ['hello', 'world']
```
10. `.join()` - Ro'yxatdagi elementlarni birlashtiradi va `string` qaytaradi.

```python
words = ['hello', 'world']
print(" ".join(words))  # "hello world"
```
11. `.find()` - Matn ichida ma'lum bir qatorni qidiradi va uning indeksini qaytaradi. Agar topilmasa, `-1` qaytaradi.
```python
text = "hello world"
print(text.find("world"))  # 6
```
12. `.startswith()` - Matn ma'lum bir qator bilan boshlanishini tekshiradi. `True` yoki `False` qaytaradi.
```python
text = "hello world"
print(text.startswith("hello"))  # True
```
13. `.endswith()` - Matn ma'lum bir qator bilan tugashini tekshiradi. `True` yoki `False` qaytaradi.
```python
text = "hello world"
print(text.endswith("world"))  # True 
```

14. `.casefold()` - metodi kichik harflar va katta harflarni taqqoslashda yordam beradi, ya'ni matndagi har qanday katta harfni kichik harfga aylantiradi. `.casefold()` metodi `.lower()` metodiga o'xshaydi, lekin u turli tillardagi katta-kichik harf farqlarini ham inobatga oladi.

```python
text = "Hello World!"
print(text.casefold())
```

15. `.center()` - metodi satrni belgilangan uzunlikdagi joyga joylashtiradi va o'rtaga qo'yadi. `.center()` yordamida satrning o'rtasiga joylashtirilgan matnning ikki tomoniga belgilangan belgilar yoki bo'shliqlar qo'shish mumkin.

Bu metod `2` ta argument qabul qiladi: 

```python
text.center(length, character)
```

- `length` - natijada hosil bo'ladigan satrning umumiy uzunligini belgilaydi.
- `character`(ixtiyoriy) - to'ldiriladigan belgi. Agar ko'rsatilmasa, bo'shliq (`" "`) belgisi qo'llaniladi.

```python
text = "Python"
print(text.center(12, '*'))
```
Yuqoridagi misolda, `Python` so'zi umumiy uzunligi `12` bo'lgan satrga joylashtirildi va uning ikki tomoniga `*` belgisi qo'shildi. Bu metod, matnni tartib bilan joylashtirish yoki dizayn berish kabi holatlarda qo'l keladi.


16. `.count()` - metodi matn ichida belgilar necha marta uchrashini hisoblab beradi. Bu metod, matn ichida maxsus so'zlar yoki belgilar sonini topishga qulay.

Bu metod `3` ta argument qabul qiladi: 

```python
text.count(substring, start, end)
```
- `substring` - matn ichida necha marta uchrashini tekshiriladigan argument.
- `start`(ixtiyoriy) - qidirishni qayerdan boshlash kerakligini bildiradi.
- `end`(ixtiyoriy) - Qidirishni qayerda tugatish kerakligini bildiradi.

```python
matn = "Python dasturlash tilini o'rganish juda qiziqarli, chunki Python juda kuchli."
soni = matn.count("Python")
print(soni)
```

**Natija:** `2` chiqadi, chunki `Python` 2 marta uchragan.

Yuqoridagi misolda, `.count()` metodi `Python` so'zi matn ichida necha marta uchraganini hisoblab beradi. 

17. `.encode()` - metodi matnni belgilangan kodlash (`encoding`) formatida kodlash uchun ishlatiladi. Bu metod, ayniqsa, turli kodlash tizimlari bilan ishlashda yoki matnni boshqa formatga o'tkazishda yordam beradi.

Bu metod `2` ta argument qabul qiladi: 

```python
matn.encode(encoding, errors)
```

- `encoding` - Kodlash formatini belgilaydi. Masalan, `utf-8`, `ascii`, `utf-16`, va hokazo.
- `errors`(ixtiyoriy) - Xatolik yuz berganda qanday choralar ko'rilishi kerakligini belgilaydi. Eng ko'p ishlatiladigan qiymatlar:
  - `strict` -  Xatolik yuz berganda `UnicodeDecodeError` xatosini chiqaradi.
  - `ignore` - Xatoliklarni e'tiborsiz qoldiradi.
  - `replace` - Xatoliklar o'rniga savol belgisi (`?`) qo'yadi.

```python
text = "Salom Dunyo!"
print(text.encode('utf-8'))
```
Yuqoridagi misolda, `.encode()` metodi `Salom Dunyo!` matnini `UTF-8` formatida kodlaydi. Natija baytlar (`bytes`) shaklida chiqariladi, ya'ni `b` prefiksi bilan ko'rsatiladi. Bu metod asosan matnlarni turli tizimlarga yuborish yoki saqlash uchun tayyorlashda ishlatiladi.

18. `.expandtabs()` - metodi `\t` **tab** belgisini belgilangan bo'sh joylarga almashtiradi. Ushbu metodda siz **tab** kengligini belgilashingiz mumkin, bu esa har bir `\t` belgisi qancha bo'sh joy bilan almashtirilishini belgilaydi.

Bu metod `1` ta argument qabul qiladi: 

```python
string.expandtabs(tabsize=8)
```

- `tabsize`(ixtiyoriy): `\t` belgisi uchun bo'sh joylar soni. Standart qiymat `8` ga teng.

Ushbu metod stringning nusxasini qaytaradi, bunda `\t` belgilari berilgan tabsize bo'yicha bo'sh joylarga almashtiriladi.

```python
text = "Hello\tworld"
result = text.expandtabs(4)
print(result)
```
Bu misolda `\t` belgisi `4` ta bo'sh joy bilan almashtiriladi.

19. `.format()` - metodi Pythonda stringlarni shakllantirish uchun ishlatiladi. Bu metod orqali string ichidagi o'rinlarni kerakli qiymatlar bilan to'ldirish mumkin.

- Syntax
```python
"{} va {}".format(qiymat1, qiymat2)
```
- `{}` - Bu joy to'ldirilishi kerak bo'lgan o'rinlarni bildiradi.
- `.format(qiymat1, qiymat2)` - Har bir `{}` uchun tegishli qiymatlarni berib, `string` ichiga qo'yadi.

1. **Oddiy formatlash:**

```python
name = "Umid"
age = 20
text = "Mening ismim {} va yoshim {} da.".format(name, age)
print(text)
```
**Result:** `Mening ismim Umid va yoshim 20 da.`

2. **Indekslar bilan formatlash:**

```python
text = "Bu yerda {0} va {1} bor. {0} eng mashhuri.".format("kitob", "qalam")
print(text)
```
**Result:** `Bu yerda kitob va qalam bor. kitob eng mashhuri.`

3. **Kalit so'zlar bilan formatlash:**

```python
text = "{ism}ning yoshi {yosh} da.".format(ism="Umid", yosh=20)
print(text)
```
**Result:** `Umidning yoshi 20 da.`

4. **Sonlarni formatlash:**

```python
text = "O'rtacha baho: {:.2f}".format(85.4567)
print(text)
```
**Result:** `O'rtacha baho: 85.46`

20. `.format_map()` metodi `dictionary` asosida matnni `placeholder` bilan formatlash uchun ishlatiladi. Bu `str.format()` ga o'xshash bo'lib, lekin to'g'ridan-to'g'ri argumentlarni qabul qilish o'rniga, lug'atni ishlatadi va `placeholder` o'rniga qiymatlarni qo'yadi.

**Syntax:**
```python
string.format_map(dictionary)
```
**Example:**
```python
# Dictionary with values to replace placeholders
info = {"name": "Umid", "age": 25}

# Using format_map to replace placeholders
result = "My name is {name} and I am {age} years old.".format_map(info)

print(result)
```
**Result:**
```shell
My name is Umid and I am 25 years old.
```
- Key Points
  - `.format_map()` katta hajmdagi lug'atlar bilan yaxshi ishlaydi va samarador.
  - Agar `dictionary`da `placeholder` qiymati bo'lmasa, `.format_map() KeyError` xatosini chiqaradi. Buning oldini olish uchun `collections.defaultdict` kabi maxsus lug'at `class`ni ishlatish mumkin.

`.format_map()` va yetishmayotgan kalitlar bilan ishlash
Agar ba'zi `key`lar mavjud bo'lmasa va xato chiqmasligini istasangiz, `collections.defaultdict` dan foydalanishingiz mumkin:

```python
from collections import defaultdict

# Kalitlar yo'q bo'lganda standart qiymat qaytaradigan lug'at
info = defaultdict(lambda: "noma'lum", name="Umid")

result = "Mening ismim {name} va men {age} yoshdaman.".format_map(info)
print(result)
```
**Natija:**
```shell
Mening ismim Umid va men noma'lum yoshdaman.
```

21. `.index()` metodi matn ichida `belgilangan qism` yoki `substring` qaysi indeksdan boshlanishini topish uchun ishlatiladi. Agar kiritilgan qism matn ichida topilsa, u holda uning birinchi uchragan indeksini qaytaradi. Topilmasa, `ValueError` xatosini chiqaradi.

**Syntax:**
```python
string.index(substring, [start], [end])
```
- substring - qidirilayotgan substring (matn qismi).
- start(optional) - qidiruvni qaysi indeksdan boshlash kerakligini belgilaydi.
- end(optional) -  qidiruvni qaysi indeksgacha qilish kerakligini belgilaydi.

```python
text = "Hello, Python programming language!"

# 'Python' qismi qaysi indeksdan boshlanishini topish
index = text.index("Python")
print("Index:", index)
```
**Result:**
```shell
Indeks: 7
```
Specifying `start` and `end` indexes
```python
text = "Learning programming languages is interesting."

# 'til' qismi 10-indeksdan boshlab qidirilmoqda
index = text.index("lang", 10)
print("Index:", index)
```
**Result:**
```shell
Indeks: 11
```

- **Key Points**
  - Agar substring topilmasa, `ValueError` xatosi chiqadi.
  - `.index()` faqat `substring`ning birinchi uchragan joyini qaytaradi, shuning uchun bir nechta bir xil qismlar mavjud bo'lsa, faqat `eng birinchi` index beriladi.



## NUMBER

- **Number** - Raqamli ma'lumot turi `2` ga bo'linadi:
    - **Integer(int)** - Butun sonlarni ifodalaydi. Masalan: `10`, `-3`, `42`.

Integer ma'lumot turi butun sonlarni ifodalaydi. Bu sonlar `manfiy`, `musbat` yoki `0` bo'lishi mumkin. Integerlar cheklanmagan uzunlikka ega, ya'ni Python juda katta sonlarni ham integer sifatida saqlay oladi.

```python
x = 10
y = -5
z = 0
a = 12345678901234567890

print(type(x))  # <class 'int'>
print(type(y))  # <class 'int'>
print(type(z))  # <class 'int'>
print(type(a))  # <class 'int'>
```
### INTEGER USTIDA AMALLAR
Integerlar ustida asosiy matematik amallarni bajarish mumkin:
```python
a = 10
b = 3

print(a + b)  # Qo'shish: 13
print(a - b)  # Ayirish: 7
print(a * b)  # Ko'paytirish: 30
print(a / b)  # Bo'lish: 3.3333333333333335
print(a // b) # Butun qismini olish: 3
print(a % b)  # Qoldiqni olish: 1
print(a ** b) # Darajaga ko'tarish: 1000
```

### UZUN SONLARNI KIRITISH
Uzun sonlarni kiritishda, qulaylik uchun, raqamlarni pastki chiziq (`_`) yordamida guruhlash mumkin. Python - son tarkibidagi pastki chiziqlarni (`_`) inobatga olmasdan, uzun sonligicha qabul qiladi.

```python
aholi_soni = 7_594_000_000 # o'qishga qulay bo'lishi uchun shunaqa ko'rinishda yozdik
print("Yer sharida", aholi_soni, "ga yaqin odam yashaydi")
```

### KONSTANTA

Aksar dasturlash tillarida `konstant` qiymatlar tushunchasi bor. Konstantlar o'zgarmas bo'ladi (misol uchun `π` ning qiymati konstant, o'zgarmas qiymat). Pythonda konstant tushunchasi yo'q, shuning uchun dasturchilar bunday o'zgaruvchilarning nomini katta harflar bilan yozadilar (`ogohlantirish sifatida`). Bu albatta qat'iy qonun emas, lekin kelajakda o'zgaruvchilar orasida konstant qiymatlarni ajratish uchun yaxshi usul.

```python
PI = 3.14159
radius = 20.7
```

### BIR NECHTA O'ZGARUVCHIGA QIYMAT BERISH
Birdaniga bir nechta o'zgaruvchiga qiymat berish uchun o'zgaruvchilar va ularga mos qiymatlar vergul (`,`) bilan ajratiladi:
```python
x, y, z = 10, -7.25, -30
```

### O'ZGARUVCHI TURINI ALMASHTIRISH

Python dasturlash tilida o'zgaruvchilar turini bir ma'lumot turidan boshqa ma'lumot turiga o'zgartirish jarayoni `type casting` deb ataladi.

#### integerdan floatga o'zgartirish

```python
x = 10
y = float(x)  # 10.0

print(type(y))  # <class 'float'>
print(y)        # 10.0
```

#### floatdan integerga o'zgartirish
> [!NOTE]
> Floatni Integerga o'zgartirishda kasr qismini olib tashlaydi.

```python
x = 3.14
y = int(x)  # 3

print(type(y))  # <class 'int'>
print(y)        # 3
```

#### stringdan integerga o'zgartirish

> [!CAUTION]
> stringni integerga o'zgartirish uchun string faqat `raqamlarni` o'z ichiga olishi kerak.

```python
s = "123"
x = int(s)  # 123

print(type(x))  # <class 'int'>
print(x)        # 123
```

#### integerdan stringga o'zgartirish

```python
x = 123
s = str(x)  # "123"

print(type(s))  # <class 'str'>
print(s)        # "123"
```

#### floatdan stringga o'zgartirish

```python
x = 3.14
s = str(x)  # "3.14"

print(type(s))  # <class 'str'>
print(s)        # "3.14"
```

### input()
Foydalanuvchidan ma'lumot olish uchun `input()` funksiyasidan foydalanamiz:

```python
ism = input("Ismingizni kiriting: ")
print(ism)
```

Yuqoridagi kodda foydalanuvchidan ism kiritishini so'radik va kiritilgan ismni terminalga chiqardik.

Input funksiyasidan foydalanishni o'rgandik, endi shu funksiya yordamida foydalanuvchidan son olishni o'rganamiz:

```python
#1 foydalanuvchining tug'ilgan yilini so'raymiz
t_yil = input("Tug'ilgan yilingizni kiriting: ")
#2 foydalanuvchi yoshini xisoblaymiz
yosh = 2020 - t_yil # 
#3 foydalanuvchi yoshini konsolga chiqaramiz
print("Siz " + yosh + " yoshda ekansiz")
```

- **Floating Point(float)** - O'nlik sonlarni ifodalaydi. Masalan: `3.14`, `-2.7`,` 0.99`.

> [!NOTE]
> Pythonda o'nlik sonlar `floating point numbers` yoki qisqa qilib `floats` deyiladi. Ingliz tilida o'nlik sonlarni yozishda vergul (`,`) emas nuqta (`.`) belgisi ishlatiladi, va bu nuqta sonning katta kichikligiga qarab joyi o'zgargani uchun `"floating"` deyiladi.

```python
pi = 3.14159 # o'nlik son (float)
radius = 10  # butun son (integer)
diametr = 2*radius
print("Aylana uzunligi ", pi*diametr, " ga teng.")
```

- Pythonda `sequence types` (ketma-ketlik) ma'lumot turlari turli xil elementlarni tartiblangan shaklda saqlash uchun ishlatiladi. Asosiy `sequence` turlari quyidagilar:
    - **List(list):** Tartiblangan va o'zgaruvchan ma'lumotlar to'plami. Masalan: `my_list = [1, 'Hello', True, '5.6']`
    - **Tuple(tuple):** Tartiblangan, lekin o'zgarmas ma'lumotlar to'plami. Masalan: `my_tuple = (1, 2, 3, 4, 5)`
    - **Range(range):** `Ketma-ket` sonlar intervalini ifodalaydi. Masalan: `range(1, 11)`
- Pythonda `mapping types` ma'lumot turi `kalit-qiymat` juftlari ko'rinishida ma'lumotlarni saqlash uchun ishlatiladi. Pythonda asosiy mapping ma'lumot turi bu **dictionary(dict)** hisoblanadi. `Dictionary` - kalit (`key`) va qiymat (`value`) juftlaridan tashkil topgan tartibsiz ma'lumotlar to'plami.
- Pythonda `set` - bu unikal elementlar to'plami bo'lib, `tartibsiz` va `indekslanmagan` holda saqlanadi. `Set` ma'lumot turi `duplikat` elementlarni o'z ichiga olmaydi va asosiy foydalanish maqsadi to'plam operatsiyalarini bajarish (`union`, `intersection`, `difference` va boshqalar) hisoblanadi.
    - Pythonda frozenset `o'zgarmas set` ma'lumot turi bo'lib, setning barcha xususiyatlariga ega, lekin elementlari yaratilgandan so'ng o'zgartirilmaydi.
- Pythonda `boolean(bool)` ma'lumot turi ikkita qiymatni ifodalaydi: `True` va `False`. `Boolean` ma'lumot turi mantiqiy ifodalarni baholash va shartli tekshiruvlarni amalga oshirish uchun ishlatiladi. 
- Pythonda `binary` ma'lumot turlari ikkilik (`binary`) ma'lumotlar bilan ishlash uchun ishlatiladi. Asosiy `binary` ma'lumot turlari quyidagilardan iborat:
    - **bytes:** O'zgarmas ikkilik ma'lumotlar to'plami.
    - **bytearray:** O'zgaruvchan ikkilik ma'lumotlar to'plami.
    - **memoryview:** Mavjud ikkilik ma'lumotlarni ko'rish va manipulyatsiya qilish imkonini beradi.

## AMALIYOT
1. O‘zgaruvchilar bilan arifmetik amallar
    - Quyidagi arifmetik amallarni bajarish uchun o‘zgaruvchilarni yarating:
        - `a` degan o'zgaruvchi yarating va unga `8` qiymat bering
        - `b` degan o'zgaruvchi yarating va unga `3` qiymat bering
        - Ularning `yig'indisi`, `ayirmasi`, `ko‘paytmasi` va `bo‘linmasi`ni hisoblang.

**Natija:** <br>
```python
Qo‘shish: 11
Ayirish: 5
Ko‘paytirish: 24
Bo‘lish: 2.6666666666666665
```

2. O‘zgaruvchi qiymatini almashtirish
    - `m` degan o'zgaruvchi yarating va unga `15` qiymat bering
    - `n` degan o'zgaruvchi yarating va unga `25` qiymat bering
    - Ularning qiymatlarini almashtiring, ya’ni `m` ning qiymatini `n` ga, `n` ning qiymatini esa `m` ga o‘tkazing.

**Natija:** <br>
```python
m = 25
n = 15
```
3. O‘zgaruvchi turlarini o‘zgartirish
    - Quyidagi ko‘rsatmalarga asosan o‘zgaruvchi turlarini o‘zgartiring:
        - `s` degan o'zgaruvchi yarating, unga `"123"` qiymat bering va butun songa o'zgartiring.
        - `r` degan o'zgaruvchi yarating, unga `"45.67"` qiymat bering va float turiga o'zgartiring
        - `q` degan o'zgaruvchi yarating, unga `"78.9"` qiymat bering va float turidan butun songa o'zgartiring.
        
**Natija:** <br>
```python
s = 123
r = 45.67
q = 78
```

4. O‘zgaruvchi uzunligini aniqlash
    - String o‘zgaruvchi yaratib, uning uzunligini aniqlang:
    - `matn` degan o'zgaruvchi yarating va unga `"Hello World!"` qiymatini bering.
    - Ushbu matnning `uzunligini` aniqlang va terminalga chiqaring.

**Natija:** <br>
```python
Matn uzunligi: 12
```

5. Topshiriq: Ikki raqamni qo'shish
    - `raqam1` degan o'zgaruvchi yarating va unga `"5"` qiymat bering.
    - `raqam2` degan o'zgaruvchi yarating va unga `"5.5"` qiymat bering.
    - Berilgan ikkita raqamni (`int` yoki `float`) qo'shing va natijani terminalga chiqarib bering.

**Natija:** <br>
```python
Natija: 9.5
```