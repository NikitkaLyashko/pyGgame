import random
import time
import pygame

picture=pygame.display.set_mode([800,800])
a=random.randint(50,150)
b=random.randint(50,150)
rect=pygame.Rect(400,400,a,b)
rect.centerx=400
rect.centery=400
speed = -2
right_speed=0

while True:
    time.sleep(1/60)
    event=pygame.event.get()

    for event_2 in event:

        if event_2.type==256:
            exit()

        if event_2.type==pygame.KEYDOWN:
            print(event_2.key)
            if pygame.K_SPACE==event_2.key:
                rect.centerx = 400
                rect.centery = 400
            if pygame.K_d==event_2.key:
                right_speed+=1
            if pygame.K_a==event_2.key:
                right_speed-=1

        if event_2.type==pygame.MOUSEBUTTONDOWN:

            rect.centerx = event_2.pos[0]
            rect.centery = event_2.pos[1]
            right_speed=0

        if event_2.type==pygame.MOUSEMOTION:
            pos=event_2.pos
            rect.centerx=pos[0]
            rect.y=pos[1]







    picture.fill([45,76,123])
    pygame.draw.rect(picture,[86,255,37],rect)
    rect.right +=right_speed

    if rect.left>=800:
        rect.right=0

    # rect.top+=speed
    # if rect.top<=0:
    #     speed=2
    # elif rect.bottom>=800:
    #     speed=-2
    #
    #



    pygame.display.flip()