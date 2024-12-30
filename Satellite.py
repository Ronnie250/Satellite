import pgzrun
import random

WIDTH = 800
HEIGHT = 500

sats = []

for i in range(10):
    satellite = Actor("satellite")
    satellite.x=random.randint(20, 780)
    satellite.y=random.randint(20, 480)
    sats.append(satellite)

def draw():
    screen.blit("background", (0,0))
    for i in sats:
        i.draw()

pgzrun.go()