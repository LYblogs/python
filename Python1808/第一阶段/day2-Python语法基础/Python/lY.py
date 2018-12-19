import random
num = int(input('请输入您的彩票数字：'))
res = random.choice(range(100)) + 1
if num == res:
    print('恭喜您中奖！')
else:
    print('谢谢惠顾')
