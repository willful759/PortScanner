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
    if not validate(target):
        return None

    if portRange is None or len(portRange) == 0:
        portRange = ports_and_services.keys()
    else:
        portRange = range(portRange[0],portRange[1] + 1)
    
    openPorts = []
    try:
        ips = socket.gethostbyname_ex(target)[2]
        host = ips[0]
        """
        if set(ips) > 1:
            print(f"scanning {target} ({host}),\nother addresses: {ips}")
        """
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
        pass
        #print(f"failed to resolve: {target}")

    return openPorts
