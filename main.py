from pygame.locals import *
from constants import Constants as con
import pygame, time, sys, random
from player import Player
from objects import Slot, Truck, RoadSlot

pygame.init()
vec = pygame.math.Vector2

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((con.WIDTH, con.HEIGHT))
pygame.display.set_caption("Don't get hit :)")

p1 = Player(vec)

# This variable tracks which slot is on top so the next slot can
# be put on top of it
top_slot = None

class Groups:
    all_sprites = pygame.sprite.Group()
    deadly_obstacles = pygame.sprite.Group()
    blocking_obstacles = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    slots = pygame.sprite.Group()

Groups.all_sprites.add(p1)

def generate_slot(slot_type):
    # generates a new slot on top of the stack
    if slot_type == "grass":
        slot = Slot(slot_pos())
    elif slot_type == "road":
        slot = RoadSlot(slot_pos())
    top_slot = slot
    Groups.all_sprites.add(slot)
    Groups.slots.add(slot)

def slot_pos():
    return top_slot.rect.top + 15

def generate_block():
    # generates a random of slots of a certain type sandwiched
    # between two strips of grass
    generate_slot("grass")
    for index in range(random.randint(3, 8)):
        generate_slot("road")
    generate_slot("grass")


def setup():
    # Sets up blocks until the screen is filled (or slightly over)
    # Should initialize with some objects already in the middle
    top_slot = Slot(vec((con.SCREEN_WIDTH / 2, con.SCREEN_HEIGHT-15)))
    while top_slot.rect.top > - 100:
        generate_block()
    for slot in Groups.slots:
        for index in range(random.randint(1, 4)):
            truck = Truck(slot, random_start=True)
            Groups.deadly_obstacles.add(truck)

setup()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    displaysurface.fill(con.grass_green)

    pygame.display.update()
    FramePerSec.tick(con.FPS)
