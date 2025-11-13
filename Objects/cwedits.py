from GameFrame import TextObject, Globals

class cwedits(TextObject): 
    def __init__(self, room, x, y, 
                 text='Credits:\nMusic:\nLimbus Company (Through Patches of Violet, Curiosity Compass)\n Code:\nMr Murtagh, Github, WindsurfAI',
                 size=40,
                 font='Comic Sans MS', 
                 colour=(255, 255, 255), 
                 bold=False): 
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold, reveal_rate=10)