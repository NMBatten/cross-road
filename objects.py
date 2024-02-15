from pygame.locals import *
import pygame, random
from constants import Constants as con

class Slot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((con.SCREEN_WIDTH, 30))
        self.surf.fill(con.road_gray)
        self.rect = self.surf.get_rect()

    def update(self):
        pass

    def generate_obstacle(self, start_pos=None):
        new_object = Truck(self)


class Truck(pygame.sprite.Sprite):
    def __init__(self, slot, start_pos = None):
        super().__init__()
        self.surf = pygame.Surface((random.randint(20, 40), 20))
        self.surf.fill(con.truck_color)
        self.rect = self.surf.get_rect()

        vec = pygame.math.Vector2

        self.pos = vec((slot.rect.left, slot.rect.center.y -15))

    def update(self):
        self.pos.x += con.TRUCK_SPEED
