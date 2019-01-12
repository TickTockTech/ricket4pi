import serial
import time
import ntplib

def _sendBreak():
    _clearStream()
    ser.write("\r".encode())
    time.sleep(0.1)

def _clearStream():
    inLine = ser.readline()
    while inLine and inLine != "":
        time.sleep(0.01)
        inLine = ser.readline()

def _dumpStream():
    inLine = ser.readline()
    while inLine and inLine != "":
        print("OUT: {}".format(inLine))
        time.sleep(0.01)
        inLine = ser.readline()

def init():
    global ser
    ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
    ser.close()
    ser.open()

    print("Started monitoring system statistics for micro:bit display.")

    _sendBreak()
    ser.write("from microbit import * \r".encode())
    time.sleep(0.1)
    ser.write("import radio \r".encode())
    time.sleep(0.1)
    ser.write("import speech \r".encode())
    time.sleep(0.1)
    ser.write("radio.on() \r".encode())
    time.sleep(0.1)
    ser.write("radio.config(length=128, channel=13, group=42, address=0x11235813, data_rate=radio.RATE_250KBIT) \r".encode())
    time.sleep(0.1)
    ser.write("display.clear() \r".encode())
    time.sleep(0.1)
    ser.write("time_os = 0 \r".encode())
    time.sleep(0.1)
#    _dumpStream()
    _clearStream()

def displayMsg(message):
    _clearStream()
    ser.write("display.scroll(\"{}\") \r".format(message).encode())
    
def displayImg(img):
    _clearStream()
    ser.write("display.show(Image.{}) \r".format(img.upper()).encode())
    
def getAccelerometer():
    _clearStream()
    ser.write("print(\"{},{},{}\".format(accelerometer.get_x(), accelerometer.get_y(), accelerometer.get_z()))\r".encode())
    time.sleep(0.1)
    echo = ser.readline()
    time.sleep(0.1)
    response = ser.readline().strip().split(",")
    intResp = []
    for digit in response:
        intResp.append(int(digit))
    return intResp

def getTemperature():
    _clearStream()
    ser.write("print(temperature())\r".encode())
    time.sleep(0.1)
    echo = ser.readline()
    time.sleep(0.1)
    response = ser.readline()
    return int(response.strip())

def isCompassCalibrated():
    _clearStream()
    ser.write("print(compass.is_calibrated())\r".encode())
    time.sleep(0.1)
    echo = ser.readline()
    time.sleep(0.1)
    response = ser.readline()
    return response.strip() == "True"

# This locks up if the compass is not calibrated
def getCompassHeading():
    _clearStream()
    ser.write("print(str(compass.heading()) if compass.is_calibrated() else \"None\")\r".encode())
    time.sleep(0.1)
    echo = ser.readline()
    time.sleep(0.1)
    response = ser.readline().strip()
    return None if response == "None" else response

def calibrateCompass():
    _clearStream()
    ser.write("compass.calibrate() \r".encode())

def echoMessage(message):
    _clearStream()
    ser.write("print(\"{}\")\r".format(message).encode())
    time.sleep(0.1)
    echo = ser.readline()
    time.sleep(0.1)
    response = ser.readline()
    return response.strip()

def speak(message):
    _clearStream()
    ser.write("speech.say(\"{}\") \r".format(message).encode())
    time.sleep(0.1)
    echo = ser.readline()
    print(echo)

def radioCheck():
    _clearStream()
    ser.write("print(radio.receive()) \r".encode())
    time.sleep(0.1)
    echo = ser.readline()
    time.sleep(0.1)
    response = ser.readline().strip()
    return None if response == "None" else response

def radioSend(message):
    _clearStream()
    ser.write("radio.send(\"{}\") \r".format(message).encode())

def setNTPTime(ntpserver):
    _clearStream()
    
    ntp_client = ntplib.NTPClient()
    print("Sync Micro:Bit to {}".format(ntpserver))

    # Provide the respective ntp server ip in below function
    response = ntp_client.request(ntpserver, version=3)
    
    time_str = time.ctime(response.tx_time)
    
    ser.write("print( int( running_time() / 1000 )) \r".encode())
    time.sleep(0.1)
    echo = ser.readline()
    time.sleep(0.1)
    running_time = int(ser.readline().strip())
    
    time_os = int(response.tx_time) - running_time
    ser.write("time_os = {} \r".format(time_os).encode())
    
    print("Setting time to: {}".format(time_str))

def getTime():
    _clearStream()
    ser.write("print( int( running_time() / 1000 ) + time_os ) \r".encode())
    time.sleep(0.1)
    echo = ser.readline()
    time.sleep(0.1)
    time_est = ser.readline().strip()
    epoch_sec = int(time_est)
    
    return epoch_sec
