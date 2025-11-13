from GameFrame import RoomObject
import pygame


class Error(RoomObject):
       
    def __init__(self, room, x, y):

        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("fish.png")
        self.set_image(image,500,500)

        # record spawn time for auto-despawn
        self.spawn_time = pygame.time.get_ticks()

    def step(self):
        # auto-delete after 3 seconds
        if pygame.time.get_ticks() - self.spawn_time >= 3000:
            self.delete_object(self)
