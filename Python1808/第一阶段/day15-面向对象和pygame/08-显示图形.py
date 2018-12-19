import pygame
from color import Color
import math
#======游戏最小系统=======
#1.游戏初始化
pygame.init()
#2.创建游戏窗口
window =pygame.display.set_mode((400,600))
#将窗口填充成不同的颜色
window.fill((255 ,200,200))
#=========显示图形========
#1.画直线
"""
line(画在哪，什么颜色,起点，终点，线宽度)

"""
# pygame.draw.line(window,Color.blue,(0,0),(100,100),5)
"""
lines(画在哪，线的颜色，是否闭合，点列表)
依次连接点列表中所有的点(是否闭合决定是否连接起点和终点)
"""
points =[(10,10),(100,70),(100,170),(40,230),(40,320)]
pygame.draw.lines(window,Color.blue,True,points)
#2.画圆
"""
circle(画在哪，颜色，圆心坐标，半径，线宽)
"""
pygame.draw.circle(window,Color.green,(200,300),200,5)

#3.画弧线
"""
arc(画在哪里，颜色，矩形，起始弧度，终止弧度，线宽=1)
矩形 - （x，y，width，height）: x,y是矩形左上角的坐标
width，height是矩形的宽高
"""
pygame.draw.arc()


#将窗口显示到设备上
pygame.display.flip()

#3.创建游戏循环
while True:
    # 4.检测事件
    for event in pygame.event.get():
        #5.区分不同的事件，做出不同的反应
        if event.type ==pygame.QUIT:
            exit() #程序结束

