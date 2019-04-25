from pygame.sprite import Sprite
import pygame
from character import Character
from pygame.locals import *


class Heroine(Character):
    def __init__(self, main_img, fr_image, bk_image, r_image, l_image, x, y):
        super().__init__(main_img, x, y, speed = 6)
        self.speed = 5
        self.main_img = fr_image
        self.fr_image = fr_image
        self.bk_image = bk_image
        self.r_image = r_image
        self.l_image = l_image

    def move(self, direction, start = True):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 512:
            self.rect.right = 512
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 480:
            self.rect.bottom = 480

    # def draw(self, w, h):
    #     if self.move_right:
    #         if self.x <= w - 64:
    #             self.x += self.speed
    #     elif self.move_left:
    #         if self.x >= 32:
    #             self.x -= self.speed
    #     if self.move_down:
    #         if self.y <= h - 64:
    #             self.y += self.speed
    #     elif self.move_up:
    #         if self.y >= 32:
    #             self.y -= self.speed

    # def collide_and_kill(self, width, enemy):
    #     if enemy.x + width < self.x:
    #         return False
    #     elif self.x + width < enemy.x:
    #         return False
    #     elif enemy.y + width < self.y:
    #         return False
    #     elif self.y + width < enemy.y:
    #         return False
    #     else:
    #         return True
