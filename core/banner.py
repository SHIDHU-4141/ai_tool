import socket

def grab_banner(target_ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2.0)
            s.connect((target_ip, port))
            if port in [80, 443, 8080]:
                s.sendall(b'HEAD / HTTP/1.1\r\nHost: ' + target_ip.encode() + b'\r\n\r\n')
            banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
            return banner if banner else 'No banner received'
    except Exception:
        return 'Connection failed or timeout'
