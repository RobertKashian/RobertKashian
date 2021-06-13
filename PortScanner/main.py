from socket import *

def conScan(tgtHost, tgtPort):
    try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.connect((tgtHost, tgtPort))
        print('[1] %d /tcp open'% tgtPort)
        connskt.close()
    except:
        print('[0] %d /tcp closed'% tgtPort)

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('[0] Cannot resolve %s '% tgtHost)
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n[1] Scan result of: %s '% tgtName[0])
    except:
        print('\n[1] Scan result of: %s ' % tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('Scanning Port: %d'% tgtPort)
        conScan(tgtHost, int(tgtPort))

if __name__ == '__main__':
    portScan('google.com',[80, 22, 56, 41, 12])