import random
class Color:
    white =(255,255,255)
    black =(0,0,0)
    red = (255,0,0)
    yellow =(255,255,0)
    green = (0,255,0)
    blue = (0,0,255)
    def __init__(self,r,g,b):
        self.r=r
        self.G=g
        self.b=b
    @staticmethod
    def rand_color():
        return random.randint