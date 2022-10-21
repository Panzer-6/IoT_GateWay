# import random
import time
from read_write_serial import*

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


    # Extracting data for the displaying on the app
    data_file = open("data.json")
    my_data = json.load(data_file)
    if isMicrobitConnected:
        if (my_data["write"] == 1):
            my_data["write"] = 0
            writeSerial("ONOFF", my_data["on-off"])
        readSerial()
    data_file = open("data.json", "w")
    json.dump(my_data, data_file)
    data_file = open("data.json", "r")
    print("Data extracted")
    time.sleep(10)
