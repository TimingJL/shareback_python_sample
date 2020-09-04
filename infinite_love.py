# -*- coding: UTF-8 -*-

do_you_love_me = False

answerDict = {
    'Y': True,
    'N': False,
}

while not do_you_love_me:
    answer = input("你愛我嗎？(Y/N): ")
    if (answer.upper() in ['Y', 'N']):
        do_you_love_me = answerDict[answer.upper()]

print('我也愛你，我們結婚吧～～～啾咪')
