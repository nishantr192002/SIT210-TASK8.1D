import smbus
import time

Bmp_Light_Sensor = 0x23

Low = 0x00
High = 0x01
Reset = 0x07
High_Definition_mode = 0X23 

carry_bus = smbus.SMBus(1)

def Light_intensity(light_address):
    result = ((light_address[1] + (256 *light_address[0]))/1.2)
    return result

def light():
    light_address = carry_bus.read_i2c_block_data(light_sensor,High_Definition_mode)
    value = Light_intensity(light_address) 
    return value
 
def  main():
    while True:
        lux = light()
        print (lux)

        if(lux >= 1450):
            print("Too bright")
        elif(lux >= 700 and lux < 1350):
            print("Bright")
        elif(lux >= 350 and lux < 750):
            print("Medium")    
        elif(lux < 51 and lux > 300):
            print("Dark")
        elif(lux < 50):
            print("Two Dark")
        
        time.sleep(0.5)
main ()
