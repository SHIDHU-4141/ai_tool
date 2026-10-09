import json
import urllib.request
import urllib.error

def analyze_scan_with_ollama(report_filename="scan_report.json", model="llama3"):
    try:
        with open(report_filename, "r") as f:
            report_data = json.load(f)
    except FileNotFoundError:
        print(f"[-] Error: {report_filename} not found. Run a scan first.")
        return

    prompt = (
        f"You are a cybersecurity expert AI. Analyze the following network port scan report "
        f"and identify potential security risks, open port implications, and recommended hardening steps:\n\n"
        f"{json.dumps(report_data, indent=2)}"
    )

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    req = urllib.request.Request(
        "http://localhost:11434/api/generate",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )

    print(f"[*] Sending scan report to local Ollama ({model})... Please wait...")

    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))
            analysis = result.get("response", "No response received from model.")
            print("\n--- AI Security Analysis ---")
            print(analysis)
            
            with open("ai_analysis_report.txt", "w") as out:
                out.write(analysis)
            print("\n[+] Analysis saved to ai_analysis_report.txt")
            
    except urllib.error.URLError as e:
        print(f"[-] Failed to connect to Ollama: {e.reason}. Ensure 'ollama serve' is running.")
