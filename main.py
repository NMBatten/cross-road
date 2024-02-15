from pygame.locals import *
from constants import Constants as con
import pygame, time, sys, random
from player import Player
from objects import Slot, RoadSlot
from groups import Groups

pygame.init()
vec = pygame.math.Vector2

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((con.SCREEN_WIDTH, con.SCREEN_HEIGHT))
pygame.display.set_caption("Don't get hit :)")

p1 = Player(vec)

# This variable tracks which slot is on top so the next slot can
# be put on top of it
top_slot = Slot((int(con.SCREEN_WIDTH / 2), con.SCREEN_HEIGHT-15))

Groups.all_sprites.add(p1)

def generate_slot(slot_type):
    # generates a new slot on top of the stack
    if slot_type == "grass":
        slot = Slot(slot_pos())
    elif slot_type == "road":
        slot = RoadSlot(slot_pos())
    global top_slot
    top_slot = slot
    # print(top_slot)
    Groups.all_sprites.add(slot)
    Groups.slots.add(slot)

def slot_pos():
    return (int(con.SCREEN_WIDTH / 2), top_slot.rect.top - 15)

def generate_block():
    # generates a random of slots of a certain type sandwiched
    # between two strips of grass
    generate_slot("grass")
    for index in range(random.randint(3, 8)):
        generate_slot("road")
    # generate_slot("grass")


def setup():
    # Sets up blocks until the screen is filled (or slightly over)
    # Should initialize with some objects already in the middle
    while top_slot.rect.top > - 100:
        generate_block()
    for slot in Groups.slots:
        if slot.type != "grass":
            for index in range(random.randint(1, 4)):
                object, associated_groups = slot.generate_obstacle(True)
                for group in associated_groups:
                    group.add(object)

setup()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT]:
                p1.jump(event.key)

    displaysurface.fill(con.grass_green)

    for object in Groups.deadly_obstacles:
        object.update()

    for entity in Groups.all_sprites:
        displaysurface.blit(entity.surf, entity.rect)

    pygame.display.update()
    FramePerSec.tick(con.FPS)
