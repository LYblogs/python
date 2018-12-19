"""__author__ = 余婷"""
"""
动画原理：不断的刷新界面上的内容（一帧一帧的画）
"""
import pygame
from random import randint


def static_page(screen):
    """
    页面上的静态内容
    """
    # 静态文字
    font = pygame.font.SysFont('Times', 40)
    title = font.render('Welcome', True, (0, 0, 0))
    screen.blit(title, (200, 200))

def animation_title(screen):
    """
    字体颜色发生改变
    """
    font = pygame.font.SysFont('Times', 40)
    title = font.render('Python', True, (randint(0,255), randint(0,255), randint(0,255)))
    screen.blit(title, (100, 100))


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    screen.fill((255, 255, 255))

    static_page(screen)

    pygame.display.flip()

    while True:
        # for里面的代码只有事件发生后才会执行
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        # 在下面去写每一帧要显示的内容
        """程序执行到这个位置，cup休息一段时间再执行后面的代码(线程在这儿阻塞指定的时间)
        单位：毫秒  (1000ms == 1s)
        """
        pygame.time.delay(60)

        # 动画前要将原来的内容全部清空
        screen.fill((255, 255, 255))

        static_page(screen)
        animation_title(screen)

        # 内容展示完成后，要更新到屏幕上
        pygame.display.update()


