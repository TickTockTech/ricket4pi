import bluetooth
import time

def getDay():
    tm_s = time.localtime(time.time())
    return tm_s.tm_yday

def getDeviceHashTable():
    active_hash = {}
    
    scan_tm = int(time.time())
    tm_str = time.ctime(scan_tm)
    
    try:
        nearby_devices = bluetooth.discover_devices()

        for addr in nearby_devices:
            name = bluetooth.lookup_name( addr )

            active_hash[addr] = (name,scan_tm) 

        #print("{}  - found {} devices".format(tm_str, len(nearby_devices)))
            
    except BluetoothError as e:
        print("BT error %s %s" % (self.name, e))
        
    return active_hash, tm_str

#
#  MAIN
#
hash_tab = {}

tm_s = time.localtime(time.time())
start_day = getDay()

print("Scanning on day: {}".format(start_day))

running = True
while running:
    new_state, tm_str = getDeviceHashTable()
    for mac in new_state:
        if not mac in hash_tab:
            hash_tab[mac] = new_state[mac]
            print("{} ({}) detected".format(hash_tab[mac][0], mac))
    rm_list = []
    for mac in hash_tab:
        if not mac in new_state:
            print("{} ({}) gone".format(hash_tab[mac][0], mac))
            rm_list.append(mac)
    for mac in rm_list:
        del hash_tab[mac]
            
    time.sleep(60)
    running = (start_day == getDay())
    
print("End of day.")