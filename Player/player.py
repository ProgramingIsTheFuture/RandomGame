import pygame
from .shoot import Fire


class Player(object):
    def __init__(self, x, y, height, width, screen):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.screen = screen
        self.speed = 2.5
        self.last_direction = 0 # 0 -> up, 1 -> down, 2 -> Left, 3 -> Right
        self.shoot_time = 0
        self.Fire = Fire(self.x, self.y, self.screen)

    def draw(self):
        self.draw_player()
        self.Fire.draw_shot()

    def draw_player(self):
        pygame.draw.rect(self.screen, (0, 0, 255), (self.x, self.y, self.width, self.height))

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        w, h = pygame.display.get_surface().get_size()

        if self.y > 0:
            if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
                self.y -= self.speed
                self.last_direction = 0

        if self.y + self.height < h:
            if pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
                self.y += self.speed
                self.last_direction = 1

        if self.x > 0:
            if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
                self.x -= self.speed
                self.last_direction = 2

        if self.x + self.width < w:
            if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
                self.x += self.speed
                self.last_direction = 3

        if pressed_keys[pygame.K_SPACE]:
            self.Fire.set_y(self.y)
            self.Fire.set_x(self.x)
            self.Fire.on_shot(self.last_direction)

    def collision(self, x, y, width, height):
        if (x <= self.x <= x + width or x <= self.x + self.width <= x + width) and (y <= self.y <= y + height or y <= self.y + self.height <= y + height):
            return True
        return False
