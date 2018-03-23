# connect.py
# authors: lukas, samuel

if instType == "s":
    ssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('', 5112)
    sock.bind(server_address)
    sock.listen(5)
    while 1:
        connection, client_address = ssock.accept()
elif instType == "c":
    csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # specify the address of server - in final version the dyndnsname should be here, but not shown to everyone now
    server_address = (sys.argv[2], 5112)
    csock.connect(server_adress)
else
    raise RuntimeError("Installation Type not specified")
