# Python OOP Tasks

1. Ta'lim classlari
   - `Student` classini yarating, unda `name`, `age`, va `grades` atributlari bo'lishi kerak. `grades` - bu o'quvchining baholari ro'yxati. `Student` classida quyidagi metodlar bo'lishi kerak:
     - **add_grade**(`grade`) - bahoni qo'shish.
     - **calculate_average()** - o'quvchining o'rtacha bahosini hisoblash.
     - **display_info()** - o'quvchi haqida ma'lumotlarni ko'rsatish.

```python
class Student:
    # Bu yerga kod yozing
```

2. O'quvchilarni nazorat qilish
   - `Course` classini yarating, unda `title`, `students` atributlari bo'lishi kerak. `students` - bu `Student` classidan iborat ro'yxat. `Course` classida quyidagi metodlar bo'lishi kerak:
     - **add_student**(`student`) - kursga o'quvchini qo'shish.
     - **remove_student**(`student`) - kursdan o'quvchini olib tashlash.
     - **display_students()** - kursdagi barcha o'quvchilarni ko'rsatish.

```python
class Course:
    # Bu yerga kod yozing
```

3. Kompyuter classini yaratish
   - `Computer` classini yarating, unda `brand`, `model`, va `price` atributlari bo'lishi kerak. `Computer` classida quyidagi metodlar bo'lishi kerak:
     - **display_info()** - kompyuter haqida ma'lumotlarni ko'rsatish.
     - **apply_discount**(`discount`) - kompyuter narxiga chegirma qo'llash.

```python
class Computer:
    # Bu yerga kod yozing
```

4. OOP o'yinlar
   - `Player` classini yarating, unda `name` va `score` atributlari bo'lishi kerak. `Player` classida quyidagi metodlar bo'lishi kerak:
     - **update_score**(`points`) - ballarni yangilash.
     - **display_score()** - o'yinchining ballini ko'rsatish.
   - Shuningdek, `Game` classini yarating, unda `players` atributi bo'lishi kerak. `Game` classida quyidagi metodlar bo'lishi kerak:
     - **add_player**(`player`) - o'yin davomida o'yinchini qo'shish.
     - **display_players()** - o'yindagi barcha o'yinchilarni ko'rsatish.

```python
class Player:
    # Bu yerga kod yozing

class Game:
    # Bu yerga kod yozing
```