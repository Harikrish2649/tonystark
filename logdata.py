import csv
import time
import Adafruit_BMP.BMP085 as BMP085

sensor = BMP085.BMP085()

csv_file = "sensor_data.csv"

def log_data(temperature, pressure):
  
    with open(csv_file, mode='a') as file:
        writer = csv.writer(file)
        
        writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), temperature, pressure])

with open(csv_file, mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Temperature (C)", "Pressure (Pa)"])

try:
    while True:
        temperature = sensor.read_temperature()
        pressure = sensor.read_pressure()
        
  
        log_data(temperature, pressure)
        
    
        print(f"Logged Data - Temperature: {temperature} °C, Pressure: {pressure} Pa")
        
  
        time.sleep(5)

except KeyboardInterrupt:
    print("Data logging stopped.")
