# Raspberry-Pi-NightVisionGoggles
Raspberry Pi Wireless Zero Night Vision Goggles
With this project I decided to create some inexpensive night vision goggles with a Raspberry Pi Zero Wireless.<BR /><BR />

Raspberry Pi Wireless Zero <BR />
1080p IR Camera<BR />
Flash SD Memory Card<BR />
Power source<BR />
Mini HDMI cable<BR />
3.2 HDMI LCD<BR />
<BR /><BR />

Tasks:<BR /><BR />
Setup Wireless connectivity<BR />
Expand storage<BR />
Enable Camera<BR />
Push updates<BR />
autologin<BR />
Setup Monitor rotate if needed<BR />

# Wireless Supplicant file
Location: Root<BR /><BR />

wpa_supplicant.conf<BR />
country=US<BR />
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev<BR />
update_config=1<BR /><BR />

network={<BR />
    ssid="NETWORKNAME"<BR />
    psk="NETWORKPASSWORD"<BR />
}<BR />

# Camera rotate
Location: /boot/config.txt<BR />
display_hdmi_rotate=3<BR />

# Install time pulg-in for Python

# Copy runcam to home and set to run automatically
copy runcam.py to /home/pi<BR />
nano /home/pi/.bashrc<BR />

echo Running at boot <BR />
sudo python3 /home/pi/runcam.py<BR />
 
## Connect with me at

<a href="https://twitter.com/HMInfoSecViking?ref_src=twsrc%5Etfw"><IMG SRC="https://github.com/bvoris/bvoris/blob/master/twitter.jpg" WIDTH=10% HEIGHT=10% ALIGN=LEFT></a>

<a href="https://www.linkedin.com/in/brad-voris" target="_blank"><IMG SRC="https://github.com/bvoris/bvoris/blob/master/linkedin.png" WIDTH=10% HEIGHT=4% ALIGN=RIGHT></a>

<BR /><BR />
<BR /><BR />

<A HREF="https://www.victimoftechnology.com">Victim Of Technology<A />
<BR /><BR />
<A HREF="https://www.cyberforgesecurity.com">Cyber 
