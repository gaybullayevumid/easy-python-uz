# import requests
#
# # Biror web sahifaga so'rov jo'natish
# response = requests.get('https://jsonplaceholder.typicode.com/posts')
#
# # Javob ma'lumotlarini olish
# if response.status_code == 200:
#     data = response.json()  # Ma'lumotni JSON formatida olish
#     print(data[5])  # Birinchi postni chop etish
# else:
#     print('So\'rov muvaffaqiyatsiz bo\'ldi.')


# import numpy as np
#
# # 1 dan 10 gacha bo'lgan sonlar bilan massiv yaratish
# arr = np.arange(1, 11)
#
# # Massivdagi barcha elementlarning kvadratini hisoblash
# squares = arr ** 2
#
# print("Asl massiv:", arr)
# print("Kvadratlar:", squares)

#
# import matplotlib.pyplot as plt
#
# # Ma'lumotlar
# x = [1, 2, 3, 4, 5]
# y = [10, 20, 25, 30, 40]
#
# # Grafikni chizish
# plt.plot(x, y, marker='o')
#
# # Grafik nomlari
# plt.title('Oddiy Grafik')
# plt.xlabel('X o\'qi')
# plt.ylabel('Y o\'qi')
#
# # Grafikni ko'rsatish
# plt.show()

#
# import pandas as pd
#
# # Jadval yaratish
# data = {
#     'Ism': ['Umid', 'Ali', 'Sarvar'],
#     'Yosh': [23, 35, 29],
#     'Kasb': ['Dasturchi', 'Muallim', 'Menejer']
# }
#
# df = pd.DataFrame(data)
#
# # Jadvalni ko'rish
# print(df)
#
# # Faqat Ism ustunini chiqarish
# print(df['Ism'])
#
# # Yosh bo'yicha filtrlash
# print(df[df['Yosh'] > 25])


#
# import requests
# from bs4 import BeautifulSoup
#
# # Web sahifa so'rovi
# url = "https://www.example.com"
# response = requests.get(url)
#
# # Sahifani pars qilish
# soup = BeautifulSoup(response.text, 'html.parser')
#
# # Sahifadagi barcha <a> teglarini topish
# links = soup.find_all('a')
#
# # Har bir linkni chop etish
# for link in links:
#     print(link.get('href'))

#
# from flask import Flask
#
# # Flask ilovasini yaratish
# app = Flask(__name__)
#
# # Bosh sahifa uchun view funksiyasi
# @app.route('/')
# def home():
#     return "Hello world"
#
# # Ilovani ishga tushirish
# if __name__ == '__main__':
#     app.run(debug=True)

# # test_mening_funksiyam.py faylida
# def ikki_barobar(qiymat):
#     return qiymat * 2
#
# def test_ikki_barobar():
#     assert ikki_barobar(3) == 6
#     assert ikki_barobar(0) == 0
#     assert ikki_barobar(-2) == -4
#
# # Testlarni ishga tushirish uchun terminalda:
# # pytest

