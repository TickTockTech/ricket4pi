import time
import micro_api

number_words = ["zero","one","too","three","for","five","six","seven","ate","nine","ten","eleven","twelve"]

micro_api.init()

micro_api.setNTPTime('uk.pool.ntp.org')

epoch_sec = micro_api.getTime()
time_st = time.localtime(epoch_sec)
next_hr = time_st.tm_hour % 24

while True:
    epoch_sec = micro_api.getTime()
    time_st = time.localtime(epoch_sec)
    
    curr_hr = time_st.tm_hour % 24

    if curr_hr == next_hr:
        next_hr = (next_hr + 1) % 24
        print("Hour: {}".format(curr_hr))
        if curr_hr > 6:
            if curr_hr > 12:
                curr_hr -= 12
            micro_api.speak(number_words[curr_hr] + " o clock")
            
    time.sleep(0.1)