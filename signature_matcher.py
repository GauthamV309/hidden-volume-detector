import yara
from utils.timestamp import get_timestamp

def run_yara(file_path, rule_path):
    print(f"[{get_timestamp()}] [*] Running YARA on: {file_path}")
    try:
        rules = yara.compile(filepath=rule_path)
        matches = rules.match(file_path)
        for match in matches:
            print(f"[{get_timestamp()}] [!] Signature match: {match.rule}")
    except Exception as e:
        print(f"[{get_timestamp()}] [ERROR] YARA scanning failed: {e}")