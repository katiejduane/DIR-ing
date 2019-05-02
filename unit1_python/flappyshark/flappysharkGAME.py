import pygame
import time
from background import Background
from shark import Shark
from seaweed import SeaWeed
from seaweed import UpperSeaWeed
from pygame.sprite import Group, spritecollide, spritecollideany, groupcollide



def main():
    width = 1000
    height = 1000
    blue_color = (97, 159, 182)
    black_color = (0, 0, 0)

    # adding music
    pygame.mixer.init()
    # sound = pygame.mixer.Sound('music/baby_shark_soundtrack.wav')

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Flappy Baby Daddy Shark')
    clock = pygame.time.Clock()

    # Adding image files
    seaweed_image = pygame.image.load('images/seaweed.png').convert_alpha()
    upper_seaweed_image = pygame.image.load(
        'images/upper_seaweed.png').convert_alpha()
    sharky_image = pygame.image.load(
        'images/daddy_shark_110px.png').convert_alpha()


    # Adding flappybabyshark and seaweed characters:
    seaweed = SeaWeed(seaweed_image, 1000, 600, 1)
    upper_seaweed = UpperSeaWeed(upper_seaweed_image, 1000, -600, 1)
    shark = Shark(100, 500)
    #shark.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
    # shark.vx = 5
    # shark.vy = 5

    # shark_group = pygame.sprite.Group()
    # shark_group.add(shark)

    seaweed_group = Group()
    seaweed_group.add(seaweed, upper_seaweed)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(shark)

    # Game loop/Event handling
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # sound.play()
                stop_game = True

        # draw stuff
        BackGround = Background('images/bbsharktitle.jpg', [0, 0])
        screen.fill([255, 255, 255])
        screen.blit(BackGround.image, BackGround.rect)
        font = pygame.font.Font(None, 50)
        text = font.render('Click to play', True, black_color)
        screen.blit(text, (395, 750))

        pygame.display.update()
        clock.tick(60)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == 275:  # right arrow key number
                    shark.should_move("right")
                elif event.key == 276:
                    shark.should_move("left")
                elif event.key == 273:
                    shark.should_move("up")
                elif event.key == 274:
                    shark.should_move("down")
            elif event.type == pygame.KEYUP:  # the user released a key
                if event.key == 275:
                    shark.should_move("right", False)
                elif event.key == 276:
                    shark.should_move("left", False)
                elif event.key == 273:
                    shark.should_move("up", False)
                elif event.key == 274:
                    shark.should_move("down", False)
                else:
                    print(event.key)
     

    
        # Game logic

        # Draw background
        screen.fill(blue_color)

        seaweed.display(screen)
        upper_seaweed.display(screen)
        seaweed.update_position(width, height)
        upper_seaweed.update_position(width, height)

        #Shark 
        if pygame.sprite.spritecollideany(shark, seaweed_group):
            shark.kill()

        # shark.render(screen, sharky_image)
        for entity in all_sprites:
            screen.blit(entity.image, [entity.x, entity.y])

        shark.draw_me(width, height)
        shark.update_me(width, height)

        # print("shark", shark.x, shark.y)
        # print("seaweed", seaweed.x, seaweed.y)
        # print("upper seaweed", upper_seaweed.x, upper_seaweed.y)

        # collision
        if pygame.sprite.spritecollideany(shark, seaweed_group):
            shark.kill()
            print('DEAD')

        pygame.display.update()
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()
