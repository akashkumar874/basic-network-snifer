from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        print("\n=== Packet Captured ===")
        print("Source IP:", ip_layer.src)
        print("Destination IP:", ip_layer.dst)

        if TCP in packet:
            print("Protocol: TCP")
        elif UDP in packet:
            print("Protocol: UDP")
        else:
            print("Other Protocol")

print("Sniffing started... Press Ctrl+C to stop.")
sniff(prn=packet_callback, store=False)
