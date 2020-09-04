# -*- coding: UTF-8 -*-

# 輸入出生年，輸出生肖

# 2020 -> 鼠年
# 2020 % 12 = 4
# 4, 5, 6, 7, 8, 9, 10, 11, 0, 1, 2, 3

languageOption = input("""
<請輸入語言偏好(Language Setting)>
(A) 中文
(B) English
：""")

languageDict = {
    'A': 'zh-tw',
    'B': 'en',
}

language = languageDict[languageOption.upper()]

zodiacDict = {
    'zh-tw': {
        'input_label': '請輸入年份',
        'zodiac_list': ['鼠', '牛', '虎', '兔', '龍', '蛇', '馬', '羊', '猴', '雞', '狗', '豬'],
    },
    'en': {
        'input_label': 'Please enter the year',
        'zodiac_list': ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig'],
    },
}

year = int(input(zodiacDict[language]['input_label'] + ': '))

print(zodiacDict[language]['zodiac_list'][(year - 4) % 12])
