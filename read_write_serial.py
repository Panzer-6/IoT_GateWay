from global_init import*

def processData(data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    try:
        if splitData[1] == "BENZENE":
            client.publish("benzene", splitData[2])
            my_data["benzene"] = ord(splitData[2]) - 48
        elif splitData[1] == "CO2":
            client.publish("co2", splitData[2])
            my_data["co2"] = ord(splitData[2]) - 48
        elif splitData[1] == "FILTERMANUAL":
            client.publish("filter-manual", splitData[2])
            my_data["filter-manual"] = ord(splitData[2]) - 48
        elif splitData[1] == "FILTERSMART":
            client.publish("filter-smart", splitData[2])
            my_data["filter-smart"] = ord(splitData[2]) - 48
        elif splitData[1] == "GAS":
            client.publish("gas", splitData[2])
            my_data["gas"] = ord(splitData[2]) - 48
        elif splitData[1] == "HUMID":
            client.publish("humid", splitData[2])
            my_data["moist"] = ord(splitData[2]) - 48
        elif splitData[1] == "NH3":
            client.publish("nh3", splitData[2])
            my_data["nh3"] = ord(splitData[2]) - 48
        elif splitData[1] == "NOX":
            client.publish("nox", splitData[2])
            my_data["nox"] = ord(splitData[2]) - 48
        elif splitData[1] == "PM2DOT5":
            client.publish("pm2-dot-5", splitData[2])
            my_data["pm2.5"] = ord(splitData[2]) - 48
        elif splitData[1] == "TEMP":
            client.publish("temp", splitData[2])
            my_data["temp"] = ord(splitData[2]) - 48
    except:
        pass

def writeSerial(var, value):
    write_data = "!1:" + var + ":" + str(value) + "#"
    ser.write(write_data.encode())

mess = ""
def readSerial():
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
    while ("#" in mess) and ("!" in mess):
        start = mess.find("!")
        end = mess.find("#")
        processData(mess[start:end + 1])
        if (end == len(mess)):
            mess = ""
        else:
            mess = mess[end + 1:]