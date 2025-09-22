import nmap

# Initialize the scanner
scanner = nmap.PortScanner()

# Prompt user for IP address
target_ip = input("🔍 Enter the IP address to scan: ")

# Define scan arguments
scan_args = '-sS -sV -O -Pn'  # SYN scan, service version, OS detection, skip ping

print(f"\n📡 Scanning {target_ip} with arguments: {scan_args}\n")

try:
    scanner.scan(hosts=target_ip, arguments=scan_args)

    if target_ip in scanner.all_hosts():
        print(f"✅ Host {target_ip} is up\n")

        for proto in scanner[target_ip].all_protocols():
            ports = scanner[target_ip][proto].keys()
            for port in sorted(ports):
                state = scanner[target_ip][proto][port]['state']
                service = scanner[target_ip][proto][port]['name']
                product = scanner[target_ip][proto][port].get('product', '')
                version = scanner[target_ip][proto][port].get('version', '')
                print(f"  - Port {port}/{proto}: {state} | {service} {product} {version}")

        os_match = scanner[target_ip].get('osmatch', [])
        if os_match:
            print(f"\n🧠 OS Guess: {os_match[0]['name']} ({os_match[0]['accuracy']}% confidence)")
        else:
            print("\n❓ OS detection inconclusive.")
    else:
        print(f"❌ Host {target_ip} appears down or unreachable.")

except Exception as e:
    print(f"⚠️ Error during scan: {e}")
