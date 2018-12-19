"""__author__ = 余婷"""
import pygame
from random import randint


def rand_color():
    """
    产生随机颜色
    """
    return randint(0, 255), randint(0, 255), randint(0, 255)

def draw_ball(screen, pos):
    pygame.draw.circle(screen, rand_color(), pos, randint(10, 20))
    # 只要屏幕上的内容有更新，都需要调用下面这两个方法中的一个
    # pygame.display.flip()
    pygame.display.update()


# 写一个函数，判断指定的点是否在指定的矩形范围中
def is_in_rect(point, rect):
    x, y = point
    rx, ry, rw, rh = rect
    if (rx <= x <= rx+rw) and (ry <= y <= ry+rh):
        return True
    return False


# 写一个函数，画一个按钮
def draw_button(screen, bth_color, title_color):
    # 画个按钮
    """矩形框"""
    pygame.draw.rect(screen, bth_color, (100, 100, 100, 60))
    """文字"""
    font = pygame.font.SysFont('Times', 30)
    title = font.render('clicke', True, title_color)
    screen.blit(title, (120, 120))

# 按钮坐标

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    screen.fill((255,255,255))
    pygame.display.set_caption('鼠标事件')

    # 画个按钮
    draw_button(screen, (0, 255, 0), (255, 0, 0))
    # """矩形框"""
    # pygame.draw.rect(screen,(0, 255, 0),(100, 100, 100, 60))
    # """文字"""
    # font = pygame.font.SysFont('Times', 30)
    # title = font.render('clicke',True,(255, 0, 0))
    # screen.blit(title, (120, 120))



    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            # 退出
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # 在指定的坐标处画一个球
                # draw_ball(screen, event.pos)
                if is_in_rect(event.pos, (100, 100, 100, 60)):
                    draw_button(screen, (0, 100, 0), (100, 0, 0))
                    pygame.display.update()

            if event.type == pygame.MOUSEBUTTONUP:
                if is_in_rect(event.pos, (100, 100, 100, 60)):
                    draw_button(screen, (0, 255, 0),(255, 0, 0))
                    pygame.display.update()

            if event.type == pygame.MOUSEMOTION:
                screen.fill((255, 255, 255))
                draw_button(screen, (0, 255, 0), (255, 0, 0))
                draw_ball(screen, event.pos)