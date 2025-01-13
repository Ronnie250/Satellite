import pgzrun
import random

WIDTH = 800
HEIGHT = 500

sats = []
lines=[]
next=0
ts=10

for i in range(ts):
    satellite = Actor("satellite")
    satellite.x=random.randint(40, 760)
    satellite.y=random.randint(40, 460)
    sats.append(satellite)

def draw():
    screen.blit("background", (0,0))
    numbers=1
    for i in sats:
        i.draw()
        screen.draw.text(str(numbers), (i.x,i.y+20))
        numbers=numbers+1
    for line in lines:
        screen.draw.line(line[0],line[1],"red")
        

def on_mouse_down(pos):
    global sats, lines, next
    if next < ts:
        if sats[next].collidepoint(pos):
            if next>0:
                lines.append((sats[next-1].pos,sats[next].pos))
                print(lines)
            next=next+1
        else:
            lines=[]
            next=0

def update():
    pass

pgzrun.go()