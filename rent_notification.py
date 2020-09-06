# -*- coding: UTF-8 -*-
import requests
import time
from datetime import datetime

# 與室友合租公寓，需要定時跟室友催房租，收齊繳交給房東，寫一支每月固定日期催繳房租的 Line Notify 吧～
# 規格：希望每個月的 10 ~ 20 日每天早上 08:00 傳送訊息到群組，提醒大家繳交房租


def sendMessage(message):
    event = 'xxx'  # The Event Name you set on the IFTTT
    key = 'xxx'  # The key from Webhooks settings on the IFTTT

    ifttt_url = 'https://maker.ifttt.com/trigger/{event}/with/key/{key}?value1={message}' \
        .format(event=event, key=key, message=message)

    try:
        requests.get(ifttt_url)
    except requests.exceptions.RequestException as e:
        print(e)
        raise SystemExit(e)


one_hour = 60 * 60  # 3600 secs is one hour
has_today_send_message = False  # 「今天是否已經發送過訊息」

while True:
    time_now = datetime.now()                           # 取得當下時間
    if (time_now.day >= 10 and time_now.hour <= 20):    # 檢查今天是否在每月 10 ~ 20 日之內
        if (not has_today_send_message):                # 檢查今天是否已經發送過提醒訊息?若還沒，則發送訊息
            sendMessage("""
            今天是{month}月{day}日，
            距離繳房租期限還剩下{days_left}天，
            請大家把握時間，按時繳房租！謝謝！
            """.format(month=time_now.month, day=time_now.day, days_left=(20 - time_now.day)))
            has_today_send_message = True   # 發送玩訊息之後，設為「已經發送過訊息」
        if (has_today_send_message):        # 若今天已經發送過訊息了
            if (time_now.hour == 0):        # 等到凌晨12點，將「今天是否已經發送過訊息」設為「否」
                has_today_send_message = False

    time.sleep(one_hour)                    # 暫停一小時(亦即，每小時檢查一次)
