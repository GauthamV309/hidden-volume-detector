import os
from utils.timestamp import get_timestamp

def scan_ads(directory):
    print(f"[{get_timestamp()}] [*] Scanning for ADS in: {directory}")
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if ":" in file:
                    print(f"[{get_timestamp()}] [!] Possible ADS: {file}")
    except Exception as e:
        print(f"[{get_timestamp()}] [ERROR] {e}")