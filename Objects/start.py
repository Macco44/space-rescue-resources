from GameFrame import RoomObject

class Start(RoomObject):
       
    def __init__(self, room, x, y):

        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("start.png")
        self.set_image(image,100,100)

        self.handle_mouse_events = True
    
    def clicked(self, button_number): 
    # - Check for a left mouse button click - # 
        if button_number == 1: 
            print("this took too long")