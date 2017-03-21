class Bar:
    def __init__(self, canvas, x, y, min_width, max_width, min_height, max_height, min_value, max_value, color,
                 background_color):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.minWidth = min_width
        self.maxWidth = max_width
        self.minHeight = min_height
        self.maxHeight = -max_height
        self.minValue = min_value
        self.maxValue = max_value
        self.idBackgroundBar = self.canvas.create_rectangle(x, y, x + self.maxWidth, y + self.maxHeight,
                                                            fill=background_color, outline=background_color)
        self.idBar = self.canvas.create_rectangle(x, y, x + self.maxWidth, y + self.maxHeight, fill=color,
                                                  outline=color)

    def set_height(self, value):
        if value > self.maxValue:
            value = self.maxValue
        elif value < self.minValue:
            value = self.minValue

        new_height = (((value - self.minValue) * (self.maxHeight - self.minHeight)) / (
            self.maxValue - self.minValue)) + self.minHeight
        new_height += self.y
        actual_dimension = self.canvas.coords(self.idBar)
        self.canvas.coords(self.idBar, actual_dimension[0], new_height, actual_dimension[2], actual_dimension[3])

    def set_width(self, value):
        if value > self.maxValue:
            value = self.maxValue
        elif value < self.minValue:
            value = self.minValue

        new_width = (((value - self.minValue) * (self.maxWidth - self.minWidth)) / (
            self.maxValue - self.minValue)) + self.minWidth
        new_width += self.x
        actual_dimension = self.canvas.coords(self.idBar)
        self.canvas.coords(self.idBar, actual_dimension[0], actual_dimension[1], new_width, actual_dimension[3])

    def set_background_color(self, color):
        self.canvas.itemconfig(self.idBackgroundBar, fill=color)
        self.canvas.itemconfig(self.idBackgroundBar, outline=color)
