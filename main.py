# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import serial.tools.list_ports
import sys
import random
import time
import json
from Adafruit_IO import MQTTClient

AIO_FEED_ID = ["benzene", "co2", "filter-manual", "filter-smart", "gas", "moist", "nh3", "nox", "pm2-dot-5", "temp"]
AIO_USERNAME = "TungVan"
AIO_KEY = "aio_RImb95kq0JZmgCsmRGOAqpTzpjGA"

my_data = {"benzene": "",
           "co2": "",
           "filter-manual": "",
           "filter-smart": "",
           "gas": "",
           "moist": "",
           "nh3": "",
           "nox": "",
           "pm2.5": "",
           "temp": "",
           "on-off": "",
           "write": ""}

def connected(client):
    print("Ket noi thanh cong ...")
    for feed in AIO_FEED_ID:
        client.subscribe(feed)
def subscribe( client , userdata , mid , granted_qos ) :
    print("Subcribe thanh cong ...")

def disconnected(client) :
    print("Ngat ket noi ...")
    sys.exit(1)

def message( client , feed_id , payload ):
    print ("Nhan du lieu : " + payload )
    if isMicrobitConnected:
        ser.write((str(payload) + "#").encode())

def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range (0, N):
        port = ports[i]
        strPort = str(port)
        if "com0com - serial port emulator" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    return commPort

isMicrobitConnected = False
if getPort() != "None":
    ser = serial.Serial(port = getPort(), baudrate = 115200)
    isMicrobitConnected = True

def processData(data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    try:
        if splitData[1] == "BENZENE":
            client.publish("benzene", splitData[2])
            #print("Benzene is updated")
            my_data["benzene"] = splitData[2]
            #print(my_data['benzene'])
        elif splitData[1] == "CO2":
            client.publish("co2", splitData[2])
            #print("CO2 is updated")
            my_data["co2"] = splitData[2]
            #print(my_data["co2"])
        elif splitData[1] == "FILTERMANUAL":
            client.publish("filter-manual", splitData[2])
            #print("Filter-manual is updated")
            my_data["filter-manual"] = splitData[2]
            #print(my_data["filter-manual"])
        elif splitData[1] == "FILTERSMART":
            client.publish("filter-smart", splitData[2])
            #print("Filter-smart is updated")
            my_data["filter-smart"] = splitData[2]
            #print(my_data["filter-smart"])
        elif splitData[1] == "GAS":
            client.publish("gas", splitData[2])
            #print("Gas is updated")
            my_data["gas"] = splitData[2]
            #print(my_data["gas"])
        elif splitData[1] == "MOIST":
            client.publish("moist", splitData[2])
            #print("Moist is updated")
            my_data["moist"] = splitData[2]
            #print(my_data["moist"])
        elif splitData[1] == "NH3":
            client.publish("nh3", splitData[2])
            #print("NH3 is updated")
            my_data["nh3"] = splitData[2]
            #print(my_data["nh3"])
        elif splitData[1] == "NOX":
            client.publish("nox", splitData[2])
            #print("NOx is updated")
            my_data["nox"] = splitData[2]
            #print(my_data["nox"])
        elif splitData[1] == "PM2DOT5":
            client.publish("pm2-dot-5", splitData[2])
            #print("PM2.5 is updated")
            my_data["pm2.5"] = splitData[2]
            #print(my_data["pm2.5"])
        elif splitData[1] == "TEMP":
            client.publish("temp", splitData[2])
            #print("Temp is updated")
            my_data["temp"] = splitData[2]
            #print(my_data["temp"])
    except:
        pass

mess = ""

def writeSerial(var, value):
    write_data = "!1:" + var + ":" + str(value) + "#"
    ser.write(write_data.encode())

def readSerial():
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        print(mess)
    while ("#" in mess) and ("!" in mess):
        start = mess.find("!")
        end = mess.find("#")
        print(mess[start:end + 1])
        processData(mess[start:end + 1])
        if (end == len(mess)):
            mess = ""
        else:
            mess = mess[end + 1:]

client = MQTTClient( AIO_USERNAME , AIO_KEY )
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

data_file = open("data.json", 'w')
json.dump(my_data, data_file)
data_file = open("data.json", 'r')
print("Data initialized")

def on_off():
    my_data["on-off"] = 1 - my_data["on-off"]
    my_data["write"] = 1

while True:
#    time.sleep(10)
#    my_data["benzene"] = random.randint(1, 100)
#    my_data["co2"] = random.randint(1, 100)
#    my_data["filter-smart"] = random.randint(1, 100)
#    my_data["filter-manual"] = random.randint(1, 100)
#    my_data["gas"] = random.randint(1, 100)
#    my_data["moist"] = random.randint(1, 100)
#    my_data["nh3"] = random.randint(1, 100)
#    my_data["nox"] = random.randint(1, 100)
#    my_data["pm2.5"] = random.randint(1, 100)
#    my_data["temp"] = random.randint(1, 100)
#    data_file = open("data.json", 'w')
#    json.dump(my_data, data_file)
#    data_file = open("data.json", 'r')
#    print("Data extracted")
#
#    for feed in AIO_FEED_ID:
#        value = random.randint(0, 100)
#        print("Cap nhat ", feed, ": ", value)
#        client.publish(feed, value)
#    time.sleep(60)
    time.sleep(10)
    #data_file = open("data.json")
    #my_data = json.load(data_file)
    #data_file.close()
    if isMicrobitConnected:
        print("Microbit connected")
        #if (my_data["write"] == 1):
        #    my_data["write"] = 0
        #    writeSerial("ONOFF", my_data["on-off"])
        readSerial()
    print(my_data)
    data_file = open("data.json", 'w')
    json.dump(my_data, data_file)
    data_file = open("data.json", 'r')
    print("Data extracted")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
