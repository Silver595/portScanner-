# Port Scanner

A simple Python script to perform port scanning on a given IP address. This script scans the specified IP address and identifies the open ports on the target device.

## Features

- Scans a target IP address for open ports.
- Displays a list of open ports.
- Customizable port range for scanning.
- Lightweight and easy to use.

## Requirements

- Python 3.x

### Python Libraries Used
- `socket`
- `sys` (optional, depending on error handling in the script)
- `ipaddress` (for IP validation, if applicable)

## How to Use

1. Clone the repository or download the script:
   ```bash
   git clone https://github.com/your-username/port-scanner.git
   cd port-scanner
   ```

2. Run the script:
   ```bash
   python port_scanner.py <target_ip> <start_port> <end_port>
   ```

   Replace:
   - `<target_ip>`: The IP address you want to scan.
   - `<start_port>`: The starting port of the range to scan.
   - `<end_port>`: The ending port of the range to scan.

   Example:
   ```bash
   python port_scanner.py 192.168.1.1 1 1000
   ```

## Output

The script outputs the list of open ports for the target IP address, for example:

```
Scanning IP: 192.168.1.1
Scanning ports 1 to 1000...
Open ports found:
- Port 22: Open
- Port 80: Open
- Port 443: Open
Scan completed.
```

## Limitations

- Scanning a wide range of ports may take time.
- The script requires proper permissions to run (use with administrative rights if needed).
- Ensure you have legal permission to scan the target IP address.

## Disclaimer

This tool is intended for educational purposes and authorized testing only. Use responsibly and ensure you have permission before scanning any network.

## License

This project is licensed under the [MIT License](LICENSE).

---

### Author

- **Your Name**
- [Your GitHub Profile](https://github.com/Silver595)
