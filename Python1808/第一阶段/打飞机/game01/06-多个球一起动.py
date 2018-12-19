"""__author__ = 余婷"""
import pygame
import random

random_color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    screen.fill((255, 255, 255))
    pygame.display.flip()

    # all_balls中保存多个球
    # 每个球要保存：半径、圆心坐标、颜色、x速度、y速度
    all_balls = [
        {
            'r': random.randint(10, 20),
            'pos': (100, 100),
            'color':random_color,
            'x_speed': random.randint(-3, 3),
            'y_speed': random.randint(-3, 3),
        },
        {
            'r': random.randint(10, 20),
            'pos': (300, 300),
            'color': random_color,
            'x_speed': random.randint(-3, 3),
            'y_speed': random.randint(-3, 3),
        }
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # 点一下鼠标创建一个球
                ball = {
                        'r': random.randint(10, 25),
                        'pos': event.pos,
                        'color': random_color,
                        'x_speed': random.randint(-3, 3),
                        'y_speed': random.randint(-3, 3)
                    }
                # 保存球
                all_balls.append(ball)



        # 刷新界面
        screen.fill((255, 255, 255))

        for ball_dict in all_balls:
            # 取出球原来的x坐标和y坐标以及他们的速度
            x, y = ball_dict['pos']
            x_speed = ball_dict['x_speed']
            y_speed = ball_dict['y_speed']
            x += x_speed
            y += y_speed
            pygame.draw.circle(screen, ball_dict['color'], (x, y), ball_dict['r'])
            # 更新球对应的坐标
            ball_dict['pos'] = x, y

        pygame.display.update()
