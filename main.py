# -*- coding: utf-8 -*-
from Tkinter import *
from gui.Gauge import *
from gui.Rpm import *
from gui.Text import *
from gui.Bar import *
from gui.Circle import *
from gui.Arrow import *
from gui.Gforce import *
from controller.Controller import *
from devices.CromeQD2 import *
from devices.MCP3208 import *
from devices.DigitalInput import *
from devices.ADXL345 import *
from devices.Odometer import *
from gui.Icon import *
import sys
from controller.Global import *

#fsock = open('error.log', 'w')
#sys.stderr = fsock

# ratio constants
root = Tk()
root.attributes('-fullscreen', True)
root.focus_set()


def close(self):
    root.destroy()


root.bind('<Escape>', close)
root.config(cursor='none')

winWidth = root.winfo_screenwidth()  # 1280
winHeight = root.winfo_screenheight()  # 800

speedFontSize = 120
circleValueSize = 40
circleTextSize = 13
circleRadius = 145
circleWidth = 40

# init devices
serial = CromeQD2()
mcp3208 = MCP3208()
controller = Controller()

# init canvas
canvas = Canvas(root, width=winWidth, height=winHeight, bg=Global.OFFBgColor)
canvas.pack()

# info
runTime = Text(canvas, 100, 415, "Helvetica", 25, "bold italic", Global.OFFtextColor, "", "", "00:00:00")

canvas.after(10, controller.new_update_all, canvas, runTime)

# main loop
root.mainloop()
