import pygame
win=pygame.Surface([200,300])

pygame.draw.line(win,[255,246,32],[100,100],[300,100],5)

pygame.draw.rect(win,[222,43,98],[100,100,50,50],5)

pygame.draw.circle(win,[145,23,72],[100,150],10,3)

pygame.draw.ellipse(win,[255,246,32],[100,100,50,50])

pygame.image.save(win,"1.jpg")


img=pygame.image.load('img.png')

pygame.draw.line(img,[255,246,32],[100,100],[300,100],5)

# print(img.get_width())

img.blit(win,[100,100])

img_2=pygame.transform.scale(img,[200,200])
img_3=pygame.transform.flip(img,True,True)
img_4=pygame.transform.rotate(img,90)
pygame.image.save(img_2,"3.jpg")
pygame.image.save(img_4,"5.jpg")
pygame.image.save(img_3,"4.jpg")




pygame.image.save(img,"2.jpg")