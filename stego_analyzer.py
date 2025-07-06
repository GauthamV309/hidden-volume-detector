import os
from utils.entropy import calculate_entropy
from utils.timestamp import get_timestamp

def analyze_image(image_path):
    print(f"[{get_timestamp()}] [*] Analyzing {image_path} for steganography")
    try:
        with open(image_path, 'rb') as f:
            data = f.read()
            entropy = calculate_entropy(data)
            if entropy > 7.8:
                print(f"[{get_timestamp()}] [!] High entropy: {entropy:.2f}")
    except Exception as e:
        print(f"[{get_timestamp()}] [ERROR] Failed to analyze image: {e}")