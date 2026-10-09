import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(target_ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.0)
            result = s.connect_ex((target_ip, port))
            if result == 0:
                return port
    except socket.error:
        pass
    return None

def run_port_scan(target_ip, ports=None, max_threads=50):
    if ports is None:
        ports = [21, 22, 80, 443, 8080, 3306]
        
    open_ports = []
    print(f"[*] Scanning target: {target_ip}...")
    
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = {executor.submit(scan_port, target_ip, port): port for port in ports}
        for future in futures:
            port = future.result()
            if port:
                open_ports.append(port)
                
    return sorted(open_ports)
