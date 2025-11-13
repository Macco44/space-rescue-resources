from GameFrame import TextObject, Globals, RoomObject



class Lives(RoomObject):
    """
    A class for displaying the number of lives remaining
    """
    def __init__(self, room, x: int, y: int):
        """
        Intialises the lives object
        """   
        RoomObject.__init__(self, room, x, y)
        
        # set image
        self.lives_icon = []
        # load the various lives images into a live list
        for index in range(6):
            self.lives_icon.append(self.load_image(f"Lives_frames/Lives_{index}.png"))
        self.update_image()
        
        
    def update_image(self):
        """
        Updates the number of lives on the UI
        """
        self.set_image(self.lives_icon[Globals.LIVES], 125, 23)