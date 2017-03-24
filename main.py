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

# fsock = open('error.log', 'w')
# sys.stderr = fsock

speedFontSize = 120
circleValueSize = 40
circleTextSize = 13
circleRadius = 145
circleWidth = 40

# init devices
serial = CromeQD2()
mcp3208 = MCP3208()

controller = Controller()

# info
runTime = Text(100, 415, "Helvetica", 25, "bold italic", Global.OFFtextColor, "", "", "00:00:00")
controller.add_object(runTime)

controller.start()


