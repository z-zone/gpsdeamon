# main.py
# authors: lukas, samuel

# General: sys to communicate with the command line
import sys
# General: socket to use the connection library
import socket

# value-variable als globaler string
value = ''

# the config.py defines all the parameters
import config

# first, the gpsdeamon should decide, if it's the client or the server.
# therefore it should check if the gps-module is installed -> client, or not -> server
instType = true
#if gps.isInstalled() == true:
#    instType = false
# for testing purposes, the installation type is specified by cmd-line argument, later on it should be decided by given modules
instType = sys.argv[1]

# in the gps.py-module the communication with the gps-module is defined
if instType == false:
    import gps
    value = gps.getGps()
# in the parse.py-module (parse) the handling of data-string is defined either the client- or the server-way
import parse
if instType == false:
    value = parse.parse(value)
# in the connect.py-module (connections) the different types of possible connections (gsm, wlan) are defined
import com
if instType == false:
    com.communicate(value)
else:
    value = com.communicate()
# in the save.py-module the saving takes place
if instType == true:
    save.save(value)
