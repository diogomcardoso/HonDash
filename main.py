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

fsock = open('error.log', 'w')
sys.stderr = fsock

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


def adc2fuel(self, adc):
    volts = (adc / 4096.000) * 4.80
    return (int)(-7.348540077 * pow(10, -1) * pow(volts, 2) - 32.27276861 * volts + 109.170896)


# conversion for VDO 323-057 sensor powered by 4.8v and read with a 56ohms voltage divider
def adc2oiltemp(adc):
    volts = (adc / 4096.000) * 4.80
    return (int)(-9.805174198 * pow(10, -1) * pow(volts, 9) + 23.4368155 * pow(volts, 8) - 240.7430517 * pow(volts,
                                                                                                             7) + 1390.11628 * pow(
        volts, 6) - 4955.008229 * pow(volts, 5) + 11266.31187 * pow(volts, 4) - 16289.93484 * pow(volts,
                                                                                                  3) + 14423.41426 * pow(
        volts, 2) - 7152.975474 * volts + 1697.497838)


def adc2oilpress(adc):
    volts = (adc / 4096.000) * 4.80
    return round(7.671035919 * pow(10, -2) * pow(volts, 7) - 1.077184901 * pow(volts, 6) + 6.295494139 * pow(volts,
                                                                                                             5) - 19.62567902 * pow(
        volts, 4) + 35.08161116 * pow(volts, 3) - 35.51613665 * pow(volts, 2) + 19.52857924 * volts - 4.551671147, 1)


def oilTempSensor():
    return adc2oiltemp(mcp3208.get_adc(7))


def oilPressSensor():
    return adc2oilpress(mcp3208.get_adc(5))


def waterTempSensor():
    return int(serial.get_ect())


def batterySensor():
    return round(serial.get_battery(), 1)


def iatSensor():
    return int(serial.get_iat())


def injSensor():
    return serial.get_inj()


def ignSensor():
    return int(serial.get_ign())


def dutySensor():
    return serial.get_duty_cycle()


# init canvas
canvas = Canvas(root, width=winWidth, height=winHeight, bg=Global.OFFBgColor)
canvas.pack()

wallpaper = Icon(canvas, "/home/pi/Desktop/HonDash/images/camo4.jpg", 1280 / 2, 800 / 2, 1280, 800, False)

fuelIcon = Icon(canvas, "/home/pi/Desktop/HonDash/images/fuel.png", 352, 356, 45, 50, False)
highBeamIcon = Icon(canvas, "/home/pi/Desktop/HonDash/images/lights.png", 900, 380, 63, 31, False)
trunkIcon = Icon(canvas, "/home/pi/Desktop/HonDash/images/rear.png", 700, 380, 64, 38, False)
oilIcon = Icon(canvas, "/home/pi/Desktop/HonDash/images/oil.png", 800, 380, 89, 21, False)

# init graphics
rpm = Gauge(canvas, 640, 260, 250, 135, 210, 1, 6, 9, Global.OFFgauge, 40, "Helvetica", "bold italic", 14, 4,
            Global.OFFgauge, 30, 8, Global.OFFgauge, 5, 8, "red", "gray75", 50, Global.OFFneedleCoverColor)
speed = Text(canvas, 135, 250, "Helvetica", speedFontSize, "bold italic", Global.OFFtextColor, "", "", "139")
speedUnit = Text(canvas, 330, 290, "Helvetica", 30, "bold italic", Global.OFFtextColor, "", "", "km/h")
mileage = 1  # Text(canvas,winWidth/2,(winHeight/10)*3,"Helvetica",10,"bold ","white","","","162.372 KM")
fuel = Bar(canvas, 25, 380, 0, 280, 0, 50, 0, 100, Global.fuelColor, Global.OFFshadeColor)
fuelText = Text(canvas, 175, 356, "Helvetica", 30, "bold italic", Global.fuelTextColor, "", "%", "100")

# p=Text(canvas,640,50,"Helvetica",40,"bold italic","black","","7","")

# pedals
clutch = Bar(canvas, 1040, 798, 80, 80, 0, 380, 0, 200, Global.clutchColor, Global.OFFclutchBgColor)
brake = Bar(canvas, 1119, 798, 80, 80, 0, 380, 2100, 2400, Global.brakeColor, Global.OFFbrakeBgColor)
throttle = Bar(canvas, 1200, 798, 80, 80, 0, 380, 0, 100, Global.throttleColor, Global.OFFthrottleBgColor)

# circles
oilTemp = Circle(canvas, 150, 540, circleRadius, circleWidth, 240, 300, 0, 150, 80, 120, Global.circleMinColor,
                 Global.circleNormalColor, Global.circleMaxColor, circleValueSize, circleTextSize, Global.OFFtextColor,
                 "OIL T", Global.OFFshadeColor, oilTempSensor, None)

oilPressure = Circle(canvas, 150, 715, circleRadius, circleWidth, 240, 300, 0, 10, 3, 6, Global.circleMinColor,
                     Global.circleNormalColor, Global.circleNormalColor, circleValueSize, circleTextSize,
                     Global.OFFtextColor, "OIL P", Global.OFFshadeColor, oilPressSensor, None)

h2o = Circle(canvas, 400, 540, circleRadius, circleWidth, 240, 300, 0, 150, 80, 120, Global.circleMinColor,
             Global.circleNormalColor, Global.circleMaxColor, circleValueSize, circleTextSize, Global.OFFtextColor,
             "H2O T", Global.OFFshadeColor, waterTempSensor, None)

g = None  # Gforce(canvas,450,680,205,2,2,"gray",6,"red",Global.OFFtextColor)

battery = Circle(canvas, 650, 540, circleRadius, circleWidth, 240, 300, 0, 16, 11, 15, Global.circleMaxColor,
                 Global.circleNormalColor, Global.circleMaxColor, circleValueSize, circleTextSize, Global.OFFtextColor,
                 "BAT", Global.OFFshadeColor, batterySensor, None)

iat = Circle(canvas, 900, 540, circleRadius, circleWidth, 240, 300, 0, 50, 0, 40, Global.circleMinColor,
             Global.circleNormalColor, Global.circleMaxColor, circleValueSize, circleTextSize, Global.OFFtextColor,
             "IAT", Global.OFFshadeColor, iatSensor, None)

inj = Circle(canvas, 400, 715, circleRadius, circleWidth, 240, 300, 0, 20, 0, 20, Global.circleMinColor,
             Global.circleNormalColor, Global.circleMaxColor, circleValueSize, circleTextSize, Global.OFFtextColor,
             "INJ ms", Global.OFFshadeColor, injSensor, None)

ign = Circle(canvas, 900, 715, circleRadius, circleWidth, 240, 300, 0, 60, 0, 60, Global.circleMinColor,
             Global.circleNormalColor, Global.circleMaxColor, circleValueSize, circleTextSize, Global.OFFtextColor,
             "IGN", Global.OFFshadeColor, ignSensor, None)

duty = Circle(canvas, 650, 715, circleRadius, circleWidth, 240, 300, 0, 50, 0, 50, Global.circleMinColor,
              Global.circleNormalColor, Global.circleMaxColor, circleValueSize, circleTextSize, Global.OFFtextColor,
              "DTY %", Global.OFFshadeColor, dutySensor, None)

# turn lights
arrowLeft = Arrow(canvas, 100, 100, 0.35, Global.signalColor, "left", False)
arrowRight = Arrow(canvas, 300, 100, 0.35, Global.signalColor, "right", False)

# info
runTime = Text(canvas, 100, 415, "Helvetica", 25, "bold italic", Global.OFFtextColor, "", "", "00:00:00")
h2oEcu = None  # Text(canvas,910,324,"Helvetica",30,"bold italic",Global.OFFtextColor,"H2O: ","cº","44")
vtec = None  # Text(canvas,700,594,"Helvetica",30,"bold italic",Global.OFFtextColor,"VTC: ","","off")
mapp = None  # Text(canvas,702,738,"Helvetica",30,"bold italic",Global.OFFtextColor,"MAP: ","mBar","433")
gear = Text(canvas, 1100, 220, "Helvetica", 350, "bold", Global.OFFtextColor, "", "", "N")
gearUnit = None  # Text(canvas,745,385,"Helvetica",20,"bold italic",Global.OFFtextColor,"GEAR","","")

odometer = Odometer()
odometerText = Text(canvas, 300, 415, "Helvetica", 25, "bold italic", Global.OFFtextColor, "", " km", "")

# update graphics
canvas.after(10, controller.updateAll, canvas, mcp3208, serial, controller, rpm, speed, oilTemp, oilPressure, h2o,
             h2oEcu, battery, fuel, throttle, clutch, brake, runTime, inj, duty, vtec, iat, ign, mapp, arrowLeft,
             arrowRight, accelerometer, g, fuelText, gear)

# main loop
root.mainloop()
