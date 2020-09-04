# -*- coding: UTF-8 -*-

GAME_TITLE = """
 ██████╗  ██████╗ ██╗  ██╗██╗  ██╗     ██████╗  █████╗ ███╗   ███╗███████╗
██╔═══██╗██╔═══██╗╚██╗██╔╝╚██╗██╔╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██║   ██║██║   ██║ ╚███╔╝  ╚███╔╝     ██║  ███╗███████║██╔████╔██║█████╗  
██║   ██║██║   ██║ ██╔██╗  ██╔██╗     ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
╚██████╔╝╚██████╔╝██╔╝ ██╗██╔╝ ██╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
 ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
"""
print(GAME_TITLE)

tictactoe = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
player_list = ['O', 'X']

TIC_TAC_TOE_MAP = """
   |   |
 {} | {} | {}
___|___|___
   |   |
 {} | {} | {}
___|___|___
   |   |
 {} | {} | {}
   |   |

"""

init_map = TIC_TAC_TOE_MAP.format(
    tictactoe[0],
    tictactoe[1],
    tictactoe[2],
    tictactoe[3],
    tictactoe[4],
    tictactoe[5],
    tictactoe[6],
    tictactoe[7],
    tictactoe[8]
)

print(init_map)

tictactoe = [' '] * 9

isPlaying = True
player = 0

while isPlaying:
    print('現在輪到玩家「{}」'.format(player_list[player]))
    print('輸入 1 ~ 9 選擇要下棋的位置\n')
    value = int(input("請輸入您選擇的位置："))
    tictactoe[value - 1] = player_list[player]
    player = (player + 1) % len(player_list)
    updated_map = TIC_TAC_TOE_MAP.format(
        tictactoe[0],
        tictactoe[1],
        tictactoe[2],
        tictactoe[3],
        tictactoe[4],
        tictactoe[5],
        tictactoe[6],
        tictactoe[7],
        tictactoe[8]
    )
    print(updated_map)
