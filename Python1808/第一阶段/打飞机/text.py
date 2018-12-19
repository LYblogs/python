import pygame
from color import Color

class Text:
    def __init__(self,name,address,text1,size,color,location:tuple):
        self.address =address
        self.text1 = text1
        self.color =color
        self.size =size
        self.name =name
        self.location =location
    def system_text(self):
        text=pygame.font.SysFont('Times',self.size,True,False)
        self.name.blit(text,self.location)
    def custom_text(self):
        font = pygame.font.Font(self.address,self.size)
        text = font.render(self.text1, False,self.color)
        self.name.blit(text, self.location)