import pygame
import sys
from pygame.locals import *
from player import Player
from ball import Ball
from sounds import Sound


class Game(object):
    def __init__(self):
        # Screen Setup
        self.screen_width = 700
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.pingpong_icon = pygame.image.load("assests/images/pingpong.png")
        self.font = pygame.font.SysFont('freesanbold.ttf', 50)

        # Check if game is active
        self.game_over = False

        # Clock
        self.clock = pygame.time.Clock()
        self.FPS = 60

        # Sounds
        self.game_over_sound = Sound("GameOver")

        # Players
        self.player1 = Player(self.screen, 'left')
        self.player2 = Player(self.screen, 'right')
        self.players = [self.player1, self.player2]
        self.winner = None
        self.score_limit = 5
        self.game_over_sound_play = True

        # Ball
        self.ball = Ball(self.screen)

    def run(self):
        # Set caption and logo
        pygame.display.set_caption("Ping Pong")
        pygame.display.set_icon(self.pingpong_icon)
        pygame.mouse.set_visible(False)
        while True:
            # Update the screen and check events
            self.update()
            self.check_events()
            self.check_game_over()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.player1.moving_up = True
                if event.key == pygame.K_s:
                    self.player1.moving_down = True

                if event.key == pygame.K_UP:
                    self.player2.moving_up = True
                if event.key == pygame.K_DOWN:
                    self.player2.moving_down = True

                if event.key == pygame.K_p and self.game_over:
                    self.players[0].x = 10
                    self.players[1].x = self.screen_width - 10
                    for player in self.players:
                        player.shape.y = (self.screen_height / 2)
                        player.points = 0
                    self.ball.x = self.screen_width / 2
                    self.ball.y = self.screen_height / 2
                    self.game_over = False
                    self.ball.wait_frames = 0
                    self.game_over_sound_play = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.player1.moving_up = False
                if event.key == pygame.K_s:
                    self.player1.moving_down = False

                if event.key == pygame.K_UP:
                    self.player2.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.player2.moving_down = False

    def check_game_over(self):
        if (self.players[0].points >= self.score_limit) or (self.players[1].points >= self.score_limit):
            self.game_over = True
            if self.players[0].points > self.players[1].points:
                self.winner = 'player 1'
            elif self.players[0].points < self.players[1].points:
                self.winner = 'player 2'

    def update(self):
        self.screen.fill('black')
        if not self.game_over:
            pygame.draw.line(self.screen, 'grey', (self.screen_width / 2, 0),
                             (self.screen_width / 2, self.screen_height))
            self.screen.blit(self.player1.score_counter, (self.screen_width / 2 - 50, 0))
            self.screen.blit(self.player2.score_counter, (self.screen_width / 2 + 30, 0))

            for player in self.players:
                player.update()
                player.draw()

            self.ball.update(self.players)
            self.ball.draw()

        else:
            if self.game_over_sound_play:
                self.game_over_sound.play()
                self.game_over_sound_play = False

            if self.winner:
                winner = self.font.render(self.winner + ' won!', True, 'white')
            else:
                winner = self.font.render('Draw!', True, 'white')
            replay_text = self.font.render('Press p to replay', True, 'white')
            self.screen.blit(winner, (250, 250))
            self.screen.blit(replay_text, (230, 340))
        pygame.display.flip()
        self.clock.tick(self.FPS)