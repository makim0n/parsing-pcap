# ICMP Exfiltration script

This tool try to get the extracted data from ICMP packet.

Test pcap are available in the `pcap_tests` folder.
---

## How to use

```bash
usage: icmp_extract.py [-h] [-f FILTER] FILE

positional arguments:
  FILE                  Path to packet capture file

optional arguments:
  -h, --help            show this help message and exit
  -f FILTER, --filter FILTER
                        Filter to use on the packet capture. Default is: icmp
```

---

### analysis.pcap

Filter: icmp.resp\_to

Output: Base64 data

Flag: cat flag.raw | base64 -d

### test.pcapng

Filter: icmp

Output: Hex data

Flag: cat flag.raw | xxd -r -p
