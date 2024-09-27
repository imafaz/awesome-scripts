from scapy.all import *

def dns_monitor(pkt):
    if pkt.haslayer(DNSQR):
        print(pkt[DNSQR].qname)

sniff(filter="udp port 53", prn=dns_monitor)