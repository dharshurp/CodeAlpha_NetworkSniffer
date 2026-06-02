from scapy.all import sniff, IP, TCP, UDP

def process_packet(packet):
if packet.haslayer(IP):
ip = packet[IP]

print("\n==============================")  
    print(f"Source IP: {ip.src}")  
    print(f"Destination IP: {ip.dst}")  
    print(f"Protocol: {ip.proto}")  

    if packet.haslayer(TCP):  
        print("Protocol Type: TCP")  
    elif packet.haslayer(UDP):  
        print("Protocol Type: UDP")  

    payload = bytes(ip.payload)  
    if payload:  
        print("Payload (first 50 bytes):", payload[:50])

print("Starting Network Sniffer... Press Ctrl+C to stop")
sniff(prn=process_packet, store=False)

