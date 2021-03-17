import busio
import time
from board import SCL, SDA
from oled_text import OledText, Layout32, BigLine, SmallLine

i2c = busio.I2C(SCL, SDA)
# Create the display, pass its pixel dimensions
oled = OledText(i2c, 128, 32)
oled.layout = Layout32.layout_1big_center()
# Select a layout with a FontAwesome font
oled.layout = Layout32.layout_icon_only()

# To print unicode characters, prefix them with \u
oled.text('\uf240', 1)
time.sleep(2)


########################################################################

 #'\' is used to splite python line
    ipaddress = os.popen("ifconfig wlan0 \
                        | grep 'inet addr' \
                        | awk -F: '{print $2}' \
                        | awk '{print $1}'").read()
    ssid = os.popen("iwconfig wlan0 \
                    | grep 'ESSID' \
                    | awk '{print $4}' \
                    | awk -F\\\" '{print $2}'").read()

    print("ssid: " + ssid)
    print("ipaddress: " + ipaddress)

    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    cmd = "hostname -I | cut -d\' \' -f1"
    IP = subprocess.check_output(cmd, shell = True )

    cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell = True )

    cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
    MemUsage = subprocess.check_output(cmd, shell = True )

    cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
    Disk = subprocess.check_output(cmd, shell = True )
	#################################################################################""






# Use a custom display layout
# Either use the provided fonts, or give a full path to your own
oled.layout = {
	1: SmallLine(0, 0),
	2: BigLine(5, 15, font="Arimo.ttf", size=24),
	3: BigLine(5, 40, font="Arimo.ttf", size=18)
}
oled.text("ssid:"+" "+str(ssid))
time.sleep(3)
oled.clear()
oled.text("IP:"+" "+str(IP))
time.sleep(3)
oled.clear()
oled.text("CPU:"+" "+str(CPU))
time.sleep(3)
oled.clear()

time.sleep(4)
oled.clear()






   