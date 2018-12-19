"""__author__ = 余婷"""
import pygame
from color import Color
import math

# 游戏最小系统
pygame.init()
window = pygame.display.set_mode((400, 600))
window.fill((255, 255, 255))

# ======显示图形=========
# 1.画直线
"""
line(画在哪儿, 线的颜色, 起点, 终点, 线宽=1)
"""
pygame.draw.line(window, Color.green, (0, 0), (100, 100), 10)

"""
lines(画在哪儿, 线的颜色, 是否闭合, 点列表, 线宽=1)
依次连接点列表中所有的点（是否闭合决定是否连接起点和终点）
"""
points = [(10, 10), (100, 70), (100, 170), (40, 230), (40, 320)]
pygame.draw.lines(window, Color.red, True, points, 5)

# 2.画圆
"""
circle(画在哪儿, 颜色, 圆心坐标, 半径, 线宽=0)
注意：线宽为0的时候画实心圆
"""
pygame.draw.circle(window, Color.yellow, (100, 100), 80, 3)

# 3.画弧线
"""
arc(画在哪儿,颜色,矩形(Rect),起始弧度,终止弧度,线宽=1)
矩形 - (x, y, width, height)； x,y是矩形坐上角的坐标，width,height是矩形的宽高
"""
pygame.draw.arc(window, Color.blue, (150, 300, 50, 100), 0, math.pi, 10)


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()



