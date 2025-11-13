from GameFrame import Level
from Objects.Email3F import Email3F
from Objects.Email3T import Email3T

class Email3(Level):
    """
    Email 2
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        self.set_background_image("safeemail.png")
        self.add_room_object(Email3T(self, 400, 400))
        self.add_room_object(Email3F(self, 900, 400))

