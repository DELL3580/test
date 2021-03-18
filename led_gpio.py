from gpiozero import LED
from time import sleep

while True:
    GPIOS=[2,3,6,7,8,9,10,11,12,13,16,17,18,19,20,21]
    for gpio_index in GPIOS:
        print(" Testing GPIO :" +" "+ str(gpio_index))        
        led = LED(gpio_index)
        led.on()
        sleep(3)
        led.off()
        sleep(3)

