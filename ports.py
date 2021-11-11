#more info protocols tcp https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
ports_and_services = {
    7: 'echo', #https://en.wikipedia.org/wiki/Echo_Protocol
    11: 'systat', #active directory https://en.wikipedia.org/wiki/Systat_(protocol)
    18: 'msp', #message send protocol https://en.wikipedia.org/wiki/Message_Send_Protocol
    19: 'chargen', #character generator https://en.wikipedia.org/wiki/Character_Generator_Protocol
    20: 'ftp', #data transfer https://en.wikipedia.org/wiki/File_Transfer_Protocol
    21: 'ftp', #control (command)  https://en.wikipedia.org/wiki/File_Transfer_Protocol
    22: 'ssh', #secure shell, file transfer (scp, sftp) https://en.wikipedia.org/wiki/Secure_Shell
    23: 'telnet', #unencrypted text communications https://en.wikipedia.org/wiki/Telnet
    25: 'smtp', #email routing https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol
    37: 'time protocol', #important dates 1900, 2036 https://en.wikipedia.org/wiki/Time_Protocol
    42: 'arpa', #hns protocol https://en.wikipedia.org/wiki/ARPA_Host_Name_Server_Protocol
    43: 'whois', #https://en.wikipedia.org/wiki/WHOIS
    52: 'xns', #xerox network systems https://en.wikipedia.org/wiki/Xerox_Network_Systems
    53: 'dns', #domain name system https://en.wikipedia.org/wiki/Domain_Name_System
    67: 'dhcp', #dynamic host configuration protocol (bootp) https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol
    68: 'dhcp',
    69: 'tftp', #trivial file transfer protocol https://en.wikipedia.org/wiki/Trivial_File_Transfer_Protocol
    70: 'gopher', #gopher protocol https://en.wikipedia.org/wiki/Gopher_(protocol)
    79: 'fp', #finger protocol https://en.wikipedia.org/wiki/Finger_(protocol)
    80: 'http', #hypertext transfer protocol https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol
    81: 'onion', #torpark onion https://en.wikipedia.org/wiki/Onion_routing
    88: 'kerberos', #https://en.wikipedia.org/wiki/Kerberos_(protocol)
    106: 'macos', #macos server https://en.wikipedia.org/wiki/MacOS_Server
    107: 'rtelnet', #remote user telnet service https://en.wikipedia.org/wiki/Rtelnet
    108: 'sna', #ibm system network arquitecture https://en.wikipedia.org/wiki/Systems_Network_Architecture
    109: 'pop2', #post office protocol v2 https://en.wikipedia.org/wiki/Post_Office_Protocol
    110: 'pop3', #post office protocol v3
    111: 'rpc', #open network remote procedure call https://en.wikipedia.org/wiki/Sun_RPC
    123: 'ntp', #network time protocol https://en.wikipedia.org/wiki/Network_Time_Protocol
    137: 'netbios', #name service https://en.wikipedia.org/wiki/NetBIOS
    138: 'netbios', #datagram service
    139: 'netbios', #session service
    143: 'imap4', #internet message access protocol https://en.wikipedia.org/wiki/Internet_Message_Access_Protocol
    443: 'https', #hyper text transfer protocol secure https://en.wikipedia.org/wiki/HTTPS
    513: 'rlogin', #https://en.wikipedia.org/wiki/Berkeley_r-commands
    540: 'uucp', #Unix-to-Unix Copy Protocol https://en.wikipedia.org/wiki/UUCP
    554: 'rtsp', #real time streaming protocol https://en.wikipedia.org/wiki/Real_Time_Streaming_Protocol
    587: 'smtp', #email message submission https://en.wikipedia.org/wiki/Message_submission_agent
    873: 'rsync', #file sync protocol https://en.wikipedia.org/wiki/Rsync
    902: 'vmware', #https://en.wikipedia.org/wiki/VMware_ESXi
    989: 'ftps', #ftp over tls https://en.wikipedia.org/wiki/FTPS
    990: 'ftps',
    1194: 'openvpn', #https://en.wikipedia.org/wiki/OpenVPN#Networking
    27017: 'mongodb', #https://docs.mongodb.com/manual/reference/mongodb-wire-protocol/
    3306: 'mysql', #https://en.wikipedia.org/wiki/MySQL
    5000: 'unpn', #https://en.wikipedia.org/wiki/Universal_Plug_and_Play used by many other systems too such as docker
    8080: 'https-proxy', #alternative port for http
    8443: 'https-alt', #alternative port for http

}
