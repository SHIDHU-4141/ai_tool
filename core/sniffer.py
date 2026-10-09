from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        proto = 'TCP' if packet.haslayer(TCP) else ('UDP' if packet.haslayer(UDP) else 'OTHER')
        print(f'[PACKET] {ip_layer.src} -> {ip_layer.dst} | Protocol: {proto}')

def start_sniffer(packet_count=10):
    print(f'[*] Starting packet capture (capturing {packet_count} packets)...')
    sniff(count=packet_count, prn=packet_callback, store=False)
