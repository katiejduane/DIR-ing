import pygame

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

class Character(pygame.sprite.Sprite):
    def __init__(self, image, pos, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed_x = 0
        self.speed_y = 0


# [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
class Hero(Character):
    def __init__(self, image, pos, x, y):
        super() .__init__(image, pos, x, y)
        self.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
        self.x = x
        self.y = y
        self.vx = 5
        self.vy = 5


class Monster(Character):
    pass


def main():
    width = 512
    height = 480
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    # Load Images
    background_image = pygame.image.load('images/background.png').convert_alpha()
    hero_image = pygame.image.load('images/hero.png').convert_alpha()
    monster_image = pygame.image.load('images/monster.png').convert_alpha()

    player = Hero(hero_image, [250, 250], 250, 250)
    monster = Monster(monster_image, [100, 100], 100, 100)

    player_group = pygame.sprite.Group()
    player_group.add(player)

    monster_group = pygame.sprite.Group()
    monster_group.add(monster)

    # Game initialization
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling
            if event.type == pygame.QUIT:
                stop_game = True

        # Game logic
        key = pygame.key.get_pressed()

        # for i in range(2):
            # if key[player.move[i]]:
            #     player.rect.x += player.vx * [-1, 1][i]
            #     print(player.rect.x, (player.vx * [-1, 1][i]))
        if key[pygame.K_LEFT]:
            player.rect.x += player.vx * -1
            print(player.rect.x, (player.vx * -1))
        if key[pygame.K_RIGHT]:
            player.rect.x += player.vx * 1
            print(player.rect.x, (player.vx * 1))
        # for i in range(2):
        #     if key[player.move[2:4][i]]:
        #         player.rect.y += player.vy * [-1, 1][i]
        #         print(player.rect.y, (player.vy * [-1, 1][i]))
        if key[pygame.K_UP]:
            player.rect.y += player.vy * -1
            print(player.rect.y, (player.vy * -1))
        if key[pygame.K_DOWN]:
            player.rect.y += player.vy * 1
            print(player.rect.y, (player.vy * 1))
        

        # Draw background
        # screen.fill(blue_color)
        screen.blit(background_image, [0, 0])

        player_group.draw(screen)
        monster_group.draw(screen)


        # Game display
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
