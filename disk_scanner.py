import os
from utils.entropy import calculate_entropy

def scan_disk_image(img_path):
    print(f"[{get_timestamp()}] [*] Scanning disk image: {img_path}")
    try:
        with open(img_path, 'rb') as f:
            data = f.read(4096)
            if calculate_entropy(data) > 7.5:
                print(f"[{get_timestamp()}] [!] High entropy data found at start of image.")
    except Exception as e:
        print(f"[{get_timestamp()}] [ERROR] Failed to read image: {e}")