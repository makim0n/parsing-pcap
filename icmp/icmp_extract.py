#!/usr/bin/python3

import sys
import pyshark
import argparse
from base64 import b64decode
from binascii import unhexlify

buf = ''

def arg_parser():
    """
    :return: Return parsed args
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("FILE", type=str, help="Path to packet capture file")
    parser.add_argument("-f", "--filter", type=str, help="Filter to use on the packet capture. Default is: icmp", default="icmp")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = arg_parser()

    # Filter on echo reply only
    # If output file is empty, try to change the Wireshark filter
    try:
        cap = pyshark.FileCapture(args.FILE, display_filter=args.filter)
    except:
        print('[-] Capture file not opened.')
        exit()

    # Extract data from ICMP request
    #for pkt in cap:
    try:
        for pkt in cap:
            buf += pkt.icmp.data
    except:
        print('[-] Can\'t read capture object, try cap_object.set_debug(), update your tshark or make sure your packet capture file exist')
        exit()
    
    data = str(unhexlify(buf))[2:-1].replace('\\n','')
    if data != '':
        try:    
            f = open('flag.raw', 'w+')
            f.write(data)
            f.close()
            print('[+] File "flag.raw" written :)')
        except:
            print('[-] File not properly written. Something went wrong :(')
            exit()
    else:
        print('[-] No data found. Try to edit the filter.')
        exit()
