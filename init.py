#!/usr/bin/python
import os, random, time

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
	mypath = "/home/AutoPlayUSB/mount/"
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	print(onlyfiles)

	#REMOVE FILE IF PRESENT
	os.system("rm /home/AutoPlayUSB/mount/playlist.txt")
	#MAKE NEW FILE
	file = open('/home/AutoPlayUSB/mount/playlist.txt', 'w')
	file.writelines(["%s\n" % item  for item in onlyfiles])
	file.close()
	
	time.sleep(2)

	os.system("cd /home/AutoPlayUSB/mount && mplayer -ao alsa:device=hw=1.0 -playlist playlist.txt -loop 0")



while True:
	try:
		pass
	except KeyboardInterrupt as e:
		continue
	pass