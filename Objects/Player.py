from GameFrame import RoomObject, Globals
import pygame

class Player(RoomObject):
    """
    A class for the player's avatar
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        # preload animation frames
        self._images = {
            'player': self.load_image("Player.png"),
            'up1': self.load_image("Up1.png"),
            'up2': self.load_image("Up2.png"),
            'up_stand': self.load_image("Up_stand.png"),
            'down1': self.load_image("Player1.png"),
            'down2': self.load_image("Player2.png"),
            'left1': self.load_image("Left1.png"),
            'left2': self.load_image("Left2.png"),
            'left_stand': self.load_image("Left_stand.png"),
            'right1': self.load_image("Right1.png"),
            'right2': self.load_image("Right2.png"),
            'right_stand': self.load_image("Right_stand.png"),
        }

        # initial sprite
        self.set_image(self._images['player'], 100, 100)
        self.handle_key_events = True

        # animation state
        self.anim = {
            'up': {'frames': ['up1', 'up2'], 'idx': 0, 'timer': 0},
            'down': {'frames': ['down1', 'down2'], 'idx': 0, 'timer': 0},
            'left': {'frames': ['left1', 'left2'], 'idx': 0, 'timer': 0},
            'right': {'frames': ['right1', 'right2'], 'idx': 0, 'timer': 0},
        }
        self.anim_delay = 6  # frames between toggles
        self.was = {'up': False, 'down': False, 'left': False, 'right': False}

    def key_pressed(self, key):
        """
        Respond to keypresses and handle per-direction animations.
        `key` is expected to be the sequence returned by pygame.key.get_pressed()
        """
        # Movement + animation (priority: W, S, A, D)
        if key[pygame.K_w]:
            self.y -= 10
            st = self.anim['up']
            st['timer'] += 1
            if st['timer'] >= self.anim_delay:
                st['timer'] = 0
                st['idx'] = (st['idx'] + 1) % len(st['frames'])
            frame_key = st['frames'][st['idx']]
            self.set_image(self._images[frame_key], 100, 100)
            self.was['up'] = True

        elif key[pygame.K_s]:
            self.y += 10
            st = self.anim['down']
            st['timer'] += 1
            if st['timer'] >= self.anim_delay:
                st['timer'] = 0
                st['idx'] = (st['idx'] + 1) % len(st['frames'])
            frame_key = st['frames'][st['idx']]
            self.set_image(self._images[frame_key], 100, 100)
            self.was['down'] = True

        elif key[pygame.K_a]:
            self.x -= 20
            st = self.anim['left']
            st['timer'] += 1
            if st['timer'] >= self.anim_delay:
                st['timer'] = 0
                st['idx'] = (st['idx'] + 1) % len(st['frames'])
            frame_key = st['frames'][st['idx']]
            self.set_image(self._images[frame_key], 100, 100)
            self.was['left'] = True

        elif key[pygame.K_d]:
            self.x += 20
            st = self.anim['right']
            st['timer'] += 1
            if st['timer'] >= self.anim_delay:
                st['timer'] = 0
                st['idx'] = (st['idx'] + 1) % len(st['frames'])
            frame_key = st['frames'][st['idx']]
            self.set_image(self._images[frame_key], 100, 100)
            self.was['right'] = True

        else:
            # handle releases: set final standing frames and reset anim state
            if self.was['up'] and not key[pygame.K_w]:
                self.set_image(self._images['up_stand'], 100, 100)
                self._reset_anim('up')
            if self.was['down'] and not key[pygame.K_s]:
                self.set_image(self._images['player'], 100, 100)
                self._reset_anim('down')
            if self.was['left'] and not key[pygame.K_a]:
                self.set_image(self._images['left_stand'], 100, 100)
                self._reset_anim('left')
            if self.was['right'] and not key[pygame.K_d]:
                self.set_image(self._images['right_stand'], 100, 100)
                self._reset_anim('right')

        # ensure player remains inside room after movement
        self.keep_in_room()

    def step(self):

        self.keep_in_room()

        # detect reaching the far right edge
        right_edge = self.x + getattr(self, 'width', 0)
        if right_edge >= Globals.SCREEN_WIDTH and Globals.fish >=4: 
            self.room.running = False
        elif right_edge >= Globals.SCREEN_WIDTH and Globals.fish <4:
            print("You need to collect at least 4 fish to proceed!")

    # helper to reset animation state
    def _reset_anim(self, name):
        st = self.anim.get(name)
        if st:
            st['idx'] = 0
            st['timer'] = 0
        self.was[name] = False

    def keep_in_room(self):
        # clamp X axis
        if self.x < 0:
            self.x = 0
        elif self.x + getattr(self, 'width', 0) > Globals.SCREEN_WIDTH:
            self.x = Globals.SCREEN_WIDTH - getattr(self, 'width', 0)

        # clamp Y axis
        if self.y < 0:
            self.y = 0
        elif self.y + getattr(self, 'height', 0) > Globals.SCREEN_HEIGHT:
            self.y = Globals.SCREEN_HEIGHT - getattr(self, 'height', 0)