import pygame
#1.游戏初始化
pygame.init()


#2.创建游戏窗口
"""
set_mode(窗口的大小) - 窗口大小是元组，有两个元素，分别是：width，height
set_mode(（宽度，高度）)
宽度和高度的单位是像素
"""
window =pygame.display.set_mode((400,600))
#将窗口填充成不同的颜色
"""
fill(颜色)
计算机颜色：计算机三原色 - 红，绿，蓝（rgb）
            颜色值就是由三个数字组成，分别代表红，绿，蓝，数字范围是：0-255

python中的颜色是一个元组，元组有三个颜色，分别是r，g，b
（255,255,255）
（0,0,0）
（255,0,0）
"""
window.fill((255 ,200,200))

#将窗口显示到设备上
pygame.display.flip()

#3.创建游戏循环
while True:
    # 4.检测事件
    for event in pygame.event.get():
        #5.区分不同的事件，做出不同的反应
        if event.type ==pygame.QUIT:
            exit() #程序结束

