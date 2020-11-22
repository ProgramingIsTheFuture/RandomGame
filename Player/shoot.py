import pygame


class Fire(object):
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.shoot_speed = 8
        self.bullet_sender = []
        self.shoot_limit = 2
        self.w_max, self.h_max = pygame.display.get_surface().get_size()
        self.height = 5
        self.width = 5

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def on_shot(self, last_direction):
        if self.bullet_sender.__len__() < self.shoot_limit:
            self.bullet_sender.append([last_direction, self.x, self.y])

    def draw_shot(self):
        for index, shoot in enumerate(self.bullet_sender):
            if 0 > shoot[1] or shoot[1] > self.w_max:
                self.bullet_sender.pop(index)

            elif 0 > shoot[2] or shoot[2] > self.h_max:
                self.bullet_sender.pop(index)

            if shoot[0] == 0:
                shoot[2] -= self.shoot_speed
                self.draw_individual_shot(shoot[1], shoot[2])

            if shoot[0] == 1:
                shoot[2] += self.shoot_speed
                self.draw_individual_shot(shoot[1], shoot[2])

            if shoot[0] == 2:
                shoot[1] -= self.shoot_speed
                self.draw_individual_shot(shoot[1], shoot[2])

            if shoot[0] == 3:
                shoot[1] += self.shoot_speed
                self.draw_individual_shot(shoot[1], shoot[2])

    def draw_individual_shot(self, shoot_1, shoot_2):
        pygame.draw.rect(self.screen, (0, 255, 0), (shoot_1, shoot_2, self.height, self.width))
