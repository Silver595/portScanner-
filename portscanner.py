import socket
import termcolor  # type: ignore

def scan(target, ports):
    print('\n' + termcolor.colored(f'Starting scan for {target}', 'cyan'))
    open_ports = 0
    for port in ports:
        if scan_port(target, port):
            open_ports += 1

    if open_ports == 0:
        print(termcolor.colored(f'[-] All {len(ports)} ports scanned are closed.', 'red', 'on_grey', ['bold']))
    else:
        print(termcolor.colored(f'[*] Scan complete. Total open ports: {open_ports}', 'blue', 'on_grey', ['bold']))

def scan_port(ip_address, port):
    try:
        sk = socket.socket()
        sk.settimeout(0.5)
        sk.connect((ip_address, port))
        print(termcolor.colored(f'[+] Open Port {port}', 'green'))
        sk.close()
        return True
    except:
        return False

targets = input('[*] Enter target(s) for scan (separate with commas ,): ')
ports_input = input('[*] Enter port(s) for scan (example: 80 or 20-80): ')

if '-' in ports_input:
    start_port, end_port = map(int, ports_input.split('-'))
    ports = range(start_port, end_port + 1)
else:
    ports = range(1, int(ports_input) + 1)

if ',' in targets:
    print(termcolor.colored('[*] Scanning multiple targets', 'yellow'))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(), ports)
else:
    scan(targets, ports)

