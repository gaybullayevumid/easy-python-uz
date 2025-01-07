# Variable Names

O'zgaruvchilarga nom berishda quyidagi qoidalarga amal qiling:

> [!CAUTION]
> - O'zgaruvchi nomi harf yoki pastki chiziq (`_`) bilan boshlanishi kerak.
> - O'zgaruvchi nomi raqam bilan boshlanishi mumkin emas
> - O'zgaruvchi nomida faqatgina lotin alifbosi harflari (`A-z`), raqamlar (`0-9`) va pastki chiziq (`_`) qatnashishi mumkin
> - O'zgaruvchi nomida bo'shliq (`пробел`) bo'lishi mumkin emas
> - O'zgaruvchi nomida katta-kichik harflar turlicha talqin qilinadi (`ism`, `ISM`, va `Ism` uchta turli o'zgaruvchi)

```python
2myvar = "John"
my-var = "John"
my var = "John"
```


- Qo'shimcha qoidalar:
  - O'zgaruvchi nomini kichik harflar bilan yozing.
  - O'zgaruvchi nomida 2 va undan ortiq so'z qatnashsa ularning orasini pastki chiziq (`_`) bilan ajrating (`ism_sharif="Umid G'aybullayev"`).
  - O'zgaruvchiga tushunarli nom bering (`y=20` emas `yosh=20`, `d="Korea"` emas `davlat = "Korea"` va hokazo).
  - Shuningdek o'zgaruvchilarga Pythonda ishlatiladigan funksiyalar va maxsus kalit so'zlarning(keywords) nomini bermang.

```python
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
```

Kalit so'zlar ro'yhatini ko'rish uchun python faylga uyidagi kodni yozamiz:

```python
import keyword
print(keyword.kwlist)
```