"""__author__ = 余婷"""

import pygame

if __name__ == '__main__':
    pygame.init()
    window= pygame.display.set_mode((600, 400))
    window.fill((255, 255, 255))
    # 设置窗口标题
    pygame.display.set_caption('游戏事件')
    background =pygame.image.load("image/background.png").convert()
    window.blit(background)
    pygame.display.flip()

    """
    QUIT：关闭按钮被点击事件
    MOUSEBUTTONDOWN: 鼠标按下事件
    MOUSEBUTTONUP: 鼠标按下弹起
    MOUSEMOTION：鼠标移动
    鼠标相关事件关心事件产生的位置
    
    KEYDOWN: 键盘按下
    KEYUP: 键盘弹起
    """
    while True:
        # 每次循环检测有没有事件发生
        for event in pygame.event.get():
            # 不同类型的事件对应的type值不一样
            if event.type == pygame.QUIT:
                exit()

            # 鼠标相关事件
            # pos属性，获取鼠标事件产生的位置
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('鼠标按下', event.pos)

            if event.type == pygame.MOUSEBUTTONUP:
                print('鼠标弹起', event.pos)

            if event.type == pygame.MOUSEMOTION:
                print('鼠标移动', event.pos)

            # 键盘相关事件
            # key属性，被按的按键对应的值的编码
            if event.type == pygame.KEYDOWN:
                print('键盘按键被按下',chr(event.key))

            if event.type == pygame.KEYUP:
                print('键盘按钮弹起', chr(event.key))
