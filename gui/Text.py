class Text:
    def __init__(self, x, y, font, size, weight, color, prefix, suffix, text):
        self.x = x
        self.y = y
        self.font = font
        self.size = size
        self.weight = weight
        self.color = color
        self.prefix = str(prefix)
        self.suffix = str(suffix)
        self.text = text
        self.id = None
        self.canvas = None

    def add_to_canvas(self, canvas):
        self.canvas = canvas
        self.id = self.canvas.create_text(self.x, self.y, text=self.prefix + self.text + self.suffix,
                                     font=self.font + " " + str(self.size) + " " + self.weight, fill=self.color)

    def set_text(self, text):
        self.canvas.itemconfig(self.id, text=self.prefix + str(text) + self.suffix)

    def set_color(self, color):
        self.canvas.itemconfig(self.id, fill=color)
