#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SPEED: Module 04: Saturation Vapor Pressure calculations from temperature

GitHub repository: https://github.com/maplion/SPEED
@author: Ryan Dammrose aka MapLion
"""

import matplotlib.pyplot as plt
import speedcalc

__author__ = "Ryan Dammrose"
__copyright__ = "Copyright 2015"
__license__ = "MIT"

sc_Pressure = speedcalc.Pressure(number_of_decimals=3)

vaporPressureList = []
temperatureList = []
temperature = -15.0
while temperature < 35.01:
    vaporPressure = sc_Pressure.vapor_pressure_from_temperature(temperature)
    vaporPressure = sc_Pressure.pascals_to_kilopascals(vaporPressure)
    print("T = {0} deg. C, esat = {1} kPa".format(temperature, vaporPressure))
    vaporPressureList.append(vaporPressure)
    temperatureList.append(temperature)
    temperature = round(temperature + 0.01, 2)
plt.plot(temperatureList, vaporPressureList)
plt.xlabel("Temperature [Celsius Degrees]")
plt.ylabel("Saturation vapor pressure (e*) [kPa]")
plt.show()
