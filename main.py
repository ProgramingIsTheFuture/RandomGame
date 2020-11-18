import pygame
import sys


class Fire(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def on_shot(self, last_direction):
        pass

    def draw_shot(self):
        pass


class Player(object):
    def __init__(self, x, y, height, width, screen):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.speed = 0.5
        self.screen = screen
        self.last_direction = 0 # 0 -> up, 1 -> down, 2 -> Left, 3 -> Right
        self.shoot_time = 0
        self.Fire = Fire(self.x, self.y)

    def draw(self):
        rect = pygame.draw.rect(self.screen, (255, 255, 255), (self.x, self.y, self.width, self.height))

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        w, h = pygame.display.get_surface().get_size()
        print(w, h)
        if self.y > 0:
            if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
                self.y -= self.speed
                self.last_direction = 0
                self.Fire.set_y(self.y)

        if self.y < h:
            if pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
                self.y += self.speed
                self.last_direction = 1
                self.Fire.set_y(self.y)

        if self.x > 0:
            if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
                self.x -= self.speed
                self.last_direction = 2
                self.Fire.set_x(self.x)

        if self.x < w:
            if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
                self.x += self.speed
                self.last_direction = 3
                self.Fire.set_x(self.x)

        if pressed_keys[pygame.K_SPACE]:
            self.Fire.on_shot(self.last_direction)

    def fire(self):
        if self.last_direction == 0:
            pass
        if self.last_direction == 1:
            pass
        if self.last_direction == 2:
            pass
        if self.last_direction == 3:
            pass

    def colision(self):
        pass


class App(object):

    def __init__(self):
        pygame.init()

        pygame.time.Clock().tick(120)

        self.screen = pygame.display.set_mode((800, 800))
        self.running = True

        w, h = pygame.display.get_surface().get_size()
        self.Player = Player(w//2, h//2, 30, 30, self.screen)

    def run(self):
        while self.running:

            self.screen.fill((100, 100, 100))

            self.Player.draw()
            self.Player.move()
            self.Player.fire()

            for event in pygame.event.get():
                self.quit(event)

            pygame.display.update()

    def quit(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            sys.exit()


if __name__ == '__main__':
    App().run()
