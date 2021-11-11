#!/usr/bin/python3

import socket #library to use https://docs.python.org/3/library/socket.html
from ports import ports_and_services

def getOpenPorts(target, portRange=None):
    openPorts = []
    if portRange is None:
        portRange = ports_and_services.keys()
    #hacer un loop sobre el rango de puertos
    for port in portRange:
        #verificar si se conecta
        try:
            #Obtener el host con socket
            s = socket.create_connection((target,port))
            #si se conecta agregarlo al array
            openPorts.append(port)
            s.close()
        except ConnectionRefusedError:
            pass

    return openPorts
