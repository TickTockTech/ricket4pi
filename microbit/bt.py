import bluetooth

print("performing inquiry...")

try:
    nearby_devices = bluetooth.discover_devices()

    for addr in nearby_devices:
        name = bluetooth.lookup_name( addr )

        print("\tDevice: {}, {}".format(addr, name)) 

    print("found %d devices" % len(nearby_devices))
        
except BluetoothError as e:
    print("BT error %s %s" % (self.name, e))
