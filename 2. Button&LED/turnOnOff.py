from gpiozero import LED, Button
from time import sleep

# GPIO6
led_red = LED(6)
# GPIO5
led_green = LED(5)

#GPIO18
button = Button(18)

isOn = False

while True:
    
    # Checking if button is pressed
    if button.is_pressed:
        isOn = not isOn
        button.wait_for_release()

    # Checking status and turning LEDs on/off
    if isOn:
        led_red.off()
        led_green.on()
    else:
        led_red.on()
        led_green.off()

    sleep(0.1)