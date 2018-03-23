# main.py
# authors: lukas, samuel

# the config.py defines all the parameters
import config
# in the gps.py-module the communication with the gps-module is defined
import gps

# first, the gpsdeamon should decide, if it's the client or the server.
# therefore it should check if the gps-module is installed -> client, or not -> server
instType = "s"
if gps.isInstalled() == true:
    instType = "c"

# in the parse.py-module (parse) the handling of data-string is defined either the client- or the server-way
import parse
# in the connect.py-module (connections) the different types of possible connections (gsm, wlan) are defined
import connect
# in the talk.py-module the sending/recieving takes place
import talk


# establish the connection to the other part
