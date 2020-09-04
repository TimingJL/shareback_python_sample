# -*- coding: UTF-8 -*-

# 輸入出生年，輸出生肖

# 2020 -> 鼠年
# 2020 % 12 = 4
# 4, 5, 6, 7, 8, 9, 10, 11, 0, 1, 2, 3

year = int(input("請輸入要查詢的西元年："))

zodiacIndex = year % 12

if (zodiacIndex == 4):
    print('鼠')
if (zodiacIndex == 5):
    print('牛')
if (zodiacIndex == 6):
    print('虎')
if (zodiacIndex == 7):
    print('兔')
if (zodiacIndex == 8):
    print('龍')
if (zodiacIndex == 9):
    print('蛇')
if (zodiacIndex == 10):
    print('馬')
if (zodiacIndex == 11):
    print('羊')
if (zodiacIndex == 0):
    print('猴')
if (zodiacIndex == 1):
    print('雞')
if (zodiacIndex == 2):
    print('狗')
if (zodiacIndex == 3):
    print('豬')
