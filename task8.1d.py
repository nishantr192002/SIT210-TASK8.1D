### I2C communication ###
""" I2C (Inter-Integrated Circuit) is a two-wire communication protocol for connecting electronic devices. 
    It features a master-slave structure, unique device addressing, synchronous data exchange, 
    and bidirectional communication, making it widely used in interconnecting sensors and peripherals with microcontrollers.
""" 
# Import the 'smbus' and 'time' modules for I2C communication and time delays.
import smbus
import time

# Define the I2C address for the light sensor.
Bmp_Light_Sensor = 0x23

# Define some constants for configuring the sensor.
Low = 0x00
High = 0x01
Reset = 0x07
High_Definition_mode = 0X23

# Initialize the I2C bus with bus number 1.
carry_bus = smbus.SMBus(1)

# Function to calculate light intensity from the sensor's data.
def Light_intensity(light_address):
    result = ((light_address[1] + (256 * light_address[0])) / 1.2)
    return result

# Function to read and return the light intensity from the sensor.
def light():
    # Read data from the sensor in high-definition mode.
    light_address = carry_bus.read_i2c_block_data(Bmp_Light_Sensor, High_Definition_mode)
    # Calculate the light intensity and return it.
    value = Light_intensity(light_address)
    return value

# Main function to continuously read and display light intensity.
def main():
    while True:
        # Read the light intensity.
        lux = light()
        # Print the light intensity value.
        print(lux)

        # Provide simple feedback based on the light intensity.
        if lux >= 1450:
            print("Too bright")
        elif 700 <= lux < 1350:
            print("Bright")
        elif 350 <= lux < 750:
            print("Medium")
        elif 51 <= lux < 300:
            print("Dark")
        elif lux < 50:
            print("Too Dark")
        
        # Wait for 0.5 seconds before taking another reading.
        time.sleep(0.5)

# Start the main function.
main()
