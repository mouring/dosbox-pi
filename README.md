The follow are a collection of notes from a side project to replace a bunch of aging 486 machines with Raspberry Pi 4Bs so that can be either attached to the back of the LCDs or the Use of the Pi 400 to replace the keyboard.

Future:
* Need way to set the macadr= unique per machine on boot
* Figure out the display setup
* Tuning for speed

Building DOSBox-X for /opt/dosbox-x/:
* apt update
* apt install -y libtool autogen autoconf automake libncurses-dev gcc g++ make  libncurses-dev nasm libsdl-net1.2-dev  libsdl2-net-dev libpcap-dev libslirp-dev  fluidsynth libfluidsynth-dev libavformat-dev  libavcodec-dev libavcodec-extra libswscale-dev  libfreetype-dev libxkbfile-dev libxrandr-dev git  ffmpeg  libcap2-bin vim
* git clone https://github.com/joncampbell123/dosbox-x.git
* cd dosbox-x
* sed -i 's,prefix=/usr,prefix=/opt/dosbox-x,’ build
* ./build 
* make install
* tar -cvzf dosbox-x.tgz /opt/dosbox-x

Using the DOSBox-X tarfile generated above:
* apt update
* apt install -y ffmpeg  libcap2-bin vim libncurses6 fluidsynth libsdl2-net-2.0-0 libpcap0.8 libslirp0 libxkbfile1
* cd /opt
* tar -xvzf ~/dosbox-x.tgz

Building Menu setup:
* apt update
* apt install -y python3-pip python3 python3-venv vim
* python3 -m venv menu
* ./menu/bin/pip3 install curses-menu

Cloning cards via Mac:
* diskutil list
* sudo dd if=/dev/rdiskX of=GamePi.img bs=1m
* diskutil umount /dev/diskXs1
* sudo dd io=/dev/rdisk4 if=GamePi.img bs=1m

Games to Support:
* Build Menu System [done, sorta]
* Doom 1
* Doom 2
* Warcraft 2 [done]
* Warcraft 1 [done]
* Duke Nuk'em
* Duke3d
* Heroes of Might and Magic 3 (win95) [hangs]
* Gauntlet (?)
* Game emulator - https://www.retrostic.com/roms

Reference Links:
* https://dosbox-x.com/wiki/Guide%3ASetting-up-networking-in-DOSBox%E2%80%90X
* https://www.dosdays.co.uk/topics/Manufacturers/s3_downloads.php
* https://dosbox-x.com/wiki/Guide%3AInstalling-Windows-95
* https://magpi.raspberrypi.com/articles/run-windows-98-on-raspberry-pi-with-dosbox-x
* https://www.raspberrypi.com/news/read-floppy-disks-and-cd-roms-with-raspberry-pi-5-magpimonday/
