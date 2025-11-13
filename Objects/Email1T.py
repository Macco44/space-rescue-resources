from GameFrame import RoomObject
from GameFrame.Globals import Globals

class Email1T(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.set_image(self.load_image("Email1T.png"), 350, 250)
        self.handle_mouse_events = True

    def clicked(self, button_number):
        if button_number == 1:
            Globals.next_level = Globals.levels.index("Screen1")
            Globals.email += 1
            Globals.fish +=1
            self.room.running = False
