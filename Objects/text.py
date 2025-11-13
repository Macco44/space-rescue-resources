from GameFrame import TextObject, Globals

class text(TextObject): 
    def __init__(self, room, x, y, 
                 text='Thank you for playing Hook, Line & Stinker.\n I hope you enjoyed it, and have learnt about phishing emails.\n Here are some key notes:\n 1. Emails with .gov or.edu are always safe\n 2. Emails with spelling mistakes are often scams\n 3. Company emails that dont have correct \n spelling are often scams.', 
                 size=60,
                 font='Comic Sans MS', 
                 colour=(64, 224, 208), 
                 bold=False): 
        full_text = f"{text}\nYour Score: {Globals.fish} Fish on {Globals.LIVES} Lives  Press ESC for Credits"
        TextObject.__init__(self, room, x, y, full_text, size, font, colour, bold, reveal_rate=10)