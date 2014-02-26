# def_parts for the flying chess
from class_parts import *
from graphics import *
from random import *
from time import *
def plus(a,color):
    if color == 'red':
        if a == 205:
            return 1
        else:
            return a+1
    elif color == 'yellow':
        if a == 211:
            return 14
        elif a == 52:
            return 1
        else:
            return a + 1
    elif color == 'blue':
        if a == 217:
            return 27
        elif a == 52:
            return 1
        else:
            return a+1
    else:
        if a == 223:
            return 40
        elif a == 52:
            return 1
        else:

            return a+1

def splus(a,color):
    if color == 'red':
        if a == 50:
            return 101
        elif a == 105:
            return 206
        else:
            return a+1
    elif color == 'yellow':
        if a == 11:
            return 106
        elif a == 110:
            return 212
        else:
            return a+1
    elif color == 'blue':
        if a == 24:
            return 111
        elif a == 115:
            return 218
        else:
            return a+1
    else:
        if a == 37:
            return 116
        elif a == 120:
            return 224
        else:
            return a+1

def run(thelist):
    t1 = Text(Point(3,5),'out!')
    t2 = Text(Point(3,5),'6!again')
    win = thelist[0]
    dice_roll = thelist[1]
    br1 = thelist[2]
    br2 = thelist[3]
    br3 = thelist[4]
    br4 = thelist[5]
    r1 = thelist[6]
    r2 = thelist[7]
    r3 = thelist[8]
    r4 = thelist[9]
    y1 = thelist[10]
    y2 = thelist[11]
    y3 = thelist[12]
    y4 = thelist[13]
    b1 = thelist[14]
    b2 = thelist[15]
    b3 = thelist[16]
    b4 = thelist[17]
    g1 = thelist[18]
    g2 = thelist[19]
    g3 = thelist[20]
    g4 = thelist[21]
    button_click = thelist[22]
    
    k = win.getMouse()
    while not(button_click.click(k)==1):
        k = win.getMouse()
    ran = randrange(1,7)
    dice_roll.setNumber(ran)
    while ran == 6:
        br1.draw(win)
        br2.draw(win)
        br3.draw(win)
        br4.draw(win)
        s = win.getMouse()
        while not(br1.click(s) or br2.click(s) or br3.click(s)or\
                    br4.click(s)):
            s = win.getMouse()
        br1.undraw()
        br2.undraw()
        br3.undraw()
        br4.undraw()
        if br1.click(s):
            r1.move(ran)
            r1.jump()
            if r1.getwinhome():
                br1.setactive(0)
            gotodecide(r1,y1,y2,y3,y4,b1,b2,b3,b4,g1,g2,g3,g4)
            t2.draw(win)
            k = win.getMouse()
            while not(button_click.click(k)==1):
                k = win.getMouse()
            ran = randrange(1,7)
            t2.undraw()
            dice_roll.setNumber(ran)
        elif br2.click(s):
            r2.move(ran)
            r2.jump()
            if r2.getwinhome():
                br2.setactive(0)
            gotodecide(r2,y1,y2,y3,y4,b1,b2,b3,b4,g1,g2,g3,g4)
            t2.draw(win)
            k = win.getMouse()
            while not(button_click.click(k)==1):
                k = win.getMouse()
            ran = randrange(1,7)
            t2.undraw()
            dice_roll.setNumber(ran)
        elif br3.click(s):
            r3.move(ran)
            r3.jump()
            if r3.getwinhome():
                br3.setactive(0)
            gotodecide(r3,y1,y2,y3,y4,b1,b2,b3,b4,g1,g2,g3,g4)
            t2.draw(win)
            k = win.getMouse()
            while not(button_click.click(k)==1):
                k = win.getMouse()
            ran = randrange(1,7)
            t2.undraw()
            dice_roll.setNumber(ran)
        elif br4.click(s):
            r4.move(ran)
            r4.jump()
            if r4.getwinhome():
                br4.setactive(0)
            gotodecide(r4,y1,y2,y3,y4,b1,b2,b3,b4,g1,g2,g3,g4)
            t2.draw(win)
            k = win.getMouse()
            while not(button_click.click(k)==1):
                k = win.getMouse()
            ran = randrange(1,7)
            t2.undraw()
            dice_roll.setNumber(ran)
    br1.setactive(r1.whether())
    br2.setactive(r2.whether())
    br3.setactive(r3.whether())
    br4.setactive(r4.whether())
    br1.draw(win)
    br2.draw(win)
    br3.draw(win)
    br4.draw(win)
    if not(r1.athome() and r2.athome() and r3.athome and r4.athome())\
        and (r1.whether() or r2.whether()\
        or r3.whether() or r4.whether()):
        s = win.getMouse()
        while not(br1.click(s) or br2.click(s) or br3.click(s)or \
                    br4.click(s)):
            s = win.getMouse()
        br1.undraw()
        br2.undraw()
        br3.undraw()
        br4.undraw()
        if br1.click(s):
            r1.move(ran)
            r1.jump()
            if r1.getwinhome():
                br1.setactive(0)
            gotodecide(r1,y1,y2,y3,y4,b1,b2,b3,b4,g1,g2,g3,g4)
        elif br2.click(s):
            r2.move(ran)
            r2.jump()
            if r2.getwinhome():
                br2.setactive(0)
            gotodecide(r2,y1,y2,y3,y4,b1,b2,b3,b4,g1,g2,g3,g4)
        elif br3.click(s):
            r3.move(ran)
            r3.jump()
            if r3.getwinhome():
                br3.setactive(0)
            gotodecide(r3,y1,y2,y3,y4,b1,b2,b3,b4,g1,g2,g3,g4)
        elif br4.click(s):
            r4.move(ran)
            r4.jump()
            if r4.getwinhome():
                br4.setactive(0)
            gotodecide(r4,y1,y2,y3,y4,b1,b2,b3,b4,g1,g2,g3,g4)
    br1.setactive(r1.notgetwinhome())
    br2.setactive(r2.notgetwinhome())
    br3.setactive(r3.notgetwinhome())
    br4.setactive(r4.notgetwinhome())

def gotodecide(r1,y1,y2,y3,y4,b1,b2,b3,b4,g1,g2,g3,g4):
    y1.decide(r1)
    y2.decide(r1)
    y3.decide(r1)
    y4.decide(r1)
    b1.decide(r1)
    b2.decide(r1)
    b3.decide(r1)
    b4.decide(r1)
    g1.decide(r1)
    g2.decide(r1)
    g3.decide(r1)
    g4.decide(r1)
