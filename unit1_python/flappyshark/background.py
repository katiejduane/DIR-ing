import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/bbsharktitle.jpg')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


# def main():
#     width = 1000
#     height = 1000
#     black_color = (0, 0, 0)
#     pygame.mixer.init()
#     sound = pygame.mixer.Sound('music/baby_shark_soundtrack.wav')
#     pygame.init()
#     screen = pygame.display.set_mode((width, height))
#     pygame.display.set_caption('Flappy Baby Daddy Shark')
#     clock = pygame.time.Clock()
#     stop_game = False
#     while not stop_game:
#         for event in pygame.event.get():
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 sound.play()
#             if event.type == pygame.QUIT:
#                 stop_game = True
#         BackGround = Background('images/bbsharktitle.jpg', [0, 0])
#         screen.fill([255, 255, 255])
#         screen.blit(BackGround.image, BackGround.rect)
#         font = pygame.font.Font(None, 50)
#         text = font.render('Click to play', True, black_color)
#         screen.blit(text, (395, 750))

#         pygame.display.update()
#         clock.tick(60)
#     pygame.quit()


# if __name__ == '__main__':
#     main()


# class Background(pygame.sprite.Sprite):
#     def __init__(self, image_file, location):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load('images/bbsharktitle.jpg')
#         self.rect = self.image.get_rect()
#         self.rect.left, self.rect.top = location


# class Scene(object):
#     def __init__(self):
#         pass

#     def render(self, screen):
#         raise NotImplementedError

#     def update(self):
#         raise NotImplementedError

#     def handle_events(self, events):
#         raise NotImplementedError


# class Title(Scene):
#     def __init__(self):
#         super(title_scene, self).__init__()
#         width = 1000
#         height = 1000
#         black_color = (0, 0, 0)
#         pygame.mixer.init()
#         sound = pygame.mixer.Sound('music/baby_shark_soundtrack.wav')
#         pygame.init()
#         screen = pygame.display.set_mode((width, height))
#         pygame.display.set_caption('Flappy Baby Daddy Shark')
#         clock = pygame.time.Clock()
#         stop_game = False
#         while not stop_game:
#             for event in pygame.event.get():
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     sound.play()
#                 if event.type == pygame.QUIT:
#                     stop_game = True
#             BackGround = Background('images/bbsharktitle.jpg', [0, 0])
#             screen.fill([255, 255, 255])
#             screen.blit(BackGround.image, BackGround.rect)
#             font = pygame.font.Font(None, 50)
#             text = font.render('Click to play', True, black_color)
#             screen.blit(text, (395, 750))

#             pygame.display.update()
#             clock.tick(60)
#         pygame.quit()
# # if __name__ == '__main__':
# #     main()
