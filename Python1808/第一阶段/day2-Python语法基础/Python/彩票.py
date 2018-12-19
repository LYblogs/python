import random
num = int(input("请输入您的号码："))
res =random.randrange(1,4,2)
if res != num:
    print("恭喜中奖")
else:
    print("谢谢惠顾")
input("请按任意键退出")