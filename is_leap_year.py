# -*- coding: UTF-8 -*-

# 公元年分非4的倍數，為平年，或
# 公元年分為4的倍數但非100的倍數，為閏年，或
# 公元年分為100的倍數但非400的倍數，為平年，或
# 公元年分為400的倍數但非3200的倍數，為閏年，或
# 公元年分為3200的倍數但非80000年的倍數，為平年，或
# 公元年分為80000的倍數為閏年。

year = int(input("請輸入年份："))
is_leap_year = False

if year % 4 == 0 and year % 100 != 0:
    is_leap_year = True
elif year % 400 == 0:
    is_leap_year = True
else:
    is_leap_year = False

is_leap_year_text = '閏年' if is_leap_year else '平年'

print(is_leap_year_text)
