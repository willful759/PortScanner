#!/usr/bin/python3

import socket #library to use
from ports import ports_and_services

def getOpenPorts(target, portRange):
    openPorts = []
    #Obtener el host con socket
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
        #hacer un loop sobre el rango de puertos
        for port in portRange:
            #abrir el socket determinado
            #verificar si se conecta
            try:
                sock.connect((target,port))
                #si se conecta agregarlo al array
                openPorts.append(port)
            except ConnectionRefusedError:
                pass

    return openPorts
