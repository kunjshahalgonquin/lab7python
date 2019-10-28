from gfxhat import lcd, backlight
import time

def displayObject(obj,x,y):
    
    i=0
    for line in obj:
        j=0
        for pixel in line:
            lcd.set_pixel(x+j,y+i,pixel)
            j=j+1
        i=i+1
    lcd.show()
    
def eraseObject(obj,x,y):
    i=0
    for line in obj:
        j=0
        for pixel in line:
            if pixel == 1: pixel = 0
            lcd.set_pixel(x+j,y+i,pixel)
            j=j+1
        i=i+1

def moveObj(x,y,vx,vy):
    x=x+vx
    y=y+vy
    return x,y
def collision(f1,x,y,vx,vy,sx,sy,w,h):
  
    if y>=sy:
        ch=False
        while not ch:
            if x<=sx and y>=0:
                x=x+vx+3  
                y=y-vy
                main(f1,x,y)
            else:
                ch=True
    elif x>=sx and y>0:
        ch=False
        while not ch:
            x=x-vx
            y=y-vy
            if x>=0 and y>=0:
                main(f1,x,y)
            else:
                ch=True
    elif y<=0:
        ch=False
        while not ch:
            x=x-vx-3
            y=y+vy
            if x>=0 and y<=sy:
                main(f1,x,y)
            else:
                ch=True
    elif x<=0:
        ch=False
        while not ch:
            if x<=sx and y<=sy:
                x=x+vx
                y=y+vy
                main(f1,x,y)
            else:
                        
    return x,y
def main(f1,x,y):
    displayObject(f1,x,y)
    eraseObject(f1,x,y)
    time.sleep(0.2)


