from pygame.locals import *
import pygame

class Slot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


class Truck(pygame.sprite.Sprite):
    def __init__(self, slot):
        super().__init__()
        
