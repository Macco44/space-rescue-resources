import pygame
from GameFrame import RoomObject, Level


class TextObject(RoomObject):
    def __init__(self, room: Level, x: int, y: int, text='Not Set', size=60,
                 font='Comic Sans MS', colour=(0, 0, 0), bold=False, reveal_rate: float = 0):
        RoomObject.__init__(self, room, x, y)

        self.rendered_text = 0
        self.rect = 0
        self.built_font = 0
        self.text = text
        self.size = size
        self.font = font
        self.colour = colour
        self.bold = bold
        self.reveal_rate = reveal_rate
        self.revealed_chars = 0 if reveal_rate and reveal_rate > 0 else len(str(text))
        self._accum_ms = 0.0
        self._last_tick = pygame.time.get_ticks()
        self.update_text()

    def update_text(self):
        self.built_font = pygame.font.SysFont(self.font, self.size, self.bold)
        src_text = str(self.text)
        if self.revealed_chars < len(src_text):
            src_text = src_text[:self.revealed_chars]
        lines = src_text.split('\n')
        if len(lines) == 1:
            self.rendered_text = self.built_font.render(src_text, False, self.colour)
            self.image = self.rendered_text
            self.width, self.height = self.built_font.size(src_text)
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
            return

        rendered_lines = [self.built_font.render(line, False, self.colour) for line in lines]
        max_width = 0
        total_height = 0
        line_heights = []
        for surf in rendered_lines:
            w, h = surf.get_size()
            max_width = max(max_width, w)
            total_height += h
            line_heights.append(h)

        composed = pygame.Surface((max_width, total_height), pygame.SRCALPHA)
        y_offset = 0
        for surf, h in zip(rendered_lines, line_heights):
            composed.blit(surf, (0, y_offset))
            y_offset += h

        self.image = composed
        self.width, self.height = composed.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def step(self):
        if not self.reveal_rate or self.reveal_rate <= 0:
            return
        now = pygame.time.get_ticks()
        elapsed = now - self._last_tick
        self._last_tick = now
        self._accum_ms += elapsed
        if self.revealed_chars >= len(str(self.text)):
            return
        ms_per_char = 1000.0 / float(self.reveal_rate)
        add = int(self._accum_ms / ms_per_char)
        if add <= 0:
            return
        self._accum_ms -= add * ms_per_char
        self.revealed_chars = min(len(str(self.text)), self.revealed_chars + add)
        self.update_text()
