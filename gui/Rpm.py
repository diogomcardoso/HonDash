class Rpm:
    def __init__(self, canvas, x, y, width, height, bar_width, color, back_color, offset_degrees, total_degrees, min_value,
                 max_value):
        self.canvas = canvas
        self.minValue = min_value
        self.maxValue = max_value
        self.totalDegrees = -total_degrees
        self.offsetDegrees = -180 - offset_degrees
        self.barWidth = bar_width
        self.canvas.create_arc(x - (width / 2), y - (height / 2), x + (width / 2), y + (height / 2), style="arc",
                               outline=back_color, fill="", extent=self.totalDegrees, start=self.offsetDegrees,
                               width=self.barWidth)
        self.idRpm = self.canvas.create_arc(x - (width / 2), y - (height / 2), x + (width / 2), y + (height / 2),
                                            style="arc", outline=color, fill="", extent=0, start=self.offsetDegrees,
                                            width=self.barWidth)

    def set_rpm(self, value_fill):
        if value_fill > self.maxValue:
            value_fill = self.maxValue
        elif value_fill < self.minValue:
            value_fill = self.minValue

        degrees = (((value_fill - self.minValue) * (self.totalDegrees - 0)) / (self.maxValue - self.minValue)) + 0
        self.canvas.itemconfig(self.idRpm, extent=degrees)
