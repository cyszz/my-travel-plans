import pygame
import sys
from pygame.locals import*
import numpy as np
from random import randint
pygame.init()

rect_width=10
size=width,height=800,500
COLOR=(100,67,3)#蛇的颜色
x_rect=int(width/rect_width)
y_rect=int(height/rect_width)#长宽格子有多个


bg=(100,180,180)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("python趣味爱好者")


ground=np.zeros([x_rect,y_rect])#整条蛇占据的矩阵，0是没有。

for i in range(1,x_rect-1):
    for j in range(1,y_rect-1):
        if randint(1,10)<2:
            ground[i][j]=1
        else:
            pass
def get_rect(row,column):#计算应该在哪里画方格，以右上角为点。
    x1=rect_width*row
    y1=rect_width*column

    return (x1,y1,rect_width,rect_width)

#pygame.draw.rect(screen,COLOR,get_rect(row,column),0)
def food_num(x,y):#为了避免出现ground[-1][-1]的情况，我们需要从1开始
    num=0
    neighbour=[ground[x][y-1],ground[x][y+1],ground[x-1][y],ground[x+1][y]\
               ,ground[x-1][y-1],ground[x+1][y-1],ground[x-1][y+1],ground[x+1][y+1]]
    return sum(neighbour)
    
def draw_food(x,y):
    pygame.draw.rect(screen,COLOR,get_rect(x,y),0)

while True:
    
    for i in range(1,x_rect-1):#所有细胞的生存状态发展
        for j in range(1,y_rect-1):
            if ground[i][j]==1:
                if food_num(i,j)!=2 and food_num(i,j)!=3:
                    ground[i][j]=0
                else:
                    pass
            else:
                if food_num(i,j)==3:
                    ground[i][j]=1
                else:
                    pass

    #下面是画出所有的细胞
    screen.fill(bg)#填充背景颜色         
    for i in range(1,x_rect-1):#所有细胞的生存状态发展
        for j in range(1,y_rect-1):
            if ground[i][j]==1:
                draw_food(i,j)
            else:
                pass
                


    pygame.display.flip()
    pygame.time.delay(80)


