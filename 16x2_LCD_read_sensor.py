from time import sleep
from datetime import datetime
import bme280
import smbus2
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

# Modify this if you have a different sized character LCD
lcd_columns = 16
lcd_rows = 2

# compatible with all versions of RPI as of Jan. 2019
# v1 - v3B+
lcd_rs = digitalio.DigitalInOut(board.D22)
lcd_en = digitalio.DigitalInOut(board.D17)
lcd_d4 = digitalio.DigitalInOut(board.D25)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d6 = digitalio.DigitalInOut(board.D23)
lcd_d7 = digitalio.DigitalInOut(board.D18)


# Initialise the lcd class
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                      lcd_d7, lcd_columns, lcd_rows)

# wipe LCD screen before we start
lcd.clear()

def get_bme_280_sensor_data():
    port = 1
    address = 0x77
    bus = smbus2.SMBus(port)

    bme280.load_calibration_params(bus,address)
    
    bme280_data = bme280.sample(bus,address)

    temperature = str(round(bme280_data.temperature, 1))
    humidity  = str(round(bme280_data.humidity, 1))
    pressure  = str(round(bme280_data.pressure, 1))

    # print(f"temp: {temperature}, humidity: {humidity}, pressure: {pressure}")
    return [temperature, humidity, pressure]


while True:
    # date and time
    # lcd_line_1 = datetime.now().strftime('%b %d  %H:%M\n')

    # current ip address
    # lcd_line_2 = "temp: 27C, humidity: 51%, air pressure: 1013hPa"

    # combine both lines into one update to the display
    sensor_data = get_bme_280_sensor_data()
    temp = sensor_data[0]
    humidity = sensor_data[1]
    pressure = sensor_data[2]

    lcd_line_1 = f't:{temp}C h:{humidity}%\n'
    lcd_line_2 = f'p:{pressure}'


    lcd.message = lcd_line_1 + lcd_line_2
    


    # lcd.message = lcd_line_1 + lcd_line_2

    sleep(2)
