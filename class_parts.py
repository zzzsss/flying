# The parts of the flying chess
from graphics import *
from def_parts import *
from time import *

class Button:
    def __init__(self,win,center,width,height,label):
        self.label = Text(center,label)
        self.xmin,self.xmax = center.getX() - 0.5 * width ,\
                              center.getX() + 0.5 * width
        self.ymin,self.ymax = center.getY() - 0.5 * height,\
                              center.getY() + 0.5 * height
        self.rect = Rectangle(Point(self.xmin,self.ymin),\
                              Point(self.xmax,self.ymax))
        self.rect.setFill('grey')
        self.rect.setWidth(2)
        self.active = 1
    def setactive(self,n):
        self.active = n
    def click(self,x):
        if self.xmin<=x.getX()<=self.xmax and\
           self.ymin<=x.getY()<=self.ymax and self.active == 1:
            return 1
        else:
            return 0
    def draw(self,win):
        if self.active == 1:
            self.rect.draw(win)
            self.label.draw(win)
    def undraw(self):
        if self.active == 1:
            self.rect.undraw()
            self.label.undraw()

class Dice:
    def __init__(self,center,length,number,win):
        self.win = win
        length = float(length)
        self.number = number
        self.center = center
        self.xmin = center.getX()-0.5 * length
        self.xmax = center.getX()+0.5 * length
        self.ymin = center.getY()-0.5 * length
        self.ymax = center.getY()+0.5 * length
        self.rect = Rectangle(Point(self.xmin,self.ymin),\
                              Point(self.xmax,self.ymax))
        self.rect.setFill('grey')
        self.rect.setWidth(2)
        self.c1 = Circle(center,0.05*length)
        self.c2 = Circle(Point(center.getX()-length/6,\
                         center.getY()+length/3),0.05*length)
        self.c3 = Circle(Point(center.getX()-length/6,\
                               center.getY()),0.05*length)
        self.c4 = Circle(Point(center.getX()-length/6,\
                         center.getY()-length/3),0.05*length)
        self.c5 = Circle(Point(center.getX()+length/6,\
                         center.getY()+length/3),0.05*length)
        self.c6 = Circle(Point(center.getX()+length/6,\
                               center.getY()),0.05*length)
        self.c7 = Circle(Point(center.getX()+length/6,\
                         center.getY()-length/3),0.05*length)
    def setNumber(self,n):
        self.undraw()
        self.number = n
        self.draw()
    def draw(self):
        self.rect.draw(self.win)
        if self.number == 1:
            self.c1.draw(self.win)
        elif self.number == 2:
            self.c4.draw(self.win)
            self.c5.draw(self.win)
        elif self.number == 3:
            self.c1.draw(self.win)
            self.c4.draw(self.win)
            self.c5.draw(self.win)
        elif self.number == 4:
            self.c2.draw(self.win)
            self.c4.draw(self.win)
            self.c5.draw(self.win)
            self.c7.draw(self.win)
        elif self.number == 5:
            self.c1.draw(self.win)
            self.c2.draw(self.win)
            self.c4.draw(self.win)
            self.c5.draw(self.win)
            self.c7.draw(self.win)
        else:
            self.c2.draw(self.win)
            self.c3.draw(self.win)
            self.c4.draw(self.win)
            self.c5.draw(self.win)
            self.c6.draw(self.win)
            self.c7.draw(self.win)
    def setBack(self,color):
        self.rect.setFill(color)
    def setWidth(self,x):
        self.rect.setWidth(x)
    def setColor(self,color):
        self.c1.setFill(color)
        self.c2.setFill(color)
        self.c3.setFill(color)
        self.c4.setFill(color)
        self.c5.setFill(color)
        self.c6.setFill(color)
        self.c7.setFill(color)
    def undraw(self):
        self.rect.undraw()
        if self.number == 1:
            self.c1.undraw()
        elif self.number == 2:
            self.c4.undraw()
            self.c5.undraw()
        elif self.number == 3:
            self.c1.undraw()
            self.c4.undraw()
            self.c5.undraw()
        elif self.number == 4:
            self.c2.undraw()
            self.c4.undraw()
            self.c5.undraw()
            self.c7.undraw()
        elif self.number == 5:
            self.c1.undraw()
            self.c2.undraw()
            self.c4.undraw()
            self.c5.undraw()
            self.c7.undraw()
        else:
            self.c2.undraw()
            self.c3.undraw()
            self.c4.undraw()
            self.c5.undraw()
            self.c6.undraw()
            self.c7.undraw()

class Square:
    def __init__(self,center,length,color,win):
        self.center = center
        self.length = length
        self.x = center.getX()
        self.y = center.getY()
        self.rec = Rectangle(Point(self.x-0.5*length,self.y-0.5*length),\
                             Point(self.x+0.5*length,self.y+0.5*length))
        self.rec.setFill(color)
        self.rec.draw(win)
    def undraw(self):
        self.rec.undraw()
    def setFill(self,color):
        self.rec.setFill(color)

class Pos:
    def __init__(self,number,win):
        self.number = number
        self.win = win
        if number==1: center = Point(6,14)
        elif number==2: center = Point(7,12)
        elif number==3: center = Point(7,10)
        elif number==4: center = Point(6,8)
        elif number==5: center = Point(8,6)
        elif number==6: center = Point(10,7)
        elif number==7: center = Point(12,7)
        elif number==8: center = Point(14,6)
        elif number==9: center = Point(15,4)
        elif number==10: center = Point(15,2)
        elif number==11: center = Point(15,0)
        elif number==12: center = Point(15,-2)
        elif number==13: center = Point(15,-4)
        elif number==14: center = Point(14,-6)
        elif number==15: center = Point(12,-7)
        elif number==16: center = Point(10,-7)
        elif number==17: center = Point(8,-6)
        elif number==18: center = Point(6,-8)
        elif number==19: center = Point(7,-10)
        elif number==20: center = Point(7,-12)
        elif number==21: center = Point(6,-14)
        elif number==22: center = Point(4,-15)
        elif number==23: center = Point(2,-15)
        elif number==24: center = Point(0,-15)
        elif number==25: center = Point(-2,-15)
        elif number==26: center = Point(-4,-15)
        elif number==27: center = Point(-6,-14)
        elif number==28: center = Point(-7,-12)
        elif number==29: center = Point(-7,-10)
        elif number==30: center = Point(-6,-8)
        elif number==31: center = Point(-8,-6)
        elif number==32: center = Point(-10,-7)
        elif number==33: center = Point(-12,-7)
        elif number==34: center = Point(-14,-6)
        elif number==35: center = Point(-15,-4)
        elif number==36: center = Point(-15,-2)
        elif number==37: center = Point(-15,0)
        elif number==38: center = Point(-15,2)
        elif number==39: center = Point(-15,4)
        elif number==40: center = Point(-14,6)
        elif number==41: center = Point(-12,7)
        elif number==42: center = Point(-10,7)
        elif number==43: center = Point(-8,6)
        elif number==44: center = Point(-6,8)
        elif number==45: center = Point(-7,10)
        elif number==46: center = Point(-7,12)
        elif number==47: center = Point(-6,14)
        elif number==48: center = Point(-4,15)
        elif number==49: center = Point(-2,15)
        elif number==50: center = Point(0,15)
        elif number==51: center = Point(2,15)
        elif number==52: center = Point(4,15)
        elif number==101: center = Point(0,12)
        elif number==102: center = Point(0,10)
        elif number==103: center = Point(0,8)
        elif number==104: center = Point(0,6)
        elif number==105: center = Point(0,4)
        elif number==106: center = Point(12,0)
        elif number==107: center = Point(10,0)
        elif number==108: center = Point(8,0)
        elif number==109: center = Point(6,0)
        elif number==110: center = Point(4,0)
        elif number==111: center = Point(0,-12)
        elif number==112: center = Point(0,-10)
        elif number==113: center = Point(0,-8)
        elif number==114: center = Point(0,-6)
        elif number==115: center = Point(0,-4)
        elif number==116: center = Point(-12,0)
        elif number==117: center = Point(-10,0)
        elif number==118: center = Point(-8,0)
        elif number==119: center = Point(-6,0)
        elif number==120: center = Point(-4,0)
        elif number==201: center = Point(12,15) #r1
        elif number==202: center = Point(15,15) #r2
        elif number==203: center = Point(12,12) #r3
        elif number==204: center = Point(15,12) #r4
        elif number==205: center = Point(9,16)  #rs
        elif number==206: center = Point(0,2)   #rh
        elif number==207: center = Point(12,-12)
        elif number==208: center = Point(15,-12)
        elif number==209: center = Point(12,-15)
        elif number==210: center = Point(15,-15)
        elif number==211: center = Point(16,-9)
        elif number==212: center = Point(2,0)
        elif number==213: center = Point(-15,-12)
        elif number==214: center = Point(-12,-12)
        elif number==215: center = Point(-15,-15)
        elif number==216: center = Point(-12,-15)
        elif number==217: center = Point(-9,-16)
        elif number==218: center = Point(0,-2)
        elif number==219: center = Point(-15,15)
        elif number==220: center = Point(-12,15)
        elif number==221: center = Point(-15,12)
        elif number==222: center = Point(-12,12)
        elif number==223: center = Point(-16,9)
        elif number==224: center = Point(-2,0)
        
        self.center = center
        self.x = center.getX()
        self.y = center.getY()
        self.circle = Circle(self.center,0.8)
        self.circle.setWidth(2)
        self.circle.setFill('white')
    def draw(self):
        self.circle.draw(self.win)
    def undraw(self):
        self.circle.undraw()
    def order(self):
        return self.number
    def center(self):
        return self.center

class Piece:
    def __init__(self,color,number,win):
        self.win = win
        self.color = color
        self.number = number
        if color == 'red':
            self.x = Pos(200+number,win).x
            self.y = Pos(200+number,win).y
        elif color == 'yellow':
            self.x = Pos(206+number,win).x
            self.y = Pos(206+number,win).y
        elif color == 'blue':
            self.x = Pos(212+number,win).x
            self.y = Pos(212+number,win).y    
        else:
            self.x = Pos(218+number,win).x
            self.y = Pos(218+number,win).y
        self.position = Point(self.x,self.y)
        self.t = Text(self.position,'%d'%(number))
        self.circle = Circle(self.position,0.6)
        self.circle.setFill(color)
        self.draw()
        self.track = self.tracking()
        self.win = win
        self.able = 0
    def number(self):
        return number
    def getable(self):
        return self.able
    def setwin(self):
        self.win = 1
    def getwin(self):
        return self.win
    def draw(self):
        self.circle.draw(self.win)
        self.t.draw(self.win)
    def undraw(self):
        self.circle.undraw()
        self.t.undraw()
    def out_continue(self,k):
        if k == 6:
            return 1
        else:
            return 0
    def getwinhome(self):
        if self.color == 'red':
            if self.x == Pos(206,self.win).x and self.y == Pos(206,self.win).y:
                return 1
            else: return 0
        elif self.color == 'yellow':
            if self.x == Pos(212,self.win).x and self.y == Pos(212,self.win).y:
                return 1
            else: return 0
        elif self.color == 'blue':
            if self.x == Pos(218,self.win).x and self.y == Pos(218,self.win).y:
                return 1
            else: return 0
        else:
            if self.x == Pos(224,self.win).x and self.y == Pos(224,self.win).y:
                return 1
            else: return 0
    def notgetwinhome(self):
        if self.getwinhome() == 1:
            return 0
        else:
            return 1
    def getbackhome(self):
        if self.color == 'red':
            self.undraw()
            self.x = Pos(200 + self.number,self.win).x
            self.y = Pos(200 + self.number,self.win).y
            self.track = self.tracking()
            self.circle = Circle(Point(self.x,self.y),0.6)
            self.circle.setFill(self.color)
            self.t = Text(Point(self.x,self.y),'%d'%(self.number))
            self.draw()
        elif self.color == 'yellow':
            self.undraw()
            self.x = Pos(206 + self.number,self.win).x
            self.y = Pos(206 + self.number,self.win).y
            self.track = self.tracking()
            self.circle = Circle(Point(self.x,self.y),0.6)
            self.circle.setFill(self.color)
            self.t = Text(Point(self.x,self.y),'%d'%(self.number))
            self.draw()
        elif self.color == 'blue':
            self.undraw()
            self.x = Pos(212 + self.number,self.win).x
            self.y = Pos(212 + self.number,self.win).y
            self.track = self.tracking()
            self.circle = Circle(Point(self.x,self.y),0.6)
            self.circle.setFill(self.color)
            self.t = Text(Point(self.x,self.y),'%d'%(self.number))
            self.draw()
        else:
            self.undraw()
            self.x = Pos(218 + self.number,self.win).x
            self.y = Pos(218 + self.number,self.win).y
            self.track = self.tracking()
            self.circle = Circle(Point(self.x,self.y),0.6)
            self.circle.setFill(self.color)
            self.t = Text(Point(self.x,self.y),'%d'%(self.number))
            self.draw()
        self.able = 0
    def athome(self):
        if self.color == 'red':
            if self.x == Pos(200 + self.number,self.win).x and\
               self.y == Pos(200 + self.number,self.win).y:
                return 1
            else: return 0
        elif self.color == 'yellow':
            if self.x == Pos(206 + self.number,self.win).x and\
               self.y == Pos(206 + self.number,self.win).y:
                return 1
            else: return 0
        elif self.color == 'blue':
            if self.x == Pos(212 + self.number,self.win).x and\
               self.y == Pos(212 + self.number,self.win).y:
                return 1
            else: return 0
        else:
            if self.x == Pos(218 + self.number,self.win).x and\
               self.y == Pos(218 + self.number,self.win).y:
                return 1
            else: return 0
    def notathome(self):
        if self.athome() == 1:
            return 0
        else:
            return 1
    def getouthome(self):
        if self.color == 'red':
            self.undraw()
            self.x = Pos(205,self.win).x
            self.y = Pos(205,self.win).y
            self.track = self.tracking()
            self.circle = Circle(Point(self.x,self.y),0.6)
            self.circle.setFill(self.color)
            self.t = Text(Point(self.x,self.y),'%d'%(self.number))
            self.draw()
        elif self.color == 'yellow':
            self.undraw()
            self.x = Pos(211,self.win).x
            self.y = Pos(211,self.win).y
            self.track = self.tracking()
            self.circle = Circle(Point(self.x,self.y),0.6)
            self.circle.setFill(self.color)
            self.t = Text(Point(self.x,self.y),'%d'%(self.number))
            self.draw()
        elif self.color == 'blue':
            self.undraw()
            self.x = Pos(217,self.win).x
            self.y = Pos(217,self.win).y
            self.track = self.tracking()
            self.circle = Circle(Point(self.x,self.y),0.6)
            self.circle.setFill(self.color)
            self.t = Text(Point(self.x,self.y),'%d'%(self.number))
            self.draw()
        else:
            self.undraw()
            self.x = Pos(223,self.win).x
            self.y = Pos(223,self.win).y
            self.track = self.tracking()
            self.circle = Circle(Point(self.x,self.y),0.6)
            self.circle.setFill(self.color)
            self.t = Text(Point(self.x,self.y),'%d'%(self.number))
            self.draw()
        self.able = 1
    def tracking(self):
        for i in range(1,53):
            if self.x == Pos(i,self.win).x and self.y == Pos(i,self.win).y:
                return i
        for i in range(101,121):
            if self.x == Pos(i,self.win).x and self.y == Pos(i,self.win).y:
                return i
        for i in range(201,225):
            if self.x == Pos(i,self.win).x and self.y == Pos(i,self.win).y:
                return i
    def move(self,n):
        if self.athome():
            self.getouthome()
        else:    
            for i in range(1,n+1):
                k = 0
                sleep(0.5)
                self.undraw()
                if 101<=self.track<=120 or\
                   (self.track == 11 and self.color == 'yellow') or\
                   (self.track == 24 and self.color == 'blue') or \
                   (self.track == 37 and self.color == 'green') or\
                   (self.track == 50 and self.color == 'red')or\
                   self.track == 206 or self.track == 212 or\
                   self.track == 218 or self.track == 224:
                    if self.track == 206 or self.track == 212 or\
                       self.track == 218 or self.track == 224:
                        k = i - 1
                        break
                    else:
                        self.x = Pos(splus(self.track,self.color),self.win).x
                        self.y = Pos(splus(self.track,self.color),self.win).y
                        self.track = self.tracking()
                        self.circle = Circle(Point(self.x,self.y),0.6)
                        self.circle.setFill(self.color)
                        self.t = Text(Point(self.x,self.y),'%d'%(self.number))
                        self.draw()
                else:
                    self.x = Pos(plus(self.track,self.color),self.win).x
                    self.y = Pos(plus(self.track,self.color),self.win).y
                    self.track = self.tracking()
                    self.circle = Circle(Point(self.x,self.y),0.6)
                    self.circle.setFill(self.color)
                    self.t = Text(Point(self.x,self.y),'%d'%(self.number))
                    self.draw()
            if k != 0 and k != n:
                self.undraw()
                if self.color == 'red':
                    self.x = Pos(105,self.win).x
                    self.y = Pos(105,self.win).y
                elif self.color == 'yellow':
                    self.x = Pos(110,self.win).x
                    self.y = Pos(110,self.win).y
                elif self.color == 'blue':
                    self.x = Pos(115,self.win).x
                    self.y = Pos(115,self.win).y
                else:
                    self.x = Pos(120,self.win).x
                    self.y = Pos(120,self.win).y
                self.track = self.tracking()
                self.circle = Circle(Point(self.x,self.y),0.6)
                self.circle.setFill(self.color)
                self.t = Text(Point(self.x,self.y),'%d'%(self.number))
                self.draw()

                if k != n-1:
                    for i in range(1,n-k):
                        sleep(0.5)
                        self.undraw()
                        self.x = Pos(self.track-1,self.win).x
                        self.y = Pos(self.track-1,self.win).y
                        self.track = self.tracking()
                        self.circle = Circle(Point(self.x,self.y),0.6)
                        self.circle.setFill(self.color)
                        self.t = Text(Point(self.x,self.y),'%d'%(self.number))
                        self.draw()
    def decide(self,k):
        if self.tracking() == k.tracking():
            self.getbackhome()
    def whether(self):
        if self.athome() or self.getwinhome():
            return 0
        else:
            return 1
    def jump(self):
        if self.color == 'red':
            if 1<=self.track<=46 and self.track!=18 and\
               (self.track - 2) % 4 == 0 and self.track != 18:
                self.move(4)
            elif self.track == 18:
                self.undraw()
                self.x = Pos(30,self.win).x
                self.y = Pos(30,self.win).y
                self.track = self.tracking()
                self.circle = Circle(Point(self.x,self.y),0.6)
                self.circle.setFill(self.color)
                self.t = Text(Point(self.x,self.y),'%d'%(self.number))
                self.draw()
                self.move(4)
                
            if self.track == 18:
                self.undraw()
                self.x = Pos(30,self.win).x
                self.y = Pos(30,self.win).y
                self.track = self.tracking()
                self.circle = Circle(Point(self.x,self.y),0.6)
                self.circle.setFill(self.color)
                self.t = Text(Point(self.x,self.y),'%d'%(self.number))
                self.draw()
        elif self.color == 'yellow':
            if (14<=self.track<=52 or 1<=self.track<=7) and\
               (self.track - 3) % 4 == 0 and self.track != 31:
                self.move(4)
            elif self.track == 31:
                self.undraw()
                self.x = Pos(43,self.win).x
                self.y = Pos(43,self.win).y
                self.track = self.tracking()
                self.circle = Circle(Point(self.x,self.y),0.6)
                self.circle.setFill(self.color)
                self.t = Text(Point(self.x,self.y),'%d'%(self.number))
                self.draw()
                self.move(4)
                
            if self.track == 31:
                self.undraw()
                self.x = Pos(43,self.win).x
                self.y = Pos(43,self.win).y
                self.track = self.tracking()
                self.circle = Circle(Point(self.x,self.y),0.6)
                self.circle.setFill(self.color)
                self.t = Text(Point(self.x,self.y),'%d'%(self.number))
                self.draw()
        elif self.color == 'blue':
            if (27<=self.track<=52 or 1<=self.track<=20) and\
               self.track % 4 == 0 and self.track != 44:
                self.move(4)
            elif self.track == 44:
                self.undraw()
                self.x = Pos(4,self.win).x
                self.y = Pos(4,self.win).y
                self.track = self.tracking()
                self.circle = Circle(Point(self.x,self.y),0.6)
                self.circle.setFill(self.color)
                self.t = Text(Point(self.x,self.y),'%d'%(self.number))
                self.draw()
                self.move(4)
                
            if self.track == 44:
                self.undraw()
                self.x = Pos(4,self.win).x
                self.y = Pos(4,self.win).y
                self.track = self.tracking()
                self.circle = Circle(Point(self.x,self.y),0.6)
                self.circle.setFill(self.color)
                self.t = Text(Point(self.x,self.y),'%d'%(self.number))
                self.draw()
        else:
            if (40<=self.track<=52 or 1<=self.track<=33) and\
               (self.track - 1) % 4 == 0 and self.track != 5:
                self.move(4)
            elif self.track == 5:
                self.undraw()
                self.x = Pos(17,self.win).x
                self.y = Pos(17,self.win).y
                self.track = self.tracking()
                self.circle = Circle(Point(self.x,self.y),0.6)
                self.circle.setFill(self.color)
                self.t = Text(Point(self.x,self.y),'%d'%(self.number))
                self.draw()
                self.move(4)

            if self.track == 5:
                self.undraw()
                self.x = Pos(17,self.win).x
                self.y = Pos(17,self.win).y
                self.track = self.tracking()
                self.circle = Circle(Point(self.x,self.y),0.6)
                self.circle.setFill(self.color)
                self.t = Text(Point(self.x,self.y),'%d'%(self.number))
                self.draw()
                
