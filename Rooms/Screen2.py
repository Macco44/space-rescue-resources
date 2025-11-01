from GameFrame import Level
from Objects.Player2 import Player2

class Screen2(Level):
    """
    Intial screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
    
        # set background image
        self.set_background_image("Background.png")
        self.add_room_object(Player2(self, 25, 50))