# 应用：猜拳游戏
'''
1. 出拳
    玩家：手动输入
    电脑：1、固定：剪刀 2、随机
2. 判断输赢
    2.1 玩家获胜
    2.2 平局
    2.3 电脑获胜
'''

#1. 出拳
# 玩家
player=int(input('请出拳：0--石头：1--剪刀：2--布'))
#电脑
import random
computer=random.randint(0,2)

#2.增加玩家与电脑的出拳显示
if player==0:
    print('玩家出的是：石头')
elif player==1:
    print('玩家出的是：剪刀')
elif player==2:
    print('玩家出的是：布')

if computer==0:
    print('电脑出的是：石头')
elif computer==1:
    print('电脑出的是：剪刀')
elif computer==2:
    print('电脑出的是：布')

#3. 判断输赢
if (player==0 and computer==1) or (player==1 and computer==2) or (player==2 and computer==0):
    print('玩家获胜了，呵')
elif (player==1 and computer==0) or (player==2 and computer==1) or (player==0 and computer==2):
    print('电脑获胜了')
elif player == computer:
    print('平局，再来一局')
    