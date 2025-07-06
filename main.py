#!/usr/bin/env python3

import argparse
import os
from textwrap import dedent
from hidden_detector.disk_scanner import scan_disk_image
from hidden_detector.ads_scanner import scan_ads
from hidden_detector.stego_analyzer import analyze_image
from hidden_detector.entropy_mapper import entropy_map
from hidden_detector.signature_matcher import run_yara
from hidden_detector.utils.timestamp import get_timestamp

def print_manual():
    manual = """
NAME
    hidden-detector - Hidden Volume & Steganography Detection Tool

SYNOPSIS
    hidden-detector [OPTIONS]

DESCRIPTION
    Linux-based cybersecurity tool for detecting hidden volumes, stego files,
    NTFS ADS, encrypted containers, and known signatures.

OPTIONS
    --scan-disk IMAGE
        Scan a disk image for hidden data.

    --scan-ads DIR
        Scan NTFS path for Alternate Data Streams (Windows images only)

    --analyze-media FILE
        Analyze media file for steganographic data

    --entropy-map FILE
        Show entropy distribution of the file

    --signature-match FILE
        Scan file with YARA signatures

    --yara-rules FILE
        Specify YARA rules file (default: signature_db/yara_rules.yar)

    --manual
        Display this manual page
"""
    os.system('clear')
    os.system(f'echo "{manual.strip().replace(chr(34), chr(92)+chr(34))}" | less')

def main():
    parser = argparse.ArgumentParser(
        prog="hidden-detector",
        description=dedent("Linux forensics tool to detect stego, ADS, hidden containers"),
        epilog=dedent("Author: Gautham.V | Use --manual for full documentation"),
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("--scan-disk", metavar="IMAGE")
    parser.add_argument("--scan-ads", metavar="DIR")
    parser.add_argument("--analyze-media", metavar="FILE")
    parser.add_argument("--entropy-map", metavar="FILE")
    parser.add_argument("--signature-match", metavar="FILE")
    parser.add_argument("--yara-rules", metavar="FILE", default="signature_db/yara_rules.yar")
    parser.add_argument("--manual", action="store_true")

    args = parser.parse_args()

    if args.manual:
        print_manual()
        return

    print(f"[{get_timestamp()}] Starting Hidden Detector...\n")

    if args.scan_disk:
        scan_disk_image(args.scan_disk)
    if args.scan_ads:
        scan_ads(args.scan_ads)
    if args.analyze_media:
        analyze_image(args.analyze_media)
    if args.entropy_map:
        entropy_map(args.entropy_map)
    if args.signature_match:
        run_yara(args.signature_match, args.yara_rules)

    if not any(vars(args).values()):
        parser.print_help()

if __name__ == "__main__":
    main()