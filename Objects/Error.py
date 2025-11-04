from GameFrame import RoomObject

class Error(RoomObject):
       
    def __init__(self, room, x, y):

        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("error.png")
        self.set_image(image,100,100)

        
