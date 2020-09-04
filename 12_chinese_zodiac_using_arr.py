# -*- coding: UTF-8 -*-

# 輸入出生年，輸出生肖

# 2020 -> 鼠年
# 2020 % 12 = 4
# 4, 5, 6, 7, 8, 9, 10, 11, 0, 1, 2, 3

year = int(input("請輸入要查詢的西元年："))

zodiacIndex = year % 12

zodiac = ['鼠', '牛', '虎', '兔', '龍', '蛇', '馬', '羊', '猴', '雞', '狗', '豬']

print(zodiac[(year - 4) % 12])
