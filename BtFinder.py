import bluetooth


def finder():
        address = []
        nameList = []

        i = 1
        # Scans for nearby Devices
        nearby_devices = bluetooth.discover_devices(lookup_names=True)
        print("found %d devices" % len(nearby_devices))

        # For each device it ouputs the address and name in the console
        for addr, name in nearby_devices:
            i += 1

            print(" %s - %s" % (addr, name))

            address.append(str(addr))
            nameList.append(str(name))

            # Returns the address and Name of each device back to the main file
        return address, nameList

