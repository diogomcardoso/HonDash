from devices.Time import *
import numpy
from controller.Global import *
import locale


class Controller:
    def __init__(self):
        self.startRecord = -1
        self.endRecord = -1
        self.timer = Time()
        self.fuelCounter = 0

    locale.setlocale(locale.LC_ALL, 'en_GB.utf8')


def adc2fuel(adc):
    volts = (adc / 4096.000) * 4.80
    return int(-7.348540077 * pow(10, -1) * pow(volts, 2) - 32.27276861 * volts + 109.170896)


def updateAll(self, canvas, mcp3208, serial, controller, rpm, speed, oilTemp, oilPressure, h2o, h2oEcu, battery, fuel,
              throttle, clutch, brake, runTime, inj, duty, vtec, iat, ign, mapp, arrowLeft, arrowRight, accelerometer,
              g, fuelText, gear):
    rawSpeed = serial.get_vss()
    speed.set_text(rawSpeed)
    if (rawSpeed <= 0):
        gear.set_text("N")
    else:
        gear.set_text(serial.get_gear())
    rpm.set_value(serial.get_rpm() / 1000.0)
    # mapp.setText(serial.getMap())
    ign.update_value()
    iat.update_value()
    inj.update_value()
    duty.update_value()
    oilTemp.update_value()
    oilPressure.update_value()
    if self.fuelCounter < self.fuelCounterMax:
        self.fuelAverage.append(self.adc2fuel(mcp3208.get_adc(3)))
        self.fuelCounter = self.fuelCounter + 1
    else:
        self.fuelAverage = numpy.median(self.fuelAverage)
        fuel.set_width(int(self.fuelAverage))
        fuelText.set_text(int(self.fuelAverage))
        self.fuelAverage = []
        self.fuelCounter = 0
    h2o.update_value()
    # h2oEcu.setText(int(serial.getEct()))
    battery.update_value()
    throttle.set_height(serial.get_tps())
    clutch.set_height(0)  # mcp3208.getADC(1))
    # if(serial.getVtec()): vtec.setText("on")
    # else: vtec.setText("off")
    brake.set_height(0)  # mcp3208.getADC(7))'''
    time = self.timer.get_time()
    runTime.set_text(self.timer.getTimeString())
    self.odometerText.set_text(locale.format("%d", self.odometer.getValue(serial.get_vss()), grouping=True))

    '''axes = accelerometer.getAxes(True)
	g.setGforce(axes['y'],axes['z'])
	print axes['x'],axes['y'],axes['z']'''
    canvas.after(10, controller.updateAll, canvas, mcp3208, serial, controller, rpm, speed, oilTemp, oilPressure, h2o,
                 h2oEcu, battery, fuel, throttle, clutch, brake, runTime, inj, duty, vtec, iat, ign, mapp, arrowLeft,
                 arrowRight, accelerometer, g, fuelText, gear)
