import pygame


class SeaWeed(pygame.sprite.Sprite):
    def __init__(self, image, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.x = x
        self.y = y
        self.rect = pygame.Rect(0,0, 180, 960)
        self.rect.centerx = self.x
        self.rect.top = self.y
        self.speed = speed

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update_position(self, width, height):
        self.x -= self.speed
        self.rect.x = self.x
        self.rect.y = self.y
        # if self.x > width:
        #     self.x = 0


class UpperSeaWeed(pygame.sprite.Sprite):
    def __init__(self, image, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = pygame.Rect(0,0, 180, 960)
        self.x = x
        self.y = y
        self.rect.centerx = self.x
        self.rect.top = self.y
        self.speed = speed

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update_position(self, width, height):
        self.x -= self.speed
        self.rect.x = self.x
        self.rect.y = self.y
        # if self.x > width:
        #     self.x = 0
