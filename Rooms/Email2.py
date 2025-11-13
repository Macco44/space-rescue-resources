from GameFrame import Level
from Objects.Email2F import Email2F
from Objects.Email2T import Email2T

class Email2(Level):
    """
    Email 2
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        self.set_background_image("safeemail.png")
        self.add_room_object(Email2F(self, 400, 400))
        self.add_room_object(Email2T(self, 900, 400))

