import pygame
import random
from random import randint
from pygame.sprite import Sprite, Group, groupcollide

class Character(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(0,0,32,32)
        self.speed_x = 0
        self.speed_y = 0

class Hero(Character):
    def __init__(self, x, y):
        super() .__init__()
        self.x = x
        self.y = y
        self.rect.centerx = self.x
        self.rect.top = self.y 
        self.speed = 8
        self.should_move_down = False
        self.should_move_up = False
        self.should_move_left = False
        self.should_move_right = False

    def shouldMove(self, direction, start = True):
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

class Monster(Character):
    def __init__(self, x, y):
        super() .__init__()
        self.x = x
        self.y = y
        self.speed = 10
        self.should_move_right = False
        self.should_move_left = False
        self.should_move_up = False
        self.should_move_down = False
    
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
        pygame.time.delay(50)

# instantiate Hero object & create sprite group
the_hero = Hero(100, 100)
heroes = Group()
heroes.add(the_hero)

# instantiate Monster object & create sprite group
the_monster = Monster(250, 250)
monsters = Group()
monsters.add(the_monster)

def main():
    width = 512
    height = 480

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Monster Chase')

    background_image = pygame.image.load('images/background.png').convert_alpha()
    hero_image = pygame.image.load('images/hero.png').convert_alpha()
    monster_image = pygame.image.load('images/monster.png').convert_alpha()
    

    # Game initialization
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True

            elif event.type == pygame.KEYDOWN:
                if event.key == 275:
                    the_hero.shouldMove("right")
                elif event.key == 276: 
                    the_hero.shouldMove("left")
                elif event.key == 273: #up arrow
                    the_hero.shouldMove("up")
                elif event.key == 274: #down arrow
                    the_hero.shouldMove("down")
            elif event.type == pygame.KEYUP:
                if event.key == 275: 
                    the_hero.shouldMove("right", False)
                elif event.key == 276: #left arrow
                    the_hero.shouldMove("left", False)
                if event.key == 273: #up arrow
                    the_hero.shouldMove("up", False)
                elif event.key == 274: #down arrow
                    the_hero.shouldMove("down", False) 

        # Game logic

        the_monster.random_move(512, 480)
        the_hero.draw_me(512,480) 

        # Draw background
        # screen.fill(blue_color)
        screen.blit(background_image, [0,0])
        screen.blit(hero_image, [the_hero.x, the_hero.y])
        screen.blit(monster_image, [the_monster.x, the_monster.y])

        # Game display
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
