import pygame
from pygame.locals import *
from pygame.sprite import Sprite, Group, groupcollide
import random
from random import randint

class Character(Sprite):
    def __init__(self):
        super(Character, self).__init__()
        # self.rect = pygame.Rect(0,0,32,32)
        self.speed_x = 0
        self.speed_y = 0

class Hero(Character):
    def __init__(self, x, y):
        super() .__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load('images/hero.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.top = self.y 
        self.speed = 4
        self.should_move_down = False
        self.should_move_up = False
        self.should_move_left = False
        self.should_move_right = False

    def should_move(self, direction, start = True):
        if direction == "right":
            self.should_move_right = start
        if direction == "left":
            self.should_move_left = start
        if direction == "up":
            self.should_move_up = start
        if direction == "down":
            self.should_move_down = start     

    def draw_me(self,w,h):
        if(self.should_move_right):
            if(self.x <= w - 64):
                self.x += self.speed
        elif(self.should_move_left):
            if(self.x >= 32):
                self.x -= self.speed
        elif(self.should_move_down):
            if(self.y <= h - 64):
                self.y += self.speed
        elif self.should_move_up:
            if(self.y >= 32):
                self.y -= self.speed  
        self.rect.x = self.x 
        self.rect.y = self.y
    
    def catch_monster(self, enemy):
        if self.x == enemy.x and self.y == enemy.y:
            print("collision detected")
            enemy.kill()

class Monster(Character):
    def __init__(self, x, y):
        super() .__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load('images/monster.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.top = self.y 
        self.speed = 8
    
    def random_move(self,w,h):
        movements = ["right", "up right", "down right", "left", "up left", "down left", "up", "down"]
        random.shuffle(movements)
        i = movements[0]
        if i == "right":
            if self.x < w:
                self.x += self.speed
            else:
                self.x = 0
                self.x += self.speed
        elif i == "up right":
            if self.x < w and self.y > 0:
                self.x += self.speed  
                self.y -= self.speed
            else:
                self.x = 0
                self.x += self.speed  
                self.y = h
                self.y -= self.speed
        elif i == "down right":
            if self.x < w and self.y < h:
                self.x += self.speed
                self.y += self.speed
            else: 
                self.x = 0
                self.x += self.speed 
                self.y = 0
                self.y += self.speed
        elif i == "left":
            if self.x > 0:
                self.x -= self.speed
            else: 
                self.x = w
                self.x -= self.speed 
        elif i == "up left":
            if self.x > 0 and self.y > 0:
                self.x -= self.speed
                self.y -= self.speed 
            else: 
                self.x = w
                self.x -= self.speed 
                self.y = h
                self.y -= self.speed 
        elif i == "down left":
            if self.x > 0 and self.y < h:
                self.x -= self.speed
                self.y += self.speed
            else: 
                self.x = w
                self.x -= self.speed 
                self.y = 0
                self.y += self.speed
        elif i == "down":
            if self.y <= h:
                self.y += self.speed
            else:
                self.y = 0
                self.y += self.speed
        elif i == "up":
            if self.y >= 0:
                self.y -= self.speed 
            else:
                self.y = h
                self.y -= self.speed 
        self.rect.x = self.x 
        self.rect.y = self.y
        pygame.time.delay(50)
    
    def kill(self):
        pygame.sprite.Sprite.kill(self)

# instantiate Hero object & create sprite group
the_hero = Hero(100, 100)
heroes = pygame.sprite.Group()
heroes.add(the_hero)

# instantiate Monster object & create sprite group
the_monster = Monster(250, 250)
monsters = pygame.sprite.Group()
monsters.add(the_monster)

def main():
    width = 512
    height = 480

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Monster Chase')

    background_image = pygame.image.load('images/background.png')

    # Game initialization
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True

            # event listener for keydown
            elif event.type == pygame.KEYDOWN:
                if event.key == 275:
                    the_hero.should_move("right")
                elif event.key == 276: 
                    the_hero.should_move("left")
                elif event.key == 273: 
                    the_hero.should_move("up")
                elif event.key == 274: 
                    the_hero.should_move("down")

            elif event.type == pygame.KEYUP:
                if event.key == 275: 
                    the_hero.should_move("right", False)
                elif event.key == 276: #left arrow
                    the_hero.should_move("left", False)
                if event.key == 273: #up arrow
                    the_hero.should_move("up", False)
                elif event.key == 274: #down arrow
                    the_hero.should_move("down", False) 

        # Draw game
        if stop_game == False:
            screen.blit(background_image, [0,0])

            for the_monster in monsters:
                screen.blit(the_monster.image, [the_monster.x, the_monster.y])
                the_monster.random_move(512, 480)

            for the_hero in heroes: 
                the_hero.draw_me(512,480) 
                the_hero.catch_monster(the_monster)
                screen.blit(the_hero.image, [the_hero.x, the_hero.y])

        # Game display
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
