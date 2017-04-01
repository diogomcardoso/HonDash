# -*- coding: utf-8 -*-
import gui.Circle
from controller.Controller import *
from controller.Global import *
from devices.Formula import Formula
from devices.DigitalInput import DigitalInput
from devices.Kpro import Kpro
from devices.MCP3208 import MCP3208
from gui.Arrow import Arrow

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
formula = Formula()


runTime = gui.Text.Text(canvas, 100, 415, "Helvetica", 25, "bold italic", Global.OFFtextColor, "", "", "00:00:00",
                        timer, 'get_time')
battery = gui.Circle.Circle(canvas, 650, 540, circleRadius, circleWidth, 240, 300, 0, 16, 11, 15, Global.circleMaxColor,
                            Global.circleNormalColor, Global.circleMaxColor, circleValueSize, circleTextSize,
                            Global.OFFtextColor, "BAT", Global.OFFshadeColor, kpro, 'bat', None)

arrowLeft = Arrow(canvas, 100, 100, 0.35, Global.signalColor, "left", False, DigitalInput(12, None), 'value', None)

oilTemp = gui.Circle.Circle(canvas, 150, 540, circleRadius, circleWidth, 240, 300, 0, 150, 80, 120,
                            Global.circleMinColor, Global.circleNormalColor, Global.circleMaxColor, circleValueSize,
                            circleTextSize, Global.OFFtextColor, "OIL T", Global.OFFshadeColor, analog, 'adc_with_formula', [0, formula.vdo_323_057])

controller.add_object(runTime)
controller.add_object(battery)
controller.add_object(kpro)
controller.add_object(arrowLeft)
controller.add_object(oilTemp)

controller.start()
# main loop
root.mainloop()
