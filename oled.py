from board import SCL, SDA
import busio
from oled_text import OledText

i2c = busio.I2C(SCL, SDA)

# Create the display, pass its pixel dimensions
oled = OledText(i2c, 128, 64)

# Write to the oled
oled.text("Hello ...", 1)  # Line 1
oled.text("... world!", 2)  # Line 2

Display layouts
There are a few preset layouts for both the 32px and 64px versions of the display. To select one, do e.g.:

oled.layout = Layout64.layout_1big_center()

Or you can define your own layout:

oled.layout = {
	1: SmallLine(0, 0),
	2: BigLine(5, 15, font="Arimo.ttf", size=24),
	3: BigLine(5, 40, font="Arimo.ttf", size=18)
}

The TrueType fonts are loaded from the included fonts folder.

Icons
To display icons, the FontAwesome Solid font is included. Select an icon from https://fontawesome.com/cheatsheet/free/solid, look up its unicode code and print it. Example:

The battery-full icon has the code f240.

# Select a layout with a FontAwesome font
oled.layout = Layout64.layout_icon_only()

# To print unicode characters, prefix them with \u
oled.text('\uf240', 1)
Automatic and manual updates
By default, every call to oled.text() will redraw the full display. If you need to set multiple lines at once, you might want to set oled.auto_show = False and use oled.show() when all lines are set.

More advanced examples
To see these examples, run: python3 -m oled_text.oled_text

import time
import busio
from board import SCL, SDA

from oled_text import OledText, Layout64, BigLine, SmallLine

""" Examples for a 128x64 px SSD1306 oled display. """

i2c = busio.I2C(SCL, SDA)

# Instantiate the display, passing its dimensions (128x64 or 128x32)
oled = OledText(i2c, 128, 64)

# A single FontAwesome icon (https://fontawesome.com/cheatsheet/free/solid)
oled.layout = Layout64.layout_icon_only()
oled.text('\uf58b', 1)
time.sleep(2)

# Output 5 lines (with auto_draw on, the display is painted after every line)
oled.layout = Layout64.layout_5small()
for i in range(1, 6):
	oled.text("Hello Line {}".format(i), i)
time.sleep(1)

# Replacing a single line (keeps the other lines)
oled.text("Brave new line", 2)
time.sleep(1)

# Setting multiple lines with manual .show() (only one display refresh)
oled.layout = Layout64.layout_1big_3small()
oled.auto_show = False
oled.text("The Title", 1)
oled.text("Line 2 text", 2)
oled.text("Line 3 text", 3)
oled.text("Line 4 text", 4)
oled.show()
oled.auto_show = True
time.sleep(2)

# A panel with 3 lines and 3 icons to the right
oled.layout = Layout64.layout_3medium_3icons()
oled.auto_show = False
oled.text("Temperature: ", 1)
oled.text("Light: ", 2)
oled.text("Humidity: ", 3)
oled.text('\uf062', 4)
oled.text('\uf061', 5)
oled.text('\uf063', 6)
oled.show()
oled.auto_show = True
time.sleep(0.5)
oled.text('\uf063', 4)
time.sleep(2)

# With a FontAwesome icon (https://fontawesome.com/cheatsheet/free/solid)
oled.layout = Layout64.layout_icon_1big_2small()
oled.auto_show = False
oled.text('\uf58b', 1)
oled.text("Meow!", 2)
oled.text("I am the", 3)
oled.text("cool cat", 4)
oled.show()
oled.auto_show = True
time.sleep(3)

# Use a custom display layout
# Either use the provided fonts, or give a full path to your own
oled.layout = {
	1: SmallLine(0, 0),
	2: BigLine(5, 15, font="Arimo.ttf", size=24),
	3: BigLine(5, 40, font="Arimo.ttf", size=18)
}
oled.text("I want my layout!")
oled.text("Custom 1", 2)
oled.text("Custom 2", 3)
time.sleep(3)

# Adding own graphics using an onDraw handler
oled.layout = Layout64.layout_1big_center()
oled.on_draw = lambda draw: draw.rectangle((0, 0, 127, 63), outline=255, fill=0)
oled.text("The Fat Cat", 1)

time.sleep(4)
oled.clear()