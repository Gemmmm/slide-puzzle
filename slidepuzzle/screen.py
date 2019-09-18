import sys

import pygame
import pygame, sys, random
from pygame.locals import *
from dbcon import *
BLACK =         (  0,   0,   0)
WHITE =         (255, 255, 255)
BRIGHTBLUE =    (  0,  50, 255)
DARKTURQUOISE = (  3,  54,  73)
GREEN =         (  0, 204,   0)
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
MESSAGECOLOR = WHITE
BGCOLOR = DARKTURQUOISE
BASICFONTSIZE = 20
BUTTONTEXTCOLOR = BLACK
def creat_screen():
    global DISPLAYSURF,BASICFONT
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    # 初始化pygame
    pygame.init()
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
    # 设置窗口大小并保存在screen对象中
    screen = pygame.display.set_mode((500, 500))

    # 设置窗口的名字
    pygame.display.set_caption("Screen")

    # 游戏的主循环
    while True:
        # 给屏幕填充蓝色
        screen.fill(( 3,  54,  73))
        msg=""
        list1=select()
        int_i=1
        msg = "----------------------------"
        textSurf, textRect = makeText(str(msg), MESSAGECOLOR, BGCOLOR, 120, 5)
        DISPLAYSURF.blit(textSurf, textRect)
        msg = "|     time     |  score | "
        textSurf, textRect = makeText(str(msg), MESSAGECOLOR, BGCOLOR, 120, 30 )
        DISPLAYSURF.blit(textSurf, textRect)
        for i in list1:
            msg="| "+i[0]+ "   |    "+i[1]+"   |"
            textSurf, textRect = makeText(str(msg), MESSAGECOLOR, BGCOLOR, 120, 30+30*int_i)
            DISPLAYSURF.blit(textSurf, textRect)
            int_i+=1
        msg = "----------------------------"
        textSurf, textRect = makeText(str(msg), MESSAGECOLOR, BGCOLOR, 120, 30 + 30 * int_i)
        DISPLAYSURF.blit(textSurf, textRect)
        # 侦听事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # 先退出pygame窗口，再退出程序
                pygame.quit()
                sys.exit()

        # 更新整个待显示的 Surface 对象到屏幕上
        pygame.display.flip()


def drawBoard( message):
    DISPLAYSURF.fill(BGCOLOR)
    if message:
        textSurf, textRect = makeText(message, MESSAGECOLOR, BGCOLOR, 5, 5)
        DISPLAYSURF.blit(textSurf, textRect)

def makeText(text, color, bgcolor, top, left):
    # create the Surface and Rect objects for some text.
    textSurf = BASICFONT.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)

