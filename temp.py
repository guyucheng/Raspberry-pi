#!/usr/bin/env python
tmpFile = open( '/sys/class/thermal/thermal_zone0/temp' )
cpu_temp_raw = tmpFile.read()
tmpFile.close()
cpu_temp = round(float(cpu_temp_raw)/1000, 1)
print (cpu_temp)



