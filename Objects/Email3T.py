from GameFrame import RoomObject
from GameFrame.Globals import Globals

class Email3T(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image("Email3T.png"), 350, 250)
        self.handle_mouse_events = True

    def clicked(self, button_number):
        if button_number == 1:
            Globals.next_level = Globals.levels.index("Screen1")
            Globals.fish += 2
            self.room.running = False
