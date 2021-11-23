#!/usr/bin/python3

import socket #library to use https://docs.python.org/3/library/socket.html
from ports import ports_and_services
from urllib.parse import urlparse

def validate(url):
    try:
        urlparse(url)
        return True
    except:
        return False

def getOpenPorts(target, portRange=None,verbose=False):
    # validate url
    if not validate(target):
        return None
    
    #handle possible ip port ranges
    if portRange is None or len(portRange) == 0:
        portRange = ports_and_services.keys()
    else:
        portRange = range(portRange[0],portRange[1] + 1)

    try:
        #find the appropiate ip for the given url
        ips = socket.gethostbyname_ex(target)[2]
        host = ips[0]
        openPorts = []
        for port in portRange:
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(0.5)
            if not sock.connect_ex((host,port)):
                if verbose:
                    openPorts.append((port,ports_and_services.get(port)))
                else:
                    openPorts.append(port)
            sock.close()
    except socket.gaierror:
        """
        this exception is raised when 
        the domain has no ip associated
        with it
        """
        return None
  
    return openPorts
