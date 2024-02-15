from pygame.locals import *
import pygame, random
from constants import Constants as con
from main import Groups

class Slot(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.surf = pygame.Surface((con.SCREEN_WIDTH, 30))
        self.surf.fill(con.grass_green)
        self.rect = self.surf.get_rect(center = pos)

    def update(self):
        pass

    def kill_condition(self):
        return False

class RoadSlot(Slot):
    def __init__(self, pos):
        super().__init__(pos)
        self.surf.fill(con.road_gray)
        self.object_speed = random.choice([-1, 1]) * con.TRUCK_SPEED

    def generate_obstacle(self, random_start=False):
        new_object = Truck(self, random_start)

    def kill_condition(self, player):
        # This checks whether or not the player should die based
        # on the type of slot
        hits = pygame.sprite.spritecollide(player, Groups.deadly_obstacles, False)
        if hits:
            return True


class Truck(pygame.sprite.Sprite):
    def __init__(self, slot, random_start):
        super().__init__()
        self.surf = pygame.Surface((random.randint(30, 50), 20))
        self.surf.fill(con.truck_color)
        self.rect = self.surf.get_rect()
        self.slot = slot

        vec = pygame.math.Vector2
        if not random_start:
            if self.slot.object_speed > 0:
                xval = self.slot.rect.left
            else:
                xval = self.slot.rect.right
            self.pos = vec((xval, slot.rect.center.y))
        else:
            self.pos = vec(( random.randint(0, con.SCREEN_WIDTH), slot.rect.center.y ))

    def update(self):
        self.pos.x += self.slot.object_speed
