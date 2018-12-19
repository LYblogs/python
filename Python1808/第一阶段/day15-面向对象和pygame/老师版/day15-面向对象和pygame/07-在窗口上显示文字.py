"""__author__ = 余婷"""
import pygame

pygame.init()
window = pygame.display.set_mode((400, 600))
window.fill((255, 255, 255))

# =======显示文字=========
# 1.创建字体对象(选笔)
"""
a.系统字体
pygame.font.SysFont(字体名, 字体大小, 是否加粗=False,是否倾斜=False) - 返回字体对象

b.自定义字体
pygame.font.Font(字体文件路径, 字体大小)
"""
# font = pygame.font.SysFont('Times', 50, italic=True)
font = pygame.font.Font('files/aa.ttf', 40)
# 2.根据字体创建文字对象
"""
render(文字内容, 是否平滑, 文字颜色)
"""
text = font.render('hello pygame 你好！', True, (255, 0, 0))

# 3.将文字渲染到窗口上
window.blit(text, (100, 100))


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()