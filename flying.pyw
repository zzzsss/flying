# The flying chess
from graphics import *
from class_parts import *
from time import *
from random import *
from draw_parts import *
from def_parts import *

def main():
    win = GraphWin('Flying Chess',700,700)
    win.setBackground('pink')
    win.setCoords(-1000,-1000,1000,1000)
    drawcover(win)
    win.setCoords(-18,-18,18,18)
    draw_background(win)
    
    button_click = Button(win,Point(3,7),3,2,'click')
    dice_roll = Dice(Point(-3,7),3,1,win)
    button_click.draw(win)
    dice_roll.setColor('red')
    dice_roll.draw()
    br1 = Button(win,Point(6,4),3,1.5,'r1')
    br2 = Button(win,Point(10,4),3,1.5,'r2')
    br3 = Button(win,Point(6,2),3,1.5,'r3')
    br4 = Button(win,Point(10,2),3,1.5,'r4')
    by1 = Button(win,Point(6,4),3,1.5,'y1')
    by2 = Button(win,Point(10,4),3,1.5,'y2')
    by3 = Button(win,Point(6,2),3,1.5,'y3')
    by4 = Button(win,Point(10,2),3,1.5,'y4')
    bb1 = Button(win,Point(6,4),3,1.5,'b1')
    bb2 = Button(win,Point(10,4),3,1.5,'b2')
    bb3 = Button(win,Point(6,2),3,1.5,'b3')
    bb4 = Button(win,Point(10,2),3,1.5,'b4')
    bg1 = Button(win,Point(6,4),3,1.5,'g1')
    bg2 = Button(win,Point(10,4),3,1.5,'g2')
    bg3 = Button(win,Point(6,2),3,1.5,'g3')
    bg4 = Button(win,Point(10,2),3,1.5,'g4')

    #draw the pieces
    r1 = Piece('red',1,win)
    r2 = Piece('red',2,win)
    r3 = Piece('red',3,win)
    r4 = Piece('red',4,win)
    y1 = Piece('yellow',1,win)
    y2 = Piece('yellow',2,win)
    y3 = Piece('yellow',3,win)
    y4 = Piece('yellow',4,win)
    b1 = Piece('blue',1,win)
    b2 = Piece('blue',2,win)
    b3 = Piece('blue',3,win)
    b4 = Piece('blue',4,win)
    g1 = Piece('green',1,win)
    g2 = Piece('green',2,win)
    g3 = Piece('green',3,win)
    g4 = Piece('green',4,win)
    k1 = Circle(Point(16,16),0.5)
    k1.setFill('red')
    k2 = Circle(Point(16,-16),0.5)
    k2.setFill('yellow')
    k3 = Circle(Point(-16,-16),0.5)
    k3.setFill('blue')
    k4 = Circle(Point(-16,16),0.5)
    k4.setFill('green')
    
    #start to play(assuming that red is the starter)
    n = 0
    while not((r1.getwinhome() and r2.getwinhome()\
               and r3.getwinhome() and r4.getwinhome())or\
              (y1.getwinhome() and y2.getwinhome()\
               and y3.getwinhome() and y4.getwinhome())or\
              (b1.getwinhome() and b2.getwinhome()\
               and b3.getwinhome() and b4.getwinhome())or\
              (g1.getwinhome() and g2.getwinhome()\
               and g3.getwinhome() and g4.getwinhome())):
        n = n + 1
        
        if n % 4 == 1: #for red to go
            k1.draw(win)
            thelist = [win,dice_roll,br1,br2,br3,br4,r1,r2,r3,r4,\
                       y1,y2,y3,y4,b1,b2,b3,b4,g1,g2,g3,g4,button_click]
            run(thelist)
            k1.undraw()

        elif n % 4 == 2: #for yellow to go
            k2.draw(win)
            thelist = [win,dice_roll,by1,by2,by3,by4,y1,y2,y3,y4,\
                       r1,r2,r3,r4,b1,b2,b3,b4,g1,g2,g3,g4,button_click]
            run(thelist)
            k2.undraw()

        elif n % 4 == 3: #for blue to go
            k3.draw(win)
            thelist = [win,dice_roll,bb1,bb2,bb3,bb4,b1,b2,b3,b4,\
                       y1,y2,y3,y4,r1,r2,r3,r4,g1,g2,g3,g4,button_click]
            run(thelist)
            k3.undraw()

        if n % 4 == 0: #for green to go
            k4.draw(win)
            thelist = [win,dice_roll,bg1,bg2,bg3,bg4,g1,g2,g3,g4,\
                       y1,y2,y3,y4,b1,b2,b3,b4,r1,r2,r3,r4,button_click]
            run(thelist)
            k4.undraw()

    #The end of the game
    if r1.getwinhome() and r2.getwinhome() and\
       r3.getwinhome() and r4.getwinhome():
        winner = 'red'
    elif y1.getwinhome() and y2.getwinhome() and\
         y3.getwinhome() and y4.getwinhome():
        winner = 'yellow'
    elif b1.getwinhome() and b2.getwinhome() and\
         b3.getwinhome() and b4.getwinhome():
        winner = 'blue'
    else:
        winner = 'green'

    win.delete('all')
    result = Text(Point(0,5),'The winner is %s'%(winner))
    result.setSize(36)
    result.draw(win)
    more = Text(Point(0,-10),\
                'Wanna play more games? Use Python to program one...')
    more.draw(win)

    quit_button = Button(win,Point(0,0),6,3,'quit')
    quit_button.draw(win)
    again_button = Button(win,Point(0,-5),6,3,'again')
    again_button.draw(win)

    k = win.getMouse()
    while not(quit_button.click(k) or again_button.click(k)):
        k = win.getMouse()
    if quit_button.click(k):
        win.close()
    else:
        win.close()
        main()

if __name__ == "__main__":
    main()
