import sys
from core.scanner import run_port_scan
from core.banner import grab_banner
from core.analyzer import analyze_scan_with_ollama
from utils.logger import save_scan_results

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <target_ip>")
        sys.exit(1)
        
    target = sys.argv[1]
    print(f"[*] Starting NetPulse Scan on {target}...")
    
    # 1. Run port scan
    open_ports = run_port_scan(target)
    print(f"[+] Open ports found: {open_ports}")
    
    # 2. Grab banners
    results = {}
    for port in open_ports:
        print(f"[*] Grabbing banner for port {port}...")
        banner = grab_banner(target, port)
        results[port] = banner
        
    # 3. Save JSON report
    save_scan_results(target, results)
    
    # 4. Run Local AI Analysis via Ollama
    print("[*] Running local AI analysis...")
    analyze_scan_with_ollama()

if __name__ == "__main__":
    main()
