#!/usr/bin/env python

import sys
import time
import struct
#import numpy

import pigpio


if __name__ == "__main__":
  pi = pigpio.pi()

  if pi.connected:
   print("Connected to pigpio daemon.")
   hndl = pi.spi_open(0, 50000)
   (count, rx_data) = pi.spi_xfer(hndl, b'\\xD0')
   pi.spi_close(hndl)

   print count
   for i in rx_data:
     print rx_data[i]

  pi.stop()
