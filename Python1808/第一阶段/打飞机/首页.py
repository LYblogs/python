import pygame
from color import Color
from text import Text
import shou
def home_page():
    num = 0
    if __name__ == '__main__':
        pygame.init()
        window = pygame.display.set_mode((400,600))
        window.fill((255, 255, 255))
        # 设置窗口标题
        pygame.display.set_caption('打飞机')
        #设置背景图片
        shou.home_page(window)
        #设置文字
        t1 =Text(window,'files/aa.ttf',"飞机大战",60,Color.black,(80,150))
        t1.custom_text()
        t2 =Text(window,"files/hei1.ttf","开始游戏",30,Color.random_color(),(135,300))
        t2.custom_text()

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEMOTION and num ==0:
                    t2 = Text(window, "files/hei1.ttf", "开始游戏", 30, Color.random_color(), (135,300))
                    t2.custom_text()
                    pygame.display.update()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    location = event.pos
                    if 135 <= location[0] <= 255 and 300 <= location[1] <= 330:
                        shou.home_page(window)
                        num = 1
                        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEMOTION:
                    pass

if __name__ == '__main__':
    home_page()
