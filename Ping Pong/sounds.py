import pygame.mixer as mixer
import os

mixer.init()


class Sound(object):
    def __init__(self, name):
        self.name = name
        self.sound = mixer.Sound(os.path.join(r"assests\sounds", name + ".mp3"))

    def play(self):
        mixer.Sound.play(self.sound)