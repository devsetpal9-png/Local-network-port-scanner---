# Local-network-port-scanner---
🚀 Cybersecurity internship project focused on local network reconnaissance. Uses Nmap for TCP/UDP scanning, Wireshark for packet analysis, and Python for automation. Includes findings, risk matrix, and ethical documentation.

# 🔍 Local Network Port Scanning – Internship Task 1

## 🎯 Objective
Discover open ports on devices in a local network to understand service exposure and potential risks.

## 🛠️ Tools Used
- Nmap
- Wireshark 
- Python (for automation)

## 📡 Methodology
1. Identified local IP range.
2. Performed TCP SYN, OPEN PORT and OS DETECTION scan.
3. Analyzed scan results and services.
4. Captured packets with Wireshark.
5. Documented risks and recommendations.

## 🔐 Ethical Disclaimer
This scan was conducted on a private network for educational purposes only. Unauthorized scanning of networks is unethical and may be illegal.

## 📊 Findings

| IP Address      | Open Ports       | OS Guess                     | Risk Level | Notes |
|-----------------|------------------|------------------------------|------------|-------|
| 192.168.231.103 | 135/tcp, 445/tcp | Windows Server 2012 / XP / 7 | High       | SMB (445) is vulnerable to exploits like EternalBlue. RPC (135) may allow remote code execution. |
| 192.168.231.133 | 53/tcp           | Linux 2.6.x                  | Medium     | VMware remote management port. Should be restricted and patched. |
| 192.168.231.254 | Host unreachable | —                            | Unknown    | May be blocking ICMP probes. Consider scanning with `-Pn`. |

## 🗒️ Notes
- The scan revealed open ports on multiple hosts within the local network.
- Host `192.168.231.254` appeared down or may be blocking ICMP probes; consider using `-Pn` to bypass ping checks.
- The Windows host exposes **SMB (port 445)**, which is commonly targeted by exploits such as **EternalBlue**. This service should be restricted or patched if not required.
- The Linux host running VMware (`port 902`) may be used for remote management; ensure access is limited and the service is up to date.
- OS detection was performed using the `-O` flag, revealing potential operating systems and network distances.
- All scans were conducted ethically within a controlled lab environment for educational purposes.

## 🤖 Automation
Included a Python script to automate Nmap scans and parse results.

## 📚 Interview Prep
See `interview-questions.md` for answers to common cybersecurity questions related to port scanning.
