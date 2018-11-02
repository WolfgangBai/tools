#!/usr/bin/env python 

import sys
import getopt
import socket
import struct
def hostToIp(value):
    if value.isdigit():
        network_value = socket.htonl(long(value))
        print '[network order value]:%s' %network_value
        ip = socket.inet_ntoa(struct.pack("!I", network_value))
        print '[ip]:%s'%ip  
    else:
        print 'The host value must be number'  

def networkToIp(value):
    if value.isdigit():
        host_value = socket.ntohl(long(value))
        print '[host order value]:%s' %host_value
        ip = socket.inet_ntoa(struct.pack("!I", int(value)))
        print '[ip]:%s'%ip  
    else:
        print 'The network value must be number' 

def usage():
    print 'hntoa.py usage:'
    print '-h,--help: show help message.'
    print '-v, --version: show script version.'
    print '-H,--host: input an host order value.'
    print '-N, --network: input an network order value.'

def version():
    print 'hntoa.py 1.0'
def outPut(args):
    print 'Hello, %s'%args
def main(argv):
    try:
        opts, args = getopt.getopt(argv[1:], 'H:N:hv', ['host=','version','help','network='])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
            sys.exit(1)
        elif o in ('-v', '--version'):
            version()
            sys.exit(0)
        elif o in ('-H', '--host'):
            print '[host order value]:%s' %a
            hostToIp(a)

        elif o in ('-N', '--network'):
            print '[network order value]:%s' %a
            networkToIp(a)
            sys.exit(0)

        else:
            print 'error option'
            sys.exit(3)

if __name__ == '__main__':
    main(sys.argv)
