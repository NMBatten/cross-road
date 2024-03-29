from pygame.locals import *
import pygame, random
from constants import Constants as con
from groups import Groups

class Slot(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.surf = pygame.Surface((con.SCREEN_WIDTH, 30))
        self.surf.fill(con.grass_green)
        self.rect = self.surf.get_rect()
        # print(pos)
        self.rect.center = pos
        self.type = "grass"
        self.gen_timer = random.randint(5, 30)

    def update(self):
        pass

    def kill_condition(self, player):
        return False

class RoadSlot(Slot):
    def __init__(self, pos):
        super().__init__(pos)
        self.surf.fill(con.road_gray)
        self.object_speed = random.choice([-1, 1]) * con.TRUCK_SPEED
        self.type = "road"

    def generate_obstacle(self, random_start=False):
        new_object = Truck(self, random_start)
        self.gen_timer = random.randint(con.GENRANGE_START, con.GENRANGE_END) + abs(new_object.rect.left - new_object.rect.right)
        return new_object, [Groups.all_sprites, Groups.deadly_obstacles]

    def kill_condition(self, player):
        # This checks whether or not the player should die based
        # on the type of slot
        hits = pygame.sprite.spritecollide(player, Groups.deadly_obstacles, False)
        # print("you dead")
        if hits:
            return True

class RiverSlot(Slot):
    def __init__(self, pos):
        super().__init__(pos)
        self.surf.fill(con.river_blue)
        self.object_speed = random.choice([-1, 1]) * con.LOG_SPEED
        self.type = "river"

    def generate_obstacle(self, random_start=False):
        new_object = Log(self, random_start)
        self.gen_timer = random.randint(con.GENRANGE_START, con.GENRANGE_END) + abs(new_object.rect.left - new_object.rect.right)
        return new_object, [Groups.all_sprites, Groups.logs]

    def kill_condition(self, player):
        # Checks if the player is on a log or not
        # If they're not, they die
        if not pygame.sprite.spritecollideany(player, Groups.logs):
            return True
        else:
            return False


class Truck(pygame.sprite.Sprite):
    def __init__(self, slot, random_start):
        super().__init__()
        self.surf = pygame.Surface((random.choice([30, 40, 50]), 20))
        self.surf.fill(con.truck_color)
        self.rect = self.surf.get_rect()
        self.slot = slot

        if not random_start:
            if self.slot.object_speed > 0:
                xval = self.slot.rect.left
            else:
                xval = self.slot.rect.right
            self.rect.center = ((xval, slot.rect.centery))
        else:
            self.rect.center = (( random.randint(0, con.SCREEN_WIDTH), slot.rect.centery ))

    def update(self):
        self.rect.centerx += self.slot.object_speed

class Log(pygame.sprite.Sprite):
    def __init__(self, slot, random_start):
        super().__init__()
        self.surf = pygame.Surface((random.choice([50, 60, 70, 80]), 20))
        self.surf.fill(con.log_brown)
        self.rect = self.surf.get_rect()
        self.slot = slot

        if not random_start:
            if self.slot.object_speed > 0:
                xval = self.slot.rect.left - 20
            else:
                xval = self.slot.rect.right + 20
            self.rect.center = ((xval, slot.rect.centery))
        else:
            self.rect.center = (( random.randint(0, con.SCREEN_WIDTH), slot.rect.centery ))

    def update(self):
        self.rect.centerx += self.slot.object_speed
