from datetime import datetime
from time import sleep
from gpiozero import LED, Button
import csv
import Adafruit_DHT
import I2C_LCD_driver

# GPIO6
led_red = LED(6)
# GPIO5
led_green = LED(5)
#GPIO18
button = Button(18)

# Setting up Temp and Hum Sensor
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 17    # GPIO17 pin of dht22 date

# Creating LCD object
lcd = I2C_LCD_driver.lcd()
lcd.lcd_display_string('Starting...',1,0)
sleep(2)
lcd.lcd_clear()
cleared = False

isOn = True

count = 0

# Always looping
while True:

    # Checking if button is pressed
    if button.is_pressed:
        isOn = not isOn
        #print('pressed')
        lcd.lcd_display_string('X',2,15)
        button.wait_for_release()

    # Checking status and turning LEDs on/off
    #lcd.lcd_clear()
    #lcd.lcd_display_string('before if',1,0)
    if isOn:
        led_red.off()
        led_green.on()
        #lcd.lcd_clear()
        #lcd.lcd_display_string('in if',1,0)

        # Getting temperature and humidity
        
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)    
        

        #lcd.lcd_clear()
        #lcd.lcd_display_string('after tf',1,0)

        if humidity is not None and temperature is not None:

            # Getting timestamp
            dateTimeObj = datetime.now()
            timestampStr = dateTimeObj.strftime("%d-%m-%Y %H:%M:%S")

            # Setting up data list
            data = [timestampStr, str(round(temperature,1)), str(round(humidity,1))]

            # Writing data to csv file
            path = r'/home/pi/PiProjects/TempHum/tempHumData.csv'
            with open(path,'a') as f:
                writer = csv.writer(f,delimiter=',')
                writer.writerow(data)

            # Printing latest data to console
            print(data[0] + ' || ' + data[1] + ' || ' + data[2])

            # Write data to LCD
            tempString = 'T:'+data[1]+'C'
            humString = 'H:'+data[2]+'%'
            lcd.lcd_display_string(data[0], 1, 0)
            lcd.lcd_display_string(tempString, 2, 0)
            lcd.lcd_display_string(humString, 2, len(tempString)+1)
            cleared = False
        else:
            lcd.lcd_display_string('Error reading data!',1,0)
            #print("Failed to read data.")
    else:
        led_red.on()
        led_green.off()
        if not cleared:
            lcd.lcd_clear()
            cleared = True
        lcd.lcd_display_string('Sensor off.',1,0)

    count=count+1
    if count > 10:
        count = 0

    lcd.lcd_display_string(str(count),2,15)
    sleep(0.1)


    
