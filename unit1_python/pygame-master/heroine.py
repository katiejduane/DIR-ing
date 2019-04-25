from pygame.sprite import Sprite
import pygame
from character import Character


class Heroine(Character):
    def __init__(self, main_img, fr_image, bk_image, r_image, l_image, x, y):
        super().__init__(main_img, x, y, speed = 6)
        self.speed = 5
        self.main_img = fr_image
        self.fr_image = fr_image
        self.bk_image = bk_image
        self.r_image = r_image
        self.l_image = l_image
        self.move_down = False
        self.move_up = False
        self.move_left = False
        self.move_right = False

    def move(self, direction, start = True):
        if direction == "right":
            self.move_right = start
        if direction == "left":
            self.move_left = start
        if direction == "down":
            self.move_down = start
        if direction == "up":
            self.move_up = start

    def draw(self, w, h):
        if self.move_right:
            if self.x <= w - 64:
                self.x += self.speed
        elif self.move_left:
            if self.x >= 32:
                self.x -= self.speed
        if self.move_down:
            if self.y <= h - 64:
                self.y += self.speed
        elif self.move_up:
            if self.y >= 32:
                self.y -= self.speed

    def collide_and_kill(self, width, enemy):
        if enemy.x + width < self.x:
            return False
        elif self.x + width < enemy.x:
            return False
        elif enemy.y + width < self.y:
            return False
        elif self.y + width < enemy.y:
            return False
        else:
            return True






# class Hero(Character):
#     def __init__(self, image, pos, x, y):
#         super() .__init__(image, pos, x, y)
#         self.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
#         self.x = x
#         self.y = y
#         self.vx = 5
#         self.vy = 5
