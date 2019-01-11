import serial, psutil, time
import micro_api

# TEST
#print getTemperature()
micro_api.init()

print("Echo: {}".format(micro_api.echoMessage("Echo")))
#micro_api.displayImg("pacman")
#print("Temp: ", micro_api.getTemperature())
#print("Compass calibrated: ", micro_api.isCompassCalibrated())
#print("Compass heading: ", micro_api.getCompassHeading())
#print("Accelerometer: ", micro_api.getAccelerometer())
#micro_api.speak("Hello")
micro_api.setNTPTime('uk.pool.ntp.org')
#micro_api.radioSend("Hello everyone!")
'''for i in range(60):
    receive = micro_api.radioCheck()
    if receive != None:
        print("RADIO:", receive)
        if receive.startswith("Speak:"):
            receive = receive[6:].strip()
            micro_api.speak(receive)
    time.sleep(0.5)'''
epoch_sec = micro_api.getTime()
time_str = time.ctime(epoch_sec)
print("Micro:bit time:".format(time_str))
