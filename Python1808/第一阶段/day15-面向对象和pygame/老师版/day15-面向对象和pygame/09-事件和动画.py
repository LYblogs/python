"""__author__ = 余婷"""
import pygame
from color import Color

pygame.init()
window = pygame.display.set_mode((400, 600))
window.fill((255, 255, 255))

# 在这儿写的代码是静态的(界面上的内容)
x = 100
y = 100
width = 100
height = 80
pygame.draw.rect(window, Color.green, (x, y, width, height))

pygame.display.flip()

while True:

    y += 3
    # width -= 2
    window.fill(Color.white)  # 覆盖原来的状态
    pygame.draw.rect(window, Color.rand_color(), (x, y, width, height))
    pygame.display.update()   # 重新显示

    # 有事件产生的时候才会进入for循环
    for event in pygame.event.get():
        # 1.type属性
        """
        不同的type值对应不同类型的事件
        QUIT - 关闭按钮被点击事件
        
        a.鼠标相关事件  - 按的位置
        MOUSEMOTION - 鼠标移动
        MOUSEBUTTONDOWN - 鼠标按下
        MOUSEBUTTOUP - 鼠标弹起
        
        event.pos - 获取鼠标事件产生的位置
        
        b.键盘事件 - 按的是哪个键
        KEYDOWN - 按键按下
        KEYUP - 按键弹起
        
        event.key - 被按的键对应的字符的编码值
        
        """
        if event.type == pygame.QUIT:
            exit()

        elif event.type == pygame.MOUSEMOTION:
            # print('鼠标移动', event.pos)
            # pygame.draw.circle(window, Color.rand_color(), event.pos, 30)
            # pygame.display.flip()
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 鼠标按下要做什么就写在这儿
            print('鼠标按下', event.pos)
            pygame.draw.circle(window, Color.rand_color(), event.pos, 30)
            pygame.display.flip()
        elif event.type == pygame.MOUSEBUTTONUP:
            print('鼠标弹起!', event.pos)

        elif event.type == pygame.KEYDOWN:
            print('按键按下')
            print(event.key, chr(event.key))

        elif event.type == pygame.KEYUP:
            print('按键弹起')
            print(event.key, chr(event.key))




