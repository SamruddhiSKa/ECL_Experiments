import BlynkLib
import board
import adafruit_dht
import time

BLYNK_AUTH = 'YOUR_AUTH_TOKEN'

blynk = BlynkLib.Blynk(BLYNK_AUTH, server='blynk.cloud', port=80)

sensor = adafruit_dht.DHT11(board.D4)

print("Starting Blynk DHT11 Monitoring on Raspberry Pi...")

def send_sensor_data():
    try:
        temp = sensor.temperature
        humi = sensor.humidity

        if humi is not None and temp is not None:
            print(f"Blynk Update -> Temp: {temp:.1f}°C | Hum: {humi:.1f}%")
            blynk.virtual_write(0, temp)
            blynk.virtual_write(1, humi)
        else:
            print("Sensor reading failed...")
    except RuntimeError:
        pass
    except Exception as e:
        sensor.exit()
        raise e

last_send_time = 0

while True:
    blynk.run()

    current_time = time.time()
    if current_time - last_send_time > 5:
        send_sensor_data()
        last_send_time = current_time
