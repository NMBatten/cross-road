from pygame.locals import *
import pygame
from constants import Constants as con
from groups import Groups

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.surf = pygame.Surface((20, 20))
        self.surf.fill((200, 250, 250))
        self.rect = self.surf.get_rect()
        self.score = 0

        self.rect.center = ((con.SCREEN_WIDTH / 2, con.SCREEN_HEIGHT - 45))
        # self.jumping = False

    def jump(self, key):
        if key == pygame.K_UP:
            self.rect.centery -= 30
        elif key == pygame.K_DOWN:
            self.rect.centery += 30
        elif key == pygame.K_LEFT:
            self.rect.centerx -= 30
        elif key == pygame.K_RIGHT:
            self.rect.centerx += 30

    def update(self):
        # hits = pygame.sprite.spritecollide(self, Groups.obstacles,  False)
        # if hits:
        #     if hits[0]:
        #         return "playerkill"
        pass
