import sys
import json
from Adafruit_IO import MQTTClient
from microbit_connection import*

AIO_FEED_ID = ["benzene", "co2", "filter-manual", "filter-smart", "gas", "moist", "nh3", "nox", "pm2-dot-5", "temp"]
AIO_USERNAME = "TungVan"
AIO_KEY = "aio_qIXg17BMn60vIFpBZwQYZMDJkrAO"

def connected(client):
    print("Connection Success ...")
    for feed in AIO_FEED_ID:
        client.subscribe(feed)

def subscribe(client, userdata, mid, granted_qos) :
    print("Subscribe Success ...")

def disconnected(client) :
    print("Stop Connection ...")
    sys.exit(1)

def message(client, feed_id, payload):
    print("Entering value : " + payload )
    if isMicrobitConnected:
        ser.write((str(payload) + "#").encode())

client = MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

my_data = {"benzene": 0,
            "co2": 0,
            "filter-manual": 0,
            "filter-smart": 0,
            "gas": 0,
            "humid": 0,
            "nh3": 0,
            "nox": 0,
            "pm2.5": 0,
            "temp": 0,
            "on-off": 0,
            "write": 0}
data_file = open("data.json", "w")
json.dump(my_data, data_file)
data_file = open("data.json", "r")
print("Data initialized")