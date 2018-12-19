import pygame
pygame.init()
window =pygame.display.set_mode((400,600))
window.fill((255,200,200))

#======================显示图片=====================
#1.加载图片
"""
pygame.image.load(图片地址)
"""
image_obj=pygame.image.load("files/bb.jpg")
#2.渲染图片
"""
blit(渲染对象，位置)
渲染对象 -图片对象 （显示什么）
位置 - 坐标（元组：（x，y））
"""


#3.获取图片大小
"""
图片对象.get_size()- 获取图片大小，返回值是一个元组：（width，height）


"""
#4.图片缩放、旋转
"""
a.缩放
pygame.transform.scale(图片对象，大小元组)-将指定的图片缩放到指定的大小,返回新的图片对象
b.旋转缩放
pygame.transform.rotozoom(图片对象，旋转角度，缩放比例)
"""
# new_image =pygame.transform.scale(image_obj,(300,400))
new_image = pygame.transform.rotozoom(image_obj,45,0.5)
im_w,im_h = new_image.get_size()
window.blit(new_image,((400-im_w)/2,(600-im_h)/2))



pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            exit() #程序结束