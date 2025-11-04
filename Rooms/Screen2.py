from GameFrame import Level
from Objects.Player2 import Player2
from GameFrame.Globals import Globals
import pygame
class Screen2(Level):


    """
    Intial screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
    
        # set background image
        self.set_background_image("screen1.png")
        self.add_room_object(Player2(self, 25, 50))
        self.music()
    def music(self):
        if Globals.sound:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("Sounds/boss_music.mp3")
            pygame.mixer.music.play(-1)
