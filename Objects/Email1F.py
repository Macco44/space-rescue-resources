from GameFrame import RoomObject
from GameFrame.Globals import Globals

class Email1F(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image("Email1F.png"), 250, 250)
        self.handle_mouse_events = True

    def clicked(self, button_number):
        if button_number == 1:
            Globals.LIVES -=1
            Globals.next_level = Globals.levels.index("Screen1")
            self.room.running = False
