#### recursive tree


import sys
import math
import random
from typing import Sized, Union
import pygame
import numpy as NP
from pygame.constants import HAT_RIGHT, KEYDOWN, K_1, K_2, K_RETURN, K_a, K_c, K_d, K_e, K_f, K_k, K_l, K_m, K_r, K_s, K_w, SCALED
from collections import deque
pygame.init()
pygame.display.set_caption("Fractal Tree")
sys.setrecursionlimit(10**6)

#///COLOR//////////////////////////////////////////////////////////////
#//
Color_white = (255,255,255)
Color_red = (255,0,0)
Color_green = (0,255,0)
Color_blue = (0,0,255)
Color_orange = (255,128,0)
Color_black = (0,0,0)
Color_purple = (127,0,255)
Color_grey = (100,100,100)
Color_yellow = (255,255,0)
Color_brown = (160,82,45)
Color_saddlebrown = (139,69,19)
Color_DarkBlue = (0,51,102)
Color_DarkGreen = (0,102,0)
Color_pink = (255,0,255)
Color_DarkGrey = (48,48,48)
Color_cyan = (0,128,255)
Color_lightpurple = (204,153,255)
#//
#///COLOR//////////////////////////////////////////////////////////////

font1 = pygame.font.Font('AllTheWayToTheSun-o2O0.ttf',15)
def AddText(name,size,color,x,y):
    font = pygame.font.Font('AllTheWayToTheSun-o2O0.ttf',size)
    text = font.render(name,True,color)
    screen.blit(text,(x,y))


def RedFade(Value):
    if Value > 180:
        Value = Value % 180
    if (Value >= 0 and Value <= 30) or (Value >= 150 and Value <= 180):
        return 255
    elif (Value >= 60 and Value <= 120):
        return 0
    elif (Value >= 30 and Value <= 60):
        return math.floor((-255) * Value/30) + 510
    elif (Value >= 120 and Value <= 150):
        return math.floor((255) * Value/30) - 1020

def GreenFade(Value):
    if Value > 180:
        Value = Value % 180
    if (Value >= 30 and Value <= 90):
        return 255
    elif (Value >= 120 and Value <= 180):
        return 0
    elif (Value >= 90 and Value <= 120):
        return math.floor((-255) * Value/30) + 1020
    elif (Value >= 0 and Value <= 30):
        return math.floor((255) * Value/30)



def BlueFade(Value):
    if Value > 180:
        Value = Value % 180
    if (Value >= 90 and Value <= 150):
        return 255
    elif (Value >= 0 and Value <= 60):
        return 0
    elif (Value >= 150 and Value <= 180):
        return math.floor((-255) * Value/30) + 1530
    elif (Value >= 60 and Value <= 90):
        return math.floor((255) * Value/30) - 510





def ReturnFadeColor(Value):
    if Value < 0:
        if abs(Value) > 180:
            Value = -(abs(Value) % 180)
        Value = 180 + Value
    if Value > 180:
        Value = Value % 180
    return (RedFade(Value),GreenFade(Value),BlueFade(Value))

################################################################## screen setup
#//
ScreenWidth = 2200

ScreenHeight = 1200
screen = pygame.display.set_mode((ScreenWidth,ScreenHeight))

#//
################################################################## screen setup

################################################################## INPUT FUNCTION
#//
def GetPressKey():
    return pygame.key.get_pressed()

def GetMousePosition():
    return pygame.mouse.get_pos()

def GetClickState():
    return pygame.mouse.get_pressed()

#//
################################################################## INPUT FUNCTION

################################################################## ultility function

################################################################ DRAW FUNCTION
#//
def UpdateScreen():
    pygame.display.update() ### important

def UpdateUI(Color):
    DrawRect(Color,0,0,300,ScreenHeight)

def UpdateUI2(Color):
    DrawRect(Color,1900,0,2200,ScreenHeight)

def ResetTree():
    DrawRect(Color_black,300,0,ScreenWidth,ScreenHeight)

def GetTreeColor(num,type):
    if num > 255:
        num = num % 255
        num = 255 - num
    if type == "NotSet":
        return Color_lightpurple
    elif type == "Rainbow":
        return ReturnFadeColor(num)
    elif type == "Red":
        return RedGradient(num)
    elif type == "Green":
        return GreenGradient(num)
    elif type == "Blue":
        return BlueGradient(num)

def RedGradient(num):
    if num > 255:
        num = num % 255
        num = 255 - num
    return(num,0,int((255 - num))/8)

def GreenGradient(num):
    if num > 255:
        num = num % 255
        num = 255 - num
    return(0,num,int((255 - num)/8))

def BlueGradient(num):
    if num > 255:
        num = num % 255
        num = 255 - num
    return(int((255 - num)/8),0,num)



def DrawRecursiveTree(X,Y,Angle,splitangle,Lenght,nextlength_percent,level,FadeType,TreeType):
    if level > 0:
        Xend = X + Lenght * math.cos(Angle)
        Yend = Y - Lenght * math.sin(Angle)
        ColorDraw = GetTreeColor(level * 20,FadeType)
        if "Random Lenght" in TreeType:
            NEWlenght1 = int(Lenght * random.randint(nextlength_percent,100)/100) + 5
            NEWlenght2 = int(Lenght * random.randint(nextlength_percent,100)/100) + 5
        else:
            NEWlenght1 = int(Lenght * nextlength_percent/100) + 5
            NEWlenght2 = int(Lenght * nextlength_percent/100) + 5
        if "Random Angle" in TreeType:
            splitangle = ReturnRadian(random.randint(1,45))
        DrawLine(ColorDraw,X,Y,Xend,Yend,level)
        if "Curve" in TreeType:
            DrawRecursiveTree(Xend,Yend,Angle + splitangle,splitangle,NEWlenght1,nextlength_percent,level - 1,FadeType,TreeType)
            DrawRecursiveTree(Xend,Yend,Angle - math.pi/4,splitangle,NEWlenght2,nextlength_percent,level - 1,FadeType,TreeType)
        else:
            DrawRecursiveTree(Xend,Yend,Angle + splitangle,splitangle,NEWlenght1,nextlength_percent,level - 1,FadeType,TreeType)
            DrawRecursiveTree(Xend,Yend,Angle - splitangle,splitangle,NEWlenght2,nextlength_percent,level - 1,FadeType,TreeType)

def IsInRect(X1,Y1,W,H,MX,MY):
    return X1 <= MX and X1 + W >= MX and Y1 <= MY and Y1 + H >= MY

def ReturnRadian(degree):
    return degree * math.pi/180

def DrawCircle(Color,X,Y,Radius):
    pygame.draw.circle(screen,Color,(X,Y),Radius)



def ClearScreen(color):
    DrawRect(color,0,0,ScreenWidth,ScreenHeight) ### important

def DrawRect(COLOR,X,Y,W,H):
    pygame.draw.rect(screen,COLOR,[X,Y,W,H])

def DrawLine(COLOR,X1,Y1,X2,Y2,Thickness):
    pygame.draw.line(screen,COLOR,(X1,Y1),(X2,Y2),Thickness)

def DrawUIbox(X,Y,W,H,Thickness,ShadowOffset):
    DrawRect(Color_black,X + ShadowOffset,Y + ShadowOffset,W,H)
    DrawRect(Color_cyan,X,Y,W,H)
    DrawRect(Color_DarkGrey,X + Thickness,Y + Thickness,W - 2* Thickness,H - 2 * Thickness)

def DrawUIboxGreen(X,Y,W,H,Thickness):
    DrawRect(Color_green,X - 3,Y - 3,W + 6,H + 6)
    DrawRect(Color_DarkGrey,X + Thickness,Y + Thickness,W - 2* Thickness,H - 2 * Thickness)

def DrawDragBar(X,Y,W,H,Thickness):
    DrawRect(Color_lightpurple,X,Y,W,H)
    DrawRect(Color_black,X + Thickness,Y + Thickness,W - 2* Thickness,H - 2 * Thickness)
#//
################################################################ DRAW FUNCTION
#//
################################################################ DRAW FUNCTION
DrawTree = False
int_NextLenght_percent = 20
Xnextlenght = 1980
int_Recursion_level = 1
Xrecursion = 1980
int_StartLenght = 20
Xstartlenght = 1980
int_SplitAngle = 0
Xangle = 1980
Bool_running = True
String_TreeFadeColor = "NotSet"
ClickTimer = 1
ClickAllow = 5
Set_TreeType = set()
while Bool_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Bool_running = False
        mx ,my = GetMousePosition()
        Coordinate_mouse = NP.array([mx,my])
        click = GetClickState()

        ############################################################################################
        if DrawTree:
            SplitAngleRad = ReturnRadian(int_SplitAngle)
            ResetTree()
            DrawRecursiveTree(1100,ScreenHeight,math.pi/2,SplitAngleRad,int_StartLenght,int_NextLenght_percent,int_Recursion_level,String_TreeFadeColor,Set_TreeType)
            DrawTree = False

        UpdateUI(Color_DarkGrey)
        UpdateUI2(Color_DarkGrey)
        DrawLine(Color_cyan,285,0,285,ScreenHeight,30)
        DrawLine(Color_cyan,1915,0,1915,ScreenHeight,30)
        

        
        AddText("FADE",30,Color_lightpurple,40,80)
        if String_TreeFadeColor == "Rainbow":
            DrawUIboxGreen(40,130,150,40,3)
        else:
            DrawUIbox(40,130,150,40,3,3)
        AddText("Rainbow",20,Color_white,60,140)

        if String_TreeFadeColor == "Red":
            DrawUIboxGreen(40,180,150,40,3)
        else:
            DrawUIbox(40,180,150,40,3,3)
        AddText("Fade red",20,Color_white,60,190)

        if String_TreeFadeColor == "Green":
            DrawUIboxGreen(40,230,150,40,3)
        else:
            DrawUIbox(40,230,150,40,3,3)
        AddText("Fade green",20,Color_white,60,240)

        if String_TreeFadeColor == "Blue":
            DrawUIboxGreen(40,280,150,40,3)
        else:
            DrawUIbox(40,280,150,40,3,3)
        AddText("Fade blue",20,Color_white,60,290)

        if click[0] == 1 and ClickTimer >= ClickAllow:
            if IsInRect(40,130,150,40,mx,my):
                ClickTimer = 0
                if String_TreeFadeColor == "Rainbow":
                    String_TreeFadeColor = "NotSet"
                else:
                    String_TreeFadeColor = "Rainbow"
            elif IsInRect(40,180,150,40,mx,my):
                ClickTimer = 0
                if String_TreeFadeColor == "Red":
                    String_TreeFadeColor = "NotSet"
                else:
                    String_TreeFadeColor = "Red"
            elif IsInRect(40,230,150,40,mx,my):
                ClickTimer = 0
                if String_TreeFadeColor == "Green":
                    String_TreeFadeColor = "NotSet"
                else:
                    String_TreeFadeColor = "Green"
            elif IsInRect(40,280,150,40,mx,my):
                ClickTimer = 0
                if String_TreeFadeColor == "Blue":
                    String_TreeFadeColor = "NotSet"
                else:
                    String_TreeFadeColor = "Blue"

        AddText("Tree Type",30,Color_lightpurple,40,340)

        if "Random Angle" in Set_TreeType:
            DrawUIboxGreen(40,390,150,40,3)
        else:
            DrawUIbox(40,390,150,40,3,3)
        AddText("Random Angle",20,Color_white,60,400)
        if "Curve" in Set_TreeType:
            DrawUIboxGreen(40,440,150,40,3)
        else:
            DrawUIbox(40,440,150,40,3,3)
        AddText("Curve",20,Color_white,60,450)
        if "Random Lenght" in Set_TreeType:
            DrawUIboxGreen(40,490,150,40,3)
        else:
            DrawUIbox(40,490,150,40,3,3)
        AddText("Random Lenght",20,Color_white,60,500)
        
        

        if click[0] == 1 and ClickTimer >= ClickAllow:
            if IsInRect(40,390,150,40,mx,my):
                ClickTimer = 0
                if "Random Angle" in Set_TreeType:
                    Set_TreeType.remove("Random Angle")
                else:
                    Set_TreeType.add("Random Angle")
            elif IsInRect(40,440,150,40,mx,my):
                ClickTimer = 0
                if "Curve" in Set_TreeType:
                    Set_TreeType.remove("Curve")
                else:
                    Set_TreeType.add("Curve")
            elif IsInRect(40,490,150,40,mx,my):
                ClickTimer = 0
                if "Random Lenght" in Set_TreeType:
                    Set_TreeType.remove("Random Lenght")
                else:
                    Set_TreeType.add("Random Lenght")



        AddText("Variable",30,Color_lightpurple,1980,200)

        
        DrawUIbox(1980,250,150,40,3,3)
        AddText("Split Angle : " + str(int(int_SplitAngle)),20,Color_white,1990,260)
        DrawDragBar(1980,310,120,20,3)
        DrawUIboxGreen(Xangle,305,10,30,3)
        if IsInRect(1980,310,120,20,mx,my) and click[0] == 1:
            Xangle = mx
            int_SplitAngle = int((Xangle - 1980) * 3)/2
        
        DrawCircle(Color_purple,2075,460,100)
        angletodraw = ReturnRadian(int_SplitAngle)
        DrawLine(Color_white,2070,460,2070 + 100 * math.cos(angletodraw),460 - 100 * math.sin(angletodraw),2)
        DrawRect(Color_DarkGrey,1970,460,2300,900)

        DrawUIbox(1980,510,200,40,3,3) # 1 to 18
        AddText("Recursion level : " + str(int(int_Recursion_level)),20,Color_white,1990,520)
        DrawDragBar(1980,570,180,20,3)
        DrawUIboxGreen(Xrecursion,565,10,30,3)
        if IsInRect(1980,570,180,20,mx,my) and click[0] == 1:
            Xrecursion = mx
            int_Recursion_level = int((Xrecursion - 1980)/10)
            if int_Recursion_level < 1:
                int_Recursion_level += 1

        DrawUIbox(1980,610,200,40,3,3)
        AddText("lenght variation : " + str(int(int_NextLenght_percent)),20,Color_white,1990,620)
        DrawDragBar(1980,670,120,20,3)
        DrawUIboxGreen(Xnextlenght,665,10,30,3)
        if IsInRect(1980,670,120,20,mx,my) and click[0] == 1:
            Xnextlenght = mx
            int_NextLenght_percent = 20 + int((Xnextlenght - 1980)/2)

        DrawUIbox(1980,710,200,40,3,3)
        AddText("Start lenght : " + str(int(int_StartLenght)),20,Color_white,1990,720)
        DrawDragBar(1980,770,180,20,3)
        DrawUIboxGreen(Xstartlenght,765,10,30,3)
        if IsInRect(1980,770,180,20,mx,my) and click[0] == 1:
            Xstartlenght = mx
            int_StartLenght = 20 + int((Xstartlenght - 1980))




        DrawUIbox(1980,100,200,50,5,5)
        AddText("Generate",35,Color_lightpurple,2010,110)
        if IsInRect(1980,100,200,50,mx,my) and click[0] == 1 and ClickTimer >= ClickAllow:
            ClickTimer = 0
            DrawTree = True


        
        ############################################################################################

        
        ClickTimer += 1
        UpdateScreen()
