from pygame.locals import *
from constants import Constants as con
import pygame, time, sys
from player import Player
from objects import Slot, Truck

pygame.init()
vec = pygame.math.Vector2

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((con.WIDTH, con.HEIGHT))
pygame.display.set_caption("Don't get hit :)")

p1 = Player(vec)

class Groups:
    obstacles = pygame.sprite.Group()

def generate_slot():
    # generates a new slot on top of the stack
    pass



while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    displaysurface.fill(con.grass_green)

    pygame.display.update()
    FramePerSec.tick(con.FPS)
