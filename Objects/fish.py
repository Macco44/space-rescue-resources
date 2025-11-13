from GameFrame import TextObject, Globals

class fish(TextObject): 
    def __init__(self, room, x, y, 
                 text='Fish:', 
                 size=40,
                 font='Comic Sans MS', 
                 colour=(255,255,255), 
                 bold=False): 
        full_text = f"{text}{Globals.fish}"
        TextObject.__init__(self, room, x, y, full_text, size, font, colour, bold)