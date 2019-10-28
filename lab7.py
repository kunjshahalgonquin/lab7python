
from gfxhat import lcd, backlight
import Lab7Librarypython

x=y=0
w=h=10
vx=vy=5
sx=127-w
sy=63-h
backlight.set_all(0, 100, 0)
backlight.show()
lcd.clear()
ball =  [
    [0,0,0,1,1,0,0,0],
    [0,0,1,1,1,1,0,0],
    [0,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,0],
    [0,0,1,1,1,1,0,0],
    [0,0,0,1,1,0,0,0]
    ]
f1=ball 
quit=False
while not quit:
    Lab7Librarypython.main(f1,x,y)
    x,y=Lab7Librarypython.moveObj(x,y,vx,vy) 
    x,y=Lab7Librarypython.collision(f1,x,y,vx,vy,sx,sy,w,h)



