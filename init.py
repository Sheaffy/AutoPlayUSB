#!/usr/bin/python
import os, random

partitionsFile = open("/proc/partitions")
lines = partitionsFile.readlines()[2:]#Skips the header lines

LOCATION = ""

for line in lines:
    words = [x.strip() for x in line.split()]
    minorNumber = int(words[1])
    deviceName = words[3]
    if minorNumber % 16 == 0:
        path = "/sys/class/block/" + deviceName
        if os.path.islink(path):
            if os.path.realpath(path).find("/usb") > 0:
            	LOCATION = "/dev/"+deviceName+"1"
                print("/dev/" + deviceName)
                

if LOCATION != "":
	os.system("sudo umount "+LOCATION)
	print("Unmounted")
	os.system("sudo mount "+LOCATION+" /home/AutoPlayUSB/mount") 
	print("Mounted")

	#GET MP3 FILE
	from os import listdir
	from os.path import isfile, join
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	print(onlyfiles)





while True:
	try:
		pass
	except KeyboardInterrupt as e:
		continue
	pass