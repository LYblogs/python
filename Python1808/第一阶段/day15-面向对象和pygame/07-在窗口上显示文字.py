import pygame
#1.游戏初始化
pygame.init()
#2.创建游戏窗口
window =pygame.display.set_mode((400,600))
#将窗口填充成不同的颜色
window.fill((255 ,200,200))
#=======显示文字=====
#1.创建字体对象（选笔）
"""
a.系统字体
pygame.font.SysFont(字体名，字体大小，是否加粗=False，是否倾斜 =False)-返回对象
b.自定义字体
pygame.font.Font(字体文件路径，字体大小)
"""
# font = pygame.font.SysFont("Times",20)
font= pygame.font.Font("files/aa.ttf",20)
#2.根据字体创建文字对象
"""
render(文字内容，是否平滑，文字颜色)

"""
text =font.render("cngz,zengpi",True,(255,0,0))

#3.将文字渲染到窗口
window.blit(text,(150,250))



#将窗口显示到设备上
pygame.display.flip()
#3.创建游戏循环
while True:
    # 4.检测事件
    for event in pygame.event.get():
        #5.区分不同的事件，做出不同的反应
        if event.type ==pygame.QUIT:
            exit() #程序结束
