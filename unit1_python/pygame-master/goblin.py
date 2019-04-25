from pygame.sprite import Sprite
import pygame
from character import Character


class Goblin(Character):
    def __init__(self, main_img, x, y):
        super().__init__(main_img, x, y, speed=2)
        self.alive = True
        self.x_dir = -2
        self.y_dir = -2
    
    def update(self, width, height):
        self.x += self.x_dir
        self.y += self.y_dir
        if self.x + 64 > width:
            self.x_dir = -2
        if self.y + 64 > height:
            self.y_dir = -2
        if self.x - 64 < 0:
            self.x_dir = 2
        if self.y - 64 < 0:
            self.y_dir = 2
