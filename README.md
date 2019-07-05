# ORP Rig Control Module
The ORP Rig Control Module is a module to add the ability to control supported radios remotely by DTMF tones. This is a more advanced modules and requires the use of the HamLib Library which must also be installed. Radio support is limited in part by what HamLib supports.

THIS MODULE IS CURRENTLY IN EARLY DEVELOPMENT AND TESTING. 

### Install HamlIb as root:
apt install libhamlib-utils

### Add svxlink user to port group:
i.e. /dev/ttyUSB0

### Add user svxlink to group dialout
usermod -a -G dialout svxlink