# -*- coding: UTF-8 -*-

game_title = """
  _            _         ___   __   _         _       
 | |   __ _ __| |_  _   / _ \ / _| | |   __ _| |_____ 
 | |__/ _` / _` | || | | (_) |  _| | |__/ _` | / / -_)
 |____\__,_\__,_|\_, |  \___/|_|   |____\__,_|_\_\___|
                 |__/                                 
"""

you_win = """
__  __               _       ___          ______
\ \/ /___  __  __   | |     / (_)___     / / / /
 \  / __ \/ / / /   | | /| / / / __ \   / / / / 
 / / /_/ / /_/ /    | |/ |/ / / / / /  /_/_/_/  
/_/\____/\__,_/     |__/|__/_/_/ /_/  (_|_|_)   
"""

print(game_title)

print("""
有一個樵夫不小心把銅斧頭掉進湖裡，這時候湖面浮出了一個女神，手上拿著金跟銀的斧頭，

女神:「請問這兩把斧頭哪把是你的？」
""")

answer = input("""
[A]: 金斧頭！
[B]: 銀斧頭！
[C]: 都不是！
你的答案是：""")

if (answer.upper() != 'C'):
    print("\n女神:「你這貪心的樵夫！！！別忘了斧頭還在我手上，去死吧！！！」\n樵夫：「啊啊啊啊啊！！！」\n\n")

if (answer.upper() == 'C'):
    print("\n女神:「你很誠實！我便將兩把斧頭連同銅斧頭都贈與你」\n")
    print(you_win)
