from scapy.all import *

def monitor(pkt):
    if pkt.haslayer(TCP) and pkt.haslayer(Raw):
        dst = pkt[IP].dst
        if not dst.startswith('192.168.') and not dst.startswith('10.') and not dst.startswith('172.'):
            print(f'HTTP request to {dst}')


sniff(filter='port 80 or port 443', prn=monitor)