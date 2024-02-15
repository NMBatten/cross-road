from pygame.locals import *
import pygame
from constants import Constants as con
from main import Groups

class Player(pygame.sprite.Sprite):
    def __init__(self, vec):
        super().__init__()

        self.surf = pygame.Surface((20, 20))
        self.surf.fill((200, 150, 0))
        self.rect = self.surf.get_rect()

        self.pos = vec((con.SCREEN_WIDTH / 2, con.SCREEN_HEIGHT - 10))
        self.jumping = False

    def jump(self, key):
        if key == pygame.K_UP:
            self.pos.x += 30
        elif key == pygame.K_DOWN:
            self.pos.x -= 30
        elif key == pygame.K_LEFT:
            self.pos.y += 30
        elif key == pygame.K_RIGHT:
            self.pos.y -= 30

    def update(self):
        hits = pygame.sprite.spritecollide(self, Groups.obstacles,  False)
        if hits:
            if hits[0]:
                return "playerkill"
