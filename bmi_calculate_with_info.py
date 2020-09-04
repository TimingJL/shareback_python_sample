# -*- coding: UTF-8 -*-

# BMI Ref:
# https://health99.hpa.gov.tw/onlinkhealth/onlink_bmi.aspx

height = float(input('請輸入身高(cm)：')) / 100  # translate cm to m
weight = float(input('請輸入體重(kg)：'))
body_status = ''

BMI = round(weight / (height ** 2), 2)

if (BMI < 18.5):
    body_status = '體重過輕'

if (BMI >= 18.5 and BMI < 24):
    body_status = '健康體位'

if (BMI >= 24 and BMI < 27):
    body_status = '過重'

if (BMI >= 27 and BMI < 30):
    body_status = '輕度肥胖'

if (BMI >= 30 and BMI < 35):
    body_status = '中度肥胖'

if (BMI >= 35):
    body_status = '重度肥胖'

print('\n你的 BMI 是：{}'.format(BMI))
print('成人肥胖定義：{}\n'.format(body_status))
