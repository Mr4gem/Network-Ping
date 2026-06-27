import subprocess
import ipaddress
import socket

DEVICE_HINTS = {
    'desktop': 'Windows PC',
    'laptop': 'Laptop',
    'iphone': 'iPhone',
    'ipad': 'iPad',
    'android': 'Android Phone',
    'samsung': 'Samsung Device',
    'pixel': 'Google Phone',
    'macbook': 'MacBook',
    'imac': 'iMac',
    'xbox': 'Xbox',
    'playstation': 'PlayStation',
    'ps4': 'PlayStation 4',
    'ps5': 'PlayStation 5',
    'switch': 'Nintendo Switch',
    'echo': 'Amazon Echo',
    'fire': 'Amazon Fire',
    'roku': 'Roku',
    'chromecast': 'Chromecast',
    'nest': 'Google Nest',
    'ring': 'Ring Device',
    'printer': 'Printer',
    'router': 'Router',
    'gateway': 'Router/Gateway',
}

def get_hostname(ip):
    try:
        return socket.gethostbyaddr(str(ip))[0]
    except:
        return None

def guess_device(hostname):
    if not hostname:
        return 'Unknown Device'
    lower = hostname.lower()
    for keyword, label in DEVICE_HINTS.items():
        if keyword in lower:
            return label
    return f'Unknown ({hostname})'

def ping_all_devices(ip_range='192.168.1.0/24', count=1):
    print("Scanning network...\n")
    found = []
    for ip in ipaddress.ip_network(ip_range, strict=False).hosts():
        r = subprocess.run(['ping', '-n', str(count), str(ip)],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if r.returncode == 0:
            hostname = get_hostname(ip)
            device = guess_device(hostname)
            print(f"{str(ip):<16} {device}")
            found.append(ip)
    print(f"\n{len(found)} device(s) found.")

if __name__ == "__main__":
    ping_all_devices()
