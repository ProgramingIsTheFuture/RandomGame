import pygame
import random


class Enemy(object):
    def __init__(self, width, height, screen):
        self.width = width
        self.speed = 1
        self.height = height
        self.spawn_position = random.randint(0, 3)
        self.screen = screen
        self.y = 0
        self.x = 0
        self.health = 100
        self.time = 0
        self.w, self.h = pygame.display.get_surface().get_size()

        self.create_enemy()

    def create_enemy(self):
        self.time = pygame.time.get_ticks()
        if self.spawn_position == 0:
            self.x = random.randint(0, self.w)
            if self.x >= self.w - self.width:
                self.x = self.w - self.width
            self.y = 0

        if self.spawn_position == 1:
            self.x = random.randint(0, self.w)
            if self.x >= self.w - self.width:
                self.x = self.w - self.width
            self.y = self.h - self.height

        if self.spawn_position == 2:
            self.x = 0
            self.y = random.randint(0, self.h)
            if self.y >= self.h - self.height:
                self.y = self.h - self.height

        if self.spawn_position == 3:
            self.x = self.w - self.width
            self.y = random.randint(0, self.h)
            if self.y >= self.h - self.height:
                self.y = self.h - self.height

    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def move_enemy(self):
        if self.spawn_position == 0:
            self.y += self.speed
            if self.y >= self.h - self.height:
                self.spawn_position = 1
        if self.spawn_position == 1:
            self.y -= self.speed
            if self.y <= 0:
                self.spawn_position = 0
        if self.spawn_position == 2:
            self.x += self.speed
            if self.x >= self.w - self.width:
                self.spawn_position = 3
        if self.spawn_position == 3:
            self.x -= self.speed
            if self.x <= 0:
                self.spawn_position = 2

    def collision_bullet(self, bullet_x, bullet_y, bullet_width, bullet_height):
        if (self.x >= bullet_x >= self.x + self.width or self.x >= bullet_x + bullet_width >= self.x + self.width) and (self.y >= bullet_y >= self.y + self.height or self.y >= bullet_y + bullet_height >= self.y + self.height):
            return True
        return False

    def shoot(self):
        pass
