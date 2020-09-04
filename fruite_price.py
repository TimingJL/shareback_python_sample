# -*- coding: UTF-8 -*-

# 葡萄 350元/箱
# 火龍果 300元/箱
# 運費 170元/件
# 買四的倍數箱，免運，其他的要多算一件運費(shipping fee)

# 輸入水果數量，輸出價錢

number_of_grapes = int(input('葡萄需要幾箱：'))
number_of_dragon_fruit = int(input('火龍果需要幾箱：'))

price_of_grapes = (number_of_grapes * 350) + \
                  (1 if (number_of_grapes % 4) > 0 else 0) * 170

price_of_dragon_fruit = (number_of_dragon_fruit * 300) + \
                        (1 if (number_of_dragon_fruit % 4) > 0 else 0) * 170

total_price = price_of_grapes + price_of_dragon_fruit

print('總共 {} 元\n'.format(total_price))
