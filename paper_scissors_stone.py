# -*- coding: UTF-8 -*-
# http://patorjk.com/software/taag
import random

# A     B
# 剪刀  剪刀
# 剪刀  石頭
# 剪刀  布

# 石頭  剪刀
# 石頭  石頭
# 石頭  布

# 布    剪刀
# 布    石頭
# 布    布

isExit = False

paper = '布'
scissors = '剪刀'
stone = '石頭'

optionsDict = {
    'A': scissors,
    'B': stone,
    'C': paper,
}

computerOptions = [scissors, stone, paper]

WORD_GAME_START = '''
  _______      ___      .___  ___.  _______         _______.___________.    ___      .______     .___________.
 /  _____|    /   \     |   \/   | |   ____|       /       |           |   /   \     |   _  \    |           |
|  |  __     /  ^  \    |  \  /  | |  |__         |   (----`---|  |----`  /  ^  \    |  |_)  |   `---|  |----`
|  | |_ |   /  /_\  \   |  |\/|  | |   __|         \   \       |  |      /  /_\  \   |      /        |  |     
|  |__| |  /  _____  \  |  |  |  | |  |____    .----)   |      |  |     /  _____  \  |  |\  \----.   |  |     
 \______| /__/     \__\ |__|  |__| |_______|   |_______/       |__|    /__/     \__\ | _| `._____|   |__|     
                                                                                                              
'''

WORD_YOU_WIN = '''
____    ____  ______    __    __     ____    __    ____  __  .__   __. 
\   \  /   / /  __  \  |  |  |  |    \   \  /  \  /   / |  | |  \ |  | 
 \   \/   / |  |  |  | |  |  |  |     \   \/    \/   /  |  | |   \|  | 
  \_    _/  |  |  |  | |  |  |  |      \            /   |  | |  . `  | 
    |  |    |  `--'  | |  `--'  |       \    /\    /    |  | |  |\   | 
    |__|     \______/   \______/         \__/  \__/     |__| |__| \__| 
                                                                       
'''

WORD_GAME_OVER = '''
  _______      ___      .___  ___.  _______      ______   ____    ____  _______ .______      
 /  _____|    /   \     |   \/   | |   ____|    /  __  \  \   \  /   / |   ____||   _  \     
|  |  __     /  ^  \    |  \  /  | |  |__      |  |  |  |  \   \/   /  |  |__   |  |_)  |    
|  | |_ |   /  /_\  \   |  |\/|  | |   __|     |  |  |  |   \      /   |   __|  |      /     
|  |__| |  /  _____  \  |  |  |  | |  |____    |  `--'  |    \    /    |  |____ |  |\  \----.
 \______| /__/     \__\ |__|  |__| |_______|    \______/      \__/     |_______|| _| `._____|
                                                                                             
'''


print(WORD_GAME_START)

while not isExit:
    computerOptionIndex = random.randint(0, len(computerOptions) - 1)

    option = input('猜拳遊戲： \n(A){0}\n(B){1}\n(C){2}\n(D)離開遊戲\n:'.format(
        scissors,
        stone,
        paper
    ))
    if option.upper() not in ['A', 'B', 'C', 'D']:
        print('\n\n')
        continue
    if (option.upper() == 'D'):
        break

    playerOption = optionsDict[option]
    computerOption = computerOptions[computerOptionIndex]
    print('\n電腦：{0} vs 玩家: {1}'.format(
        computerOption,
        playerOption)
    )
    if (playerOption == computerOption):
        print('平手\n\n')
        continue
    if (playerOption == scissors):
        if (computerOption == paper):
            print(WORD_YOU_WIN)
        if (computerOption == stone):
            print(WORD_GAME_OVER)
    if (playerOption == stone):
        if (computerOption == scissors):
            print(WORD_YOU_WIN)
        if (computerOption == paper):
            print(WORD_GAME_OVER)
    if (playerOption == paper):
        if (computerOption == stone):
            print(WORD_YOU_WIN)
        if (computerOption == scissors):
            print(WORD_GAME_OVER)
    print('\n\n')


print('感謝您！歡迎下次再來！')
