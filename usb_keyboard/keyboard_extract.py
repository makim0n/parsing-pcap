#!/usr/bin/python3

import sys
import pyshark
import argparse
from base64 import b64decode
from binascii import unhexlify
from layout import *

res = []

def arg_parser():
    """
    :return: Return parsed args
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("FILE", type=str, help="Path to packet capture file")
    parser.add_argument("KEYBOARD", type=str, help="Select keyboard layout. Default: EN")
    parser.add_argument("-f", "--filter", type=str, help="Filter to use on the packet capture. None by default", default="")
    args = parser.parse_args()
    return args

def leftover_extract(cap_obj):
    """
    Function used to extract HID value from USB packet.

    :param @cap_obj: Capture object from PyShark, the PCAP to analyze.
    :return: C{list} containing each HID value.
    """
    leftovers = []
    for pkt in cap_obj:
        try:
            leftovers.append(pkt.data.usb_capdata)
        except:
            pass
    return leftovers

def data_extraction(usb_data, keyboard):
    """
    Translate HID value into ASCII char according to a dictionnary in "layout.py" file.

    :param @usb_data: Each HID value - C{list}
    :param @keyboard: Layout used for translation - C{dict}
    :return: Return the extracted data as a C{str}
    """
    lines = ''
    pos = 0
    
    try:
        for x in usb_data:
            i = int(x[6:8], 16)
            if i == 0:
                continue
            if int(x[0:2], 16) == 2:
                try:
                    lines += keyboard[i][1]
                except:
                    pass
            else:
                try:
                    lines += keyboard[i][0]
                except:
                    pass
    except:
        pass
    return lines

if __name__ == "__main__":
    args = arg_parser()

    try:
        cap = pyshark.FileCapture(args.FILE, display_filter=args.filter)
    except:
        print('[-] Capture file not opened.')
        exit()

    try:
        usb_data = leftover_extract(cap)
    except:
        print('[-] Can\'t read capture object, try cap_object.set_debug(), update your tshark or make sure your packet capture file exist')
        exit()

    try:
        res = data_extraction(usb_data, globals()[args.KEYBOARD.lower()])
        print(str(res))
    except:
        print('Something went wrong during extraction processing :-(')

