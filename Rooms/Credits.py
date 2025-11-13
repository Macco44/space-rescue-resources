from Objects.cwedits import cwedits
from GameFrame import Level


class Credits(Level):
    """
    Intial screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        self.add_room_object(cwedits(self, 25, 50))
    def music(self):
        if Globals.sound:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("Sounds/boss_music.mp3")
            pygame.mixer.music.play(-1)
