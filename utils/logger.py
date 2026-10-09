import json
from datetime import datetime

def save_scan_results(target, open_ports_with_banners, filename='scan_report.json'):
    report = {
        'timestamp': datetime.utcnow().isoformat(),
        'target': target,
        'results': open_ports_with_banners
    }
    with open(filename, 'w') as f:
        json.dump(report, f, indent=4)
    print(f'[+] Report saved to {filename}')
