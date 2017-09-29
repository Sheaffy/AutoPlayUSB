# AutoPlayUSB

This is a python script that will automaticly mount any usb drives, find all mp3's on that drive and play them all on on a playlist that repeats.
## Dependancys
install Mplayer
```
sudo apt-get mplayer
```

## Installation
ALWAYS install in /home this is currently hardcoded
```
sudo git clone https://github.com/Sheaffy/AutoPlayUSB.git
```

### Automatic Startup
```
sudo nano /etc/rc.local
```
Put in rc.local
```
python /home/pi/Boat/init.py &
exit 0
```
