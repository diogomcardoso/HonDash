# -*- coding: utf-8 -*-
import gui.Circle
from controller.Controller import *
from controller.Global import *
from devices.Kpro import Kpro
from devices.MCP3208 import MCP3208

circleValueSize = 40
circleTextSize = 13
circleRadius = 145
circleWidth = 40

# ratio constants
root = Tk()
root.attributes('-fullscreen', True)
root.focus_set()


def close(event):
    root.destroy()


root.bind('<Escape>', close)
root.config(cursor='none')

win_width = root.winfo_screenwidth()  # 1280
win_height = root.winfo_screenheight()  # 800

canvas = Canvas(root, width=win_width, height=win_height, bg=Global.OFFBgColor)
canvas.pack()

controller = Controller(canvas)

analog = MCP3208()
timer = devices.Time.Time()
kpro = Kpro()

runTime = gui.Text.Text(canvas, 100, 415, "Helvetica", 25, "bold italic", Global.OFFtextColor, "", "", "00:00:00",
                        timer, 'get_time')
battery = gui.Circle.Circle(canvas, 650, 540, circleRadius, circleWidth, 240, 300, 0, 16, 11, 15, Global.circleMaxColor,
                            Global.circleNormalColor, Global.circleMaxColor, circleValueSize, circleTextSize,
                            Global.OFFtextColor, "BAT", Global.OFFshadeColor, kpro, 'rpm', None)

controller.add_object(runTime)
controller.add_object(battery)
controller.add_object(kpro)

controller.start()
# main loop
root.mainloop()
