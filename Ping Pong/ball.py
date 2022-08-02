from pygame.sprite import Sprite
import random
import pygame
from sounds import Sound
import ball_physics


class Ball(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.game_screen = screen
        self.screen_width = self.game_screen.get_rect().width
        self.screen_height = self.game_screen.get_rect().height
        self.x = self.screen_width / 2
        self.y = self.screen_height / 2
        self.color = 'red'
        self.radius = 5
        self.direction = random.choice((1, -1)), random.choice((1, -1))
        self.speed = 5
        self.wait_frames = 0
        # Sounds
        self.hit_sound = Sound("hit")
        self.out_sound = Sound("out")

    def reset(self):
        self.x = self.screen_width / 2
        self.y = self.screen_height / 2
        self.direction = random.choice((1, -1)), random.choice((1, -1))

    def update(self, players):
        if self.wait_frames < 45:
            self.wait_frames += 1
        else:
            dx, dy = self.direction
            self.x, self.y = ball_physics.move_ball(self.x, self.y, dx, dy, self.speed)
            if ball_physics.hit_screen_height(self.screen_height, self.y):
                self.direction = ball_physics.ball_hit(dx, dy, 'height')
                self.hit_sound.play()
            if (ball_physics.shapes_collision(self.x, self.y, players[0].shape.x, players[0].shape.y) or
                    (ball_physics.shapes_collision(self.x, self.y, players[1].shape.x, players[1].shape.y))):
                self.direction = ball_physics.ball_hit(dx, dy, 'width')
                self.hit_sound.play()

            if ball_physics.hit_screen_width(self.screen_width, self.x) == 1:
                self.out_sound.play()
                players[0].points += 1
                pygame.time.wait(500)
                self.reset()

            elif ball_physics.hit_screen_width(self.screen_width, self.x) == -1:
                self.out_sound.play()
                players[1].points += 1
                pygame.time.wait(500)
                self.reset()

    def draw(self):
        pygame.draw.circle(self.game_screen, self.color, (self.x, self.y), self.radius)