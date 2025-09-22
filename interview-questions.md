1. What is an open port?
An open port is a network port that actively accepts incoming connections. It indicates a service is running and reachable, which can be exploited if misconfigured or vulnerable.

2. How does Nmap perform a TCP SYN scan?
Nmap sends a SYN packet to the target port. If it receives a SYN-ACK response, the port is open. It then sends an RST to avoid completing the handshake—making it stealthy and fast.

3. What risks are associated with open ports?
Open ports expose services that may have vulnerabilities. Attackers can exploit these to gain unauthorized access, perform denial-of-service attacks, or escalate privileges.

4. Explain the difference between TCP and UDP scanning.
- TCP scan: Actively connects to ports and confirms their state.
- UDP scan: Sends datagrams and infers port status based on ICMP responses. Slower and less reliable due to lack of handshake.

5. How can open ports be secured?
- Close unused ports
- Use firewalls to restrict access
- Apply patches to services
- Implement intrusion detection systems (IDS)

6. What is a firewall's role regarding ports?
Firewalls monitor and control incoming/outgoing traffic. They block or allow traffic based on rules, helping prevent unauthorized access to open ports.

7. What is a port scan and why do attackers perform it?
A port scan probes a system to discover open ports and services. Attackers use it for reconnaissance to identify potential entry points before launching an attack.

8. How does Wireshark complement port scanning?
Wireshark captures and analyzes network packets. It helps verify scan behavior, detect anomalies, and understand how services respond to probes—useful for validating Nmap results.


