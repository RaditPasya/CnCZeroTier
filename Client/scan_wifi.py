import subprocess
import re


def get_self_ip():
    result = subprocess.run(
        ['ipconfig', '/all'], capture_output=True, text=True, check=True)
    output = result.stdout.split('\n')
    wifi_adapter_found = False
    ip_address = None
    for line in output:
        if line.strip().startswith("Wireless LAN adapter Wi-Fi"):
            wifi_adapter_found = True
        if wifi_adapter_found and line.strip().startswith("IPv4 Address"):
            # Use regex to extract the IP address
            match = re.search(r"IPv4 Address[^\:]*: ([\d\.]+)", line)
            if match:
                ip_address = match.group(1)
                break
    if ip_address:
        # print(f"Found IPv4 Address: {ip_address}")
        return ip_address
    else:
        print("IPv4 Address not found for Wireless LAN adapter Wi-Fi")
        return None


def scan_wifi():
    ip_address = get_self_ip()
    if ip_address:
        result = subprocess.run(
            ['arp', '-a'], capture_output=True, text=True, check=True)
        output = result.stdout.split('\n')

        interface_found = False
        dynamic_addresses = []

        for line in output:
            if line.strip().startswith(f"Interface: {ip_address}"):
                interface_found = True
            elif interface_found and line.strip().startswith("Interface:"):
                # Exit the loop if we encounter another interface section
                break
            elif interface_found:
                columns = line.split()
                if len(columns) == 3 and columns[2] == "dynamic":
                    dynamic_addresses.append(columns[1])

        # if dynamic_addresses:
        #     print(f"Dynamic physical addresses for interface {ip_address}:")
        #     for address in dynamic_addresses:
        #         print(address)
        # else:
        #     print(
        #         f"No dynamic physical addresses found for interface {ip_address}")
        return dynamic_addresses
    else:
        print("Could not determine the self IP address.")
        return []


scan_wifi()
