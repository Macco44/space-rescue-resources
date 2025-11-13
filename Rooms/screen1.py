from GameFrame import Level
from Objects.Player import Player
from Objects.Lives import Lives
from Objects.Email import Email
import pygame
from GameFrame import Globals
from Objects.fish import fish

class Screen1(Level):
    """
    Intial screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)    
        self.set_background_image("screen1.png")
        self.add_room_object(Player(self, 25, 50))
        self.add_room_object(Lives(self, 1400, 10))
        self.add_room_object(fish(self, 1400, 700))
        self.add_room_object(Email(self, 650, 100))
