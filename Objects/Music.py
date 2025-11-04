from GameFrame import RoomObject
import pygame
from GameFrame.Globals import Globals

class Music(RoomObject):
       
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.handle_mouse_events = True
        self._last_sound_state = None  # Track last state
        self.update_image()  # Initial image setup
    
    def update_image(self):
        if Globals.sound:
            image = self.load_image("unmute.png")
        else:
            image = self.load_image("mute.png")
        self.set_image(image, 200, 200)
        self._last_sound_state = Globals.sound

    def step(self):
        # Check if sound state changed
        if self._last_sound_state != Globals.sound:
            self.update_image()
    
    def clicked(self, button_number): 
        if button_number == 1:
            Globals.sound = not Globals.sound  # Toggle sound
            if Globals.sound:
                pygame.mixer.music.load("Sounds/background_music.mp3")
                pygame.mixer.music.play(-1)
            else:
                pygame.mixer.music.stop()