# NetPulse 🛡️

NetPulse is a modular network reconnaissance tool built in Python. It provides fast multi-threaded port scanning and service banner grabbing, outputting structured JSON reports designed for local LLM (Ollama) and cyber AI tool ingestion.

## Project Structure

\\\	ext
netpulse/
│
├── core/
│   ├── __init__.py
│   ├── scanner.py       # Fast multi-threaded port scanner
│   └── banner.py        # Service banner grabbing module
│
├── utils/
│   ├── __init__.py
│   └── logger.py        # Structured JSON report generator
│
├── main.py              # CLI entry point
└── requirements.txt     # Project dependencies
\\\

## Installation

1. Clone the repository:
   \\\ash
   git clone https://github.com/SHIDHU-4141/netpulse.git
   cd netpulse
   \\\

2. Install dependencies:
   \\\ash
   pip install -r requirements.txt
   \\\

## Usage

Run a scan against a target IP address (e.g., localhost):
\\\ash
python main.py 127.0.0.1
\\\

This will output an open port list, grab service banners, and generate a scan_report.json file ready for AI analysis.
