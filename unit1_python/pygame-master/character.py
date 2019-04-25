from pygame.sprite import Sprite
import pygame


class Character(Sprite):
    def __init__(self, main_img, x, y, speed):
        super(Character, self).__init__()
        self.main_img = main_img
        self.x = x
        self.y = y
        self.speed = speed
        self.rect = pygame.Rect(0, 0, 64, 64)
        self.rect.centerx = self.x
        self.rect.top = self.y

    def render(self, screen):
        screen.blit(self.main_img, (self.x, self.y))

