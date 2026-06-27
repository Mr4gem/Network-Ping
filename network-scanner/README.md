# Network Scanner

Scans your local network, pings every device, and tries to identify what each one is by its hostname.

## Requirements

- Python 3.x (no extra packages needed — uses standard library only)
- Windows (uses `ping -n`)

## Usage

```bash
python scanner.py
```

By default scans `192.168.1.0/24`. To change the range, edit the bottom of `scanner.py`:

```python
ping_all_devices(ip_range='192.168.0.0/24')
```

## Example Output

```
Scanning 192.168.1.0/24...

192.168.1.1     Router/Gateway
192.168.1.5     Windows PC
192.168.1.10    iPhone
192.168.1.22    Unknown Device

4 device(s) found.
```

## Notes

- Scanning a full /24 network (254 hosts) takes a few minutes
- Run as Administrator for best results
- Some devices may not respond to ping even if online (firewall blocks ICMP)
