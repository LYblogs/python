"""__author__ = 余婷"""
import pygame

pygame.init()
window = pygame.display.set_mode((400, 600))
window.fill((255, 255, 255))

# =========显示图片===========
# 1.加载图片
"""
pygame.image.load(图片地址) - 加载指定路径下的图片，返回一个图片对象
"""
image_obj = pygame.image.load('files/luffy.jpg')
window.blit(image_obj, (0, 0))
# 2.渲染图片
"""
blit(渲染对象, 位置) 
渲染对象 - 图片对象(显示什么)
位置 - 元祖，(x, y)
"""

# 3.获取图片的大小
"""
图片对象.get_size() - 获取图片大小,返回值是一个元祖:(width, height)
"""
image_w, image_h = image_obj.get_size()
# window.blit(image_obj, ((400-image_w)/2, (600-image_h)/2))

# 4.图片缩放和旋转
"""
a.缩放
pygame.transform.scale(图片对象, 大小) - 将指定的图片缩放在指定的大小, 返回新的图片对象
"""
new_image = pygame.transform.scale(image_obj, (50, 150))
window.blit(new_image, (0, 110))

"""
b.旋转缩放
pygame.transform.rotozoom(图片对象, 旋转角度, 缩放比例)
"""
new_image2 = pygame.transform.rotozoom(image_obj, 0, 0.5)
window.blit(new_image2, (0, 270))


new_image3 = pygame.transform.rotozoom(image_obj, 45, 1.5)
window.blit(new_image3, (0, 330))





pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()