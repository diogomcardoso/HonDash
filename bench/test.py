#sudo python bench/test.py
from __future__ import print_function
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from devices.kpro import Kpro
from reprint import output


kpro = Kpro()
with output(output_type="dict", initial_len=1, interval=0) as output_list:
    while True:
        output_list['BAT'] = str(kpro.bat())
        output_list['CAM'] = str(kpro.cam())
        output_list['AFR'] = str(kpro.afr())
        output_list['IAT'] = str(kpro.iat())
        output_list['RPM'] = str(kpro.rpm())
        output_list['TPS'] = str(kpro.tps())
        output_list['VSS'] = str(kpro.vss())
        output_list['ECT'] = str(kpro.ect())
        output_list['GEAR'] = str(kpro.gear())
        output_list['EPS'] = str(kpro.eps())
        output_list['SCS'] = str(kpro.scs())
        output_list['RVSLCK'] = str(kpro.rvslck())
        output_list['BKSW'] = str(kpro.bksw())
        output_list['ACSW'] = str(kpro.acsw())
        output_list['ACCL'] = str(kpro.accl())
        output_list['FLR'] = str(kpro.flr())
        output_list['MAP'] = str(kpro.map())
        output_list['INFO'] = str(kpro.info)