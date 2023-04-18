import pygame
pygame.init()
font=pygame.font.SysFont("arial",50,False,False)

text_1=font.render("Hello world",True,[123,123,123])
pygame.image.save(text_1,"1.png")