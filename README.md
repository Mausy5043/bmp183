Running:

`sudo python measure.py`

For continuous measurement run:

`watch -n 1 sudo python measure.py`

Expected result looks similar to this:
```
Temperature:  18.9 deg C
Pressure:  1013.39  hPa
```

Connecting:
```
BMP pin : RPi pin
========:===============
VIN     : 17  (3v3)
3vo     : N/C
GND     : 25  (GND)
SCLK    : 23  (GPIO11)
SDO     : 21  (GPIO09; MISO)
SDI     : 19  (GPIO10; MOSI)
CS      : 24  (GPIO08; CE0)
```
