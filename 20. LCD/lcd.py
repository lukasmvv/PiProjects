import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

# mylcd.lcd_display_string(“TEXT TO PRINT”, ROW, COLUMN)
# rows: 1-2
# colums: 0-15
mylcd.lcd_display_string('hello world', 2, 3)
sleep(1)
mylcd.lcd_clear()
