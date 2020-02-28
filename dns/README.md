# DNS Exfiltration script

This tool try to get the extracted data from DNS packet.

Test pcap are available in the `pcap_tests` folder.
---

## How to use

```
usage: dns_extract.py [-h] [-f FILTER] FILE

positional arguments:
  FILE                  Path to packet capture file

optional arguments:
  -h, --help            show this help message and exit
  -f FILTER, --filter FILTER
                        Filter to use on the packet capture. Default is: dns.a
```

---

### chall.pcap

Filter: ip.src == 8.8.8.8 && dns.a
Full cmd: ./dns\_extract.py -f 'ip.src == 8.8.8.8 && dns.a' pcap\_tests/chall.pcap

Output: Hex data with ".evil.com" domain

Flag: cat flag.raw | sed 's/.evil.com//g' | xxd -r -p
You should see a private key
