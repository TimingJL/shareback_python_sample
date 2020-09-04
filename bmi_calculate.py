# -*- coding: UTF-8 -*-

# BMI Ref:
# https://health99.hpa.gov.tw/onlinkhealth/onlink_bmi.aspx

height = float(input('請輸入身高(cm)：')) / 100  # translate cm to m
weight = float(input('請輸入體重(kg)：'))

BMI = weight / (height ** 2)

print('\n你的 BMI 是：{}\n\n'.format(BMI))
