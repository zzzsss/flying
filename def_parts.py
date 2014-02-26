# def_parts for the flying chess
from class_parts import *
from graphics import *
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
    
        
        
            
