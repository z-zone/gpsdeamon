# connect.py
# authors: lukas, samuel

# arg1 should tell if its a server-isntallation (true) oder client (false), arg2 is the ip/dns of server and arg3 is the message that should be sent
def communicate(instType, *options):
    # define the specific length of a possible message
    msglen = 23
    # server version
    if instType == true:
        handler = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('', 5112)
        handler.bind(server_address)
        handler.listen(5)
        while 1:
            ssock, client_address = handler.accept()
        try:
            bytes_recd = 0
            buffers = []
            while bytes_recd < msglen:
                buffer = ssock.recv(min(MSGLEN - bytes_recd, 2048))
                if buffer == '':
                    raise RuntimeError("server lost socket connection")
                else:
                    buffers.append(buffer)
                    bytes_recd += len(buffer)
            # return the full received message
            return ''.join(buffers)
        finally:
            ssock.close()
    # client version
    elif instType == false:
        serverdns = options[0]
        msgstring = options[1]
        csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # specify the address of server - in final version the dyndnsname should be here, but not shown to everyone now
        server_address = (serverdns, 5112)
        csock.connect(server_adress)
        try:
            # send data
            totalsent = 0
            while totalsent < msglen:
                sent = csock.send(msgstring[totalsent:])
                if sent == 0:
                    raise RuntimeError("client lost socket connection")
                totalsent += sent
            return true
        finally:
            csock.close
        
    # no version specified
    else
        raise RuntimeError("Installation Type not clear")
