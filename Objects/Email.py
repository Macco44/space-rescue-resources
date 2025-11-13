from GameFrame import TextObject, Globals, RoomObject

class Email(RoomObject):
    """
    A class for the email object
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image("Email.png")
        self.set_image(image,250,250)
        self.handle_mouse_events = True
    def clicked(self, button_number):
        if button_number == 1 and Globals.email == 0:
            Globals.next_level = Globals.levels.index("Email1")
            self.room.running = False
        elif button_number == 1 and Globals.email == 1:
            Globals.next_level = Globals.levels.index("Email2")  
            self.room.running = False
        elif button_number == 1 and Globals.email == 2:
            Globals.next_level = Globals.levels.index("Email3")
            self.room.running = False
