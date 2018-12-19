import pygame
from color import Color
import deng_lu
#游戏初始化
pygame.init()
#创建游戏窗口
window = pygame.display.set_mode((600,400))
#填充窗口
window.fill((200,255,200))
#加载图片
im_obj =pygame.image.load("files/111.jpg")
im_obj2 =pygame.image.load("files/222.jpg")
#图片缩放、旋转
im_obj2=pygame.transform.rotozoom(im_obj2,0,0.5)
im_obj =pygame.transform.rotozoom(im_obj,0,0.4)
im_w,im_h =im_obj2.get_size()
#渲染图片
window.blit(im_obj,(100,50))
#选笔
font = pygame.font.Font("files/hei1.ttf",20)
#创建文字对象
text =font.render("欢迎来到召唤师管理系统",True,Color.black)
text1 =font.render("账号：",True,Color.black)
text2 =font.render("密码：",True,Color.black)
text3 =font.render("登录",True,Color.white)
#将文字渲染到窗口
window.blit(text,(200,30))
#画矩形
pygame.draw.rect(window,(30,144,255),(200,100,220,40))
pygame.draw.rect(window,(30,144,255),(200,180,220,40))
pygame.draw.rect(window,(255,69,0),(220,270,180,50))
##将文字渲染到窗口
window.blit(text1,(210,105))
window.blit(text2,(210,185))
window.blit(text3,(290,280))

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            location=event.pos
            if 220<=location[0]<=400 and 270<=location[1]<=320:
                window.fill(Color.white)
                window.fill((200, 255, 200))
                window.blit(im_obj2, ((600-im_w)/2,(400-im_h)/2))
                font = pygame.font.Font("files/hei1.ttf", 30)
                text = font.render("我卢本伟没有开挂", True, Color.black)
                window.blit(text, (170,325))
                pygame.display.update()