import pygame


class Shark(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            'images/daddy_shark_110px.png').convert_alpha()
        self.x = x
        self.y = y
        self.rect = pygame.Rect(0,0,110, 50)
        self.rect.centerx = self.x
        self.rect.top = self.y
        self.speed = 5
        self.should_move_down = False
        self.should_move_up = False
        self.should_move_left = False
        self.should_move_right = False

    def should_move(self, direction, start=True):
        if direction == "right":
            self.should_move_right = start
        if direction == "left":
            self.should_move_left = start
        if direction == "down":
            self.should_move_down = start
        if direction == "up":
            self.should_move_up = start

    # def render(self, screen, image):
    #     screen.blit(image, [self.x, self.y])

    def draw_me(self, w, h):
        if self.should_move_right:
            if self.x <= w - 110:
                self.x += self.speed
        elif self.should_move_left:
            if self.x >= 50:
                self.x -= self.speed
        if self.should_move_down:
            if self.y <= h - 110:
                self.y += self.speed
        elif self.should_move_up:
            if self.y >= 50:
                self.y -= self.speed

    def update_me(self, width, height):
        # self.x -= self.speed
        self.rect.x = self.x
        self.rect.y = self.y




    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self, pressed_keys):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
