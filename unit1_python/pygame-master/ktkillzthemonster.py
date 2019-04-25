# Import pygame
import pygame

# Import super class
from character import Character

# Import sub classes
from heroine import Heroine
from monster import Monster
from goblin import Goblin

#Get group and groupcollide from the Sprite Module
from pygame.sprite import Group, spritecollide, spritecollideany


#Keys
K_UP = 273
K_DOWN = 274
K_LEFT = 276
K_RIGHT = 275

heroine_alive = True


def main():
    #init pygame
    pygame.init()

    # screen and size
    width = 512
    height = 480
    screen = pygame.display.set_mode((width, height))

    # Load Images
    background_image = pygame.image.load('images/background.png').convert_alpha()
    heroine_fr = pygame.image.load('images/heroine_front.png').convert_alpha()
    heroine_bk = pygame.image.load('images/heroine_back.png').convert_alpha()
    heroine_r = pygame.image.load('images/heroine_right.png').convert_alpha()
    heroine_l = pygame.image.load('images/heroine_left.png').convert_alpha()
    monster_image = pygame.image.load('images/monster.png').convert_alpha()
    goblin_image = pygame.image.load('images/goblin.png').convert_alpha()

    # Create characters
    la_heroina = Heroine(heroine_fr, heroine_fr, heroine_bk, heroine_r, heroine_l, 250, 250)
    monster = Monster(monster_image, 100, 100)
    goblin = Goblin(goblin_image, 400, 400)

   # Make groups
    enemies = pygame.sprite.Group()
    enemies.add(monster, goblin)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(la_heroina)

    # Game initialization
    game_on = True
    while game_on:
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.QUIT:
                game_on = False


        # Game logic

        # Draw stuff
        screen.blit(background_image, [0, 0])

        # la_heroina.render(screen)
        # la_heroina.draw(512, 480)
        pressed_keys = pygame.key.get_pressed()
        la_heroina.move(pressed_keys)

        monster.render(screen)
        monster.update(width, height)

        goblin.render(screen)
        goblin.update(width, height)

        enemies.update(width, height)

        for entity in all_sprites:
            screen.blit(entity.main_img, entity.rect)

        # let the chase begin (monster chase the heroine, sorry, heroine)
        if pygame.sprite.spritecollideany(la_heroina, enemies):
            la_heroina.kill()
            print("heroine: ", la_heroina.rect)
            print("monster: ", monster.rect)
            print("goblin: ", goblin.rect)
            pygame.quit()

        # killz = pygame.sprite.spritecollide(la_heroina, enemies, True)
        # if killz:
        #     print('true')

        # Game display
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()


 
