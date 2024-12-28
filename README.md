# **Information Security Project: Wi-Fi Jammer**

## **Introduction**  
The Wi-Fi Jammer is an advanced Python-based tool designed to simulate deauthentication attacks within a controlled and authorized environment. This project aims to highlight potential vulnerabilities in wireless networks, offering valuable insights for security researchers and professionals to strengthen network defenses.  

**⚠️ Note: This tool is intended solely for educational and ethical use. Unauthorized deployment is strictly prohibited.**

---

## **Key Features**  
- **Device Disconnection:** Sends deauthentication packets to disconnect all devices connected to a specific Wi-Fi access point.  
- **Simulation for Testing:** Provides a realistic simulation of deauthentication attacks to evaluate wireless security.  
- **Security Assessment:** Assists in identifying weaknesses in Wi-Fi networks and devising appropriate countermeasures.

---

## **System Requirements**  
Ensure the following prerequisites are met before using the tool:  
1. **Python Environment:** Python 3 installed.  
2. **Libraries and Tools:**  
   - [Scapy Library](https://scapy.net): For crafting and transmitting network packets.  
   - [Aircrack-ng Suite](https://www.aircrack-ng.org): For handling Wi-Fi network tasks.  
3. **Hardware:** A Wi-Fi adapter supporting monitor mode and packet injection capabilities.

---

## **Installation & Usage**  
1. **Installation:**  
   - Install Python and ensure `pip` is available for package management.  
   - Install the Scapy library:  
     ```bash
     pip install scapy
     ```  
   - Set up the Aircrack-ng suite and configure your Wi-Fi adapter in monitor mode.

2. **Execution:**  
   - Clone the repository or download the script (`deauth.py`).  
   - Run the script in a terminal:  
     ```bash
     python deauth.py
     ```  
   - Follow the on-screen instructions to perform the attack simulation on a **pre-authorized** Wi-Fi network.

3. **Documentation:**  
   - Refer to the detailed project report for setup, execution, and troubleshooting.

---

## **Educational Objectives**  
This project demonstrates:  
- **Wireless Vulnerabilities:** Understanding the risks associated with insecure Wi-Fi configurations.  
- **Deauthentication Mechanisms:** Insights into how deauthentication packets can disrupt wireless networks.  
- **Security Best Practices:** Emphasis on implementing robust encryption and authentication protocols to prevent such attacks.

---

## **Legal Disclaimer**  
This tool is developed for **educational purposes only** to raise awareness about wireless network vulnerabilities. **Unauthorized use is strictly prohibited** and may lead to legal consequences. Always obtain explicit permission before testing on any network.  

**The creators are not liable for any misuse or damages resulting from unauthorized application of this tool.**

---
