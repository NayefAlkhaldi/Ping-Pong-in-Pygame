import pygame
from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self, screen, position):
        super().__init__()
        self.game_screen = screen
        self.screen_width = self.game_screen.get_rect().width
        self.screen_height = self.game_screen.get_rect().height
        self.color = 'white'
        self.speed = 10
        self.moving_up = False
        self.moving_down = False
        self.points = 0
        self.font = pygame.font.SysFont('freesanbold.ttf', 50)
        self.score_counter = self.font.render(str(self.points), True, 'white')
        if position == 'left':
            self.x = 10
        elif position == 'right':
            self.x = self.screen_width - 10
        self.y = (self.screen_height / 2)
        self.shape = pygame.Rect(self.x, self.y, 3, 50)

    def update(self):
        self.score_counter = self.font.render(str(self.points), True, 'white')
        if self.moving_up and self.shape.y > 0:
            self.shape.move_ip(0, -self.speed)
        elif self.moving_down and self.shape.y < self.screen_height - 55:
            self.shape.move_ip(0, self.speed)

    def draw(self):
        pygame.draw.rect(self.game_screen, self.color, self.shape)