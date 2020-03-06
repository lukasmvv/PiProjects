from gpiozero import LED
from time import sleep

# GPIO6
led_red = LED(6)
# GPIO5
led_green = LED(5)

while True:
    led_red.on()
    led_green.off()
    sleep(1)
    led_red.off()
    led_green.on()
    sleep(1)