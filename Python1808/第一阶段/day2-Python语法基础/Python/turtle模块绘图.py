#导入turtle库

#其他命令
#done() 程序继续执行
#undo() 撤销上一次动作
#hideturtle()  隐藏海龟
#showturtle()  显示海龟 
import turtle

turtle.done()
''' 移动命令
forward(d) 向前移动
backward(d) 向后移动
right(d)向右转动多少度
left(d)向左转动多少度
goto(x,y)到（x，y）这个位置
speed()移动速度[0,10]

笔画控制命令
up()  笔画抬起，不会绘图，只移动
down() 笔画落下
setheading()  改变海龟的朝向
pensize() 改变笔画的宽度
pencolor("red")颜色
reset() 清空页面，并恢复设置
clear()仅清空页面
circle(r,steps=e)绘制一个圆形，r为半径，e为次数


begin_fill
fillcolor()
end_fill    填充颜色