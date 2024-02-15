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
            if not self.rect.centery + 30 > con.SCREEN_HEIGHT:
                self.rect.centery += 30
        elif key == pygame.K_LEFT:
            if not self.rect.centerx - 30 < 0:
                self.rect.centerx -= 20
        elif key == pygame.K_RIGHT:
            if not self.rect.centerx + 30 > con.SCREEN_WIDTH:
                self.rect.centerx += 20


    def update(self):
        log = pygame.sprite.spritecollide(self, Groups.logs, False)
        if log:
            self.rect.centerx += log[0].slot.object_speed

        if self.rect.right > con.SCREEN_WIDTH:
            pass
