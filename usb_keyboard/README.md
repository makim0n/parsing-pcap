# Extraction from USB Keyboard

This tool try to extract HID key from pcap.

### Installation

* Install `tshark` package
* Install PyShark librarie

```bash
$ sudo pacman -S wireshark-gtk # For Arch guys
$ pip install --user -r requirements.txt
$ #ENJOY
```

---

### Usage

```bash
usage: keyboard_extract.py [-h] [-f FILTER] FILE KEYBOARD

positional arguments:
  FILE                  Path to packet capture file
  KEYBOARD              Select keyboard layout. Default: EN

optional arguments:
  -h, --help            show this help message and exit
  -f FILTER, --filter FILTER
                        Filter to use on the packet capture. None by default
```

---

### challenge.pcap

Filter: By default, so no filter

Output: The flag \o/

---

### Known issues

#### Run as root

* Don't run this script as `root` user. PyShark is based on tshark and this script will not run properly (or not run at all).

To reproduce the issue:

```bash
$ sudo pip install -r requirements.txt
$ sudo python
>>> import pyshark
>>> cap = pyshark.FileCapture('SomePcap.pcap')
>>> cap.set_debug()
>>> print(cap[11].data.usb_capdata)
[START OF BIG ERROR OF THE DEATH]
Don't run Wireshark as root user
[END OF BIG ERROR OF THE DEATH]
```

