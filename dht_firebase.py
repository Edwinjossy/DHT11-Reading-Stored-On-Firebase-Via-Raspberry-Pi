import time
import Adafruit_DHT
import pyrebase

sensor=Adafruit_DHT.DHT11

gpio=21
 
humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)

config = {
  "apiKey": "AIzaSyAVHoVDvvxxxxxxxxxxxxxxxxxxxxxxxx",
  "authDomain": "raxxxxxxxxx.firebaseapp.com",
  "databaseURL": "https://raxxxxxxx-default-rtdb.firebaseio.com",
  "projectId": "raxxxxxxxxxxxx",
  "storageBucket": "raxxxxxx.appspot.com",
  "messagingSenderId": "2859xxxxxxxxx",
  "appId": "1:2859xxxxxxxxxx:web:74eccbxxxxxxxxxx",
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()

print("Send Data to Firebase Using Raspberry Pi")
print("----------------------------------------")
print()

while True:
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')
    data = {
        "Temperature": temperature,
        "Humidity": humidity
        }

    # db.child("mlx90614").child("1-set").set(data)
    # db.child("mlx90614").child("2-push").push(data)
    database.child("DB object name")

    database.set(data)

    time.sleep(8)
