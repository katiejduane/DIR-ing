# Import pygame
import pygame

# Import my own classes
# Import super class
from character import Character
# Import sub classes
from heroine import Heroine
from monster import Monster
from goblin import Goblin

# # Import Button
# from button import Start_Button

#Get group and groupcollide from the Sprite Module
from pygame.sprite import Group, groupcollide


#Keys
KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275



def main():
    width = 512
    height = 480
    blue_color = (97, 159, 182)

    #init pygame
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    # Load Images
    background_image = pygame.image.load('images/background.png').convert_alpha()
    heroine_fr = pygame.image.load('images/heroine_front.png').convert_alpha()
    heroine_bk = pygame.image.load('images/heroine_back.png').convert_alpha()
    heroine_r = pygame.image.load('images/heroine_right.png').convert_alpha()
    heroine_l = pygame.image.load('images/heroine_left.png').convert_alpha()
    monster_image = pygame.image.load('images/monster.png').convert_alpha()
    goblin_image = pygame.image.load('images/goblin.png').convert_alpha()

    # (self, fr_image, bk_image, r_image, l_image, x, y):
    la_heroina = Heroine(heroine_fr, heroine_fr, heroine_bk, heroine_r, heroine_l, 250, 250)
    monster = Monster(monster_image, 100, 100)
    goblin = Goblin(goblin_image, 400, 400)

    heroines = Group()
    heroines.add(la_heroina)
    enemies = Group()
    enemies.add(monster, goblin)

    # Game initialization
    stop_game = False
    while not stop_game:
        # Draw things!!!

        # background
        screen.blit(background_image, [0, 0])

        # heroine
        la_heroina.render(screen)
        la_heroina.draw(512, 480)

        # monster
        monster.render(screen)
        monster.update(width, height)

        # goblin
        goblin.render(screen)
        goblin.update(width, height)

        # kill
        kill = groupcollide(heroines, enemies, False, True)
        if kill:
            print("kill")

        for event in pygame.event.get():

            # Event handling
            if event.type == pygame.QUIT:
                stop_game = True

            # Game logic
            key = pygame.key.get_pressed()

            if event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == 275:  # right arrow key number
                    la_heroina.move("right")
                elif event.key == 276:
                    la_heroina.move("left")
                elif event.key == 273:
                    la_heroina.move("up")
                elif event.key == 274:
                    la_heroina.move("down")
            elif event.type == pygame.KEYUP:  # the user released a key
                if event.key == 275:
                    la_heroina.move("right", False)
                elif event.key == 276:
                    la_heroina.move("left", False)
                elif event.key == 273:
                    la_heroina.move("up", False)
                elif event.key == 274:
                    la_heroina.move("down", False)
                else:
                    print(event.key)


        # Game display
        pygame.display.update()

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
