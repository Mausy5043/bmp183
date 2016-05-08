#!/usr/bin/env python
from pigbmp183 import bmp183

bmp = bmp183()
bmp.measure_pressure()
print ("Temperature: {0} degC".format(bmp.temperature))
print ("Pressure:    {0} hPa ".format(bmp.pressure / 100.0))
quit()
