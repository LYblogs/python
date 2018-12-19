"""__author__ = 余婷"""
import pygame


def draw_ball(place, color, pos):
    """
    画球
    """
    pygame.draw.circle(place, color, pos, 20)

# 方向对应的key值
Up = 273
Down = 274
Left = 276
Right = 275

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    screen.fill((255, 255, 255))
    pygame.display.flip()

    # 保存初始坐标
    ball_x = 100
    ball_y = 100
    x_speed = 5
    y_speed = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            # 通过上下左右键控制球的方向
            if event.type == pygame.KEYDOWN:
                if event.key == Up:
                    y_speed = -5
                    x_speed = 0
                elif event.key == Down:
                    y_speed = 5
                    x_speed = 0
                elif event.key == Right:
                    x_speed = 5
                    y_speed = 0
                elif event.key == Left:
                    x_speed = -5
                    y_speed = 0


        # 刷新屏幕
        screen.fill((255, 255, 255))

        # 每次循环让球的x和y坐标变化
        ball_x += x_speed
        ball_y += y_speed

        # 边界检测
        if ball_x + 20 >= 600 or ball_x <= 20 or ball_y + 20 >= 400 or ball_y <= 20:
            print('游戏结束')
            exit()
            # ball_x = 600 -20
            # x_speed *= -1
        draw_ball(screen, (255, 0, 0), (ball_x, ball_y))

        pygame.display.update()