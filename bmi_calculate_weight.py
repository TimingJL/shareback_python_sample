# -*- coding: UTF-8 -*-

# BMI Ref:
# https://health99.hpa.gov.tw/onlinkhealth/onlink_bmi.aspx

height = float(input('請輸入身高(cm)：')) / 100  # translate cm to m

start_weight = round((height ** 2) * 18.5, 2)
end_weight = round((height ** 2) * 24, 2)

print('根據 BMI 指標，你的健康體重範圍是：{}kg ～ {}kg\n\n'.format(start_weight, end_weight))
