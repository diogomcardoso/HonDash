# -*- coding: utf-8 -*-
from controller.Controller import *
from controller.Global import *
from devices.CromeQD2 import *
from devices.MCP3208 import *
import gui.Text

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


runTime = gui.Text.Text(100, 415, "Helvetica", 25, "bold italic", Global.OFFtextColor, "", "", "00:00:00")
controller.add_object(runTime)

controller.start()


