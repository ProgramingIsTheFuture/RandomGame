import pygame
import sys
import time
from Player.player import Player
from Enemy.enemy import Enemy


class App(object):
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Random Game LOL!")
        self.running = True

        w, h = pygame.display.get_surface().get_size()

        self.Player = Player(w//2, h//2, 30, 30, self.screen)
        self.Fire = self.Player.Fire
        self.Enemy = []
        for i in range(5):
            self.Enemy.append(Enemy(30, 30, self.screen))
        self.player_dead = False
        self.enemy_dead = False

    def run(self):
        while self.running:
            self.clock.tick(120)

            self.screen.fill((100, 100, 100))

            for index, i in enumerate(self.Enemy):
                i.draw()
                i.move_enemy()
                self.player_dead = self.Player.collision(i.x, i.y, i.width, i.height)
                if self.player_dead:
                    self.running = False

                self.enemy_dead = i.collision_bullet(self.Fire.get_x(), self.Fire.get_y(), self.Fire.get_width(), self.Fire.get_height())
                if self.enemy_dead:
                    self.Enemy.pop(index)
                    self.enemy_dead = False

            self.Player.draw()
            self.Player.move()

            for event in pygame.event.get():
                self.quit(event)

            pygame.display.update()

        pygame.quit()

    def quit(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            sys.exit()


if __name__ == '__main__':
    App().run()
