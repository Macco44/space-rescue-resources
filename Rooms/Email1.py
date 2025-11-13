from GameFrame import Level
from Objects.Email1F import Email1F
from Objects.Email1T import Email1T

class Email1(Level):
    """
    Email 1
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        self.set_background_image("safeemail.png")
        self.add_room_object(Email1F(self, 400, 400))
        self.add_room_object(Email1T(self, 900, 400))

