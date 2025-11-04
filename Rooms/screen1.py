from GameFrame import Level
from Objects.Player import Player


class Screen1(Level):
    """
    Intial screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
    
    
        self.set_background_image("screen1.png")
        self.add_room_object(Player(self, 25, 50))