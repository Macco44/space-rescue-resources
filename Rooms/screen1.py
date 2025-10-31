from GameFrame import Level
class screen1(Level):
    """
    Intial screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
    
        # set background image
        self.set_background_image("Background.png")

        self.add_room_object(Start(self, 750, 400))