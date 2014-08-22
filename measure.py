from bmp183 import bmp183

if __name__ == "__main__":
	bmp = bmp183()
	bmp.measure_pressure()
	print "Temperature: ", bmp.temperature, "deg C"
	print "Pressure: ", bmp.pressure/100.0, " hPa"
	quit()
