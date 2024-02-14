from pygame.locals import *
from constants import Constants as con
import pygame, time, sys

pygame.init()
vec = pygame.math.Vector2

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((con.WIDTH, con.HEIGHT))
pygame.display.set_caption("Don't get hit :)")


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    displaysurface.fill(con.grass_green)

    pygame.display.update()
    FramePerSec.tick(con.FPS)
