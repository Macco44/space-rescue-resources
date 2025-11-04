from GameFrame import Level
from Objects.Start import Start
from Objects.Music import Music

class WelcomeScreen(Level):
    """
    Intial screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
    
        # set background image
        self.set_background_image("welcomescreen.png")

        self.add_room_object(Start(self, 680, 280))
        
        self.add_room_object(Music(self, 0,-30))