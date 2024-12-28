# **Information Security Project: Wi-Fi Jammer**

## **Introduction**  
The Wi-Fi Jammer is a sophisticated Python-based tool designed to simulate deauthentication attacks within a controlled and authorized environment. This project is intended to raise awareness about vulnerabilities in wireless networks, offering practical insights for security researchers and professionals to enhance network defenses.  

**⚠️ Important:** This tool is exclusively for educational and ethical use. Unauthorized deployment is strictly prohibited and may have legal consequences.

---

## **Key Features**  
- **Comprehensive Device Disconnection:** Sends deauthentication packets to disconnect all devices connected to a specified Wi-Fi access point.  
- **Realistic Simulation:** Provides an authentic representation of deauthentication attacks for security evaluation and learning.  
- **Proactive Security Assessment:** Facilitates the identification of vulnerabilities in Wi-Fi networks and supports the development of effective countermeasures.  

---

## **System Requirements**  
To utilize this tool, ensure the following prerequisites are met:  
1. **Python Environment:** Python 3 installed.  
2. **Libraries and Tools:**  
   - [Scapy Library](https://scapy.net): Used for crafting and transmitting network packets.  
   - [Aircrack-ng Suite](https://www.aircrack-ng.org): Essential for managing Wi-Fi network tasks.  
3. **Hardware:** A Wi-Fi adapter capable of monitor mode and packet injection.

---

## **Installation & Usage**  

### **Installation:**  
1. Install Python and verify the availability of `pip` for package management.  
2. Install the Scapy library by running:  
   ```bash
   pip install scapy
   ```  
3. Set up the Aircrack-ng suite and configure your Wi-Fi adapter to operate in monitor mode.

### **Execution:**  
1. Clone the repository or download the script (`deauth.py`).  
2. Open a terminal and execute the script:  
   ```bash
   python deauth.py
   ```  
3. Follow the on-screen prompts to conduct the attack simulation on a **pre-authorized** Wi-Fi network.

### **Documentation:**  
For a detailed explanation of the setup, execution process, and troubleshooting steps, refer to the accompanying project report.

---

## **Educational Objectives**  
This project is designed to:  
- **Expose Wireless Vulnerabilities:** Highlight the risks associated with insecure Wi-Fi configurations.  
- **Explain Deauthentication Attacks:** Provide insights into how deauthentication packets can disrupt wireless connectivity.  
- **Promote Security Best Practices:** Advocate for the implementation of robust encryption and authentication protocols to prevent such attacks.  

---

## **Legal Disclaimer**  
This tool is developed exclusively for **educational purposes** to raise awareness about wireless network vulnerabilities. **Unauthorized use is strictly prohibited** and may result in severe legal consequences. Ensure explicit permission is obtained before testing any network.  

**The developers are not liable for any misuse or damages arising from the unauthorized application of this tool.**

---
