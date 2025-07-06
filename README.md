# ✅ `README.md`

````markdown
# 🔍 Hidden Volume & Steganography Detection Tool

A Linux-based cybersecurity and digital forensics tool that detects hidden data in disk images and media files using entropy analysis, steganalysis, alternate data stream inspection, and signature matching.

---

 📌 Features

- Hidden Volume Detection
  - Scans disk images (`.img`, `.dd`, `.bin`) for signs of TrueCrypt/VeraCrypt headers and high-entropy regions.
- Steganography Detection
  - Analyzes images, audio, and video for hidden content using statistical analysis and tool-specific markers.
- Alternate Data Streams (ADS)
  - Lists hidden streams in NTFS file systems (useful for investigating malware and hidden payloads).
- Entropy Mapping
  - Visualizes entropy to detect encrypted or compressed regions.
- YARA Signature Matching
  - Uses YARA to identify hidden files, encrypted volumes, or malware signatures.

---

 🖥️ Supported File Types

| Module               | Supported Formats                     |
|----------------------|----------------------------------------|
| Disk Scanner         | `.img`, `.dd`, `.bin`, raw block files |
| Stego Analyzer       | `.jpg`, `.png`, `.bmp`, `.mp3`, `.wav`, `.mp4`, `.avi` |
| ADS Scanner          | NTFS files only (`file:stream` format) |
| Entropy Analyzer     | Any binary file                        |

---

 ⚙️ Installation

# 1. Clone the repository

```bash
git clone https://github.com/GauthamV309/hidden-volume-detector
cd hidden-detector
````

# 2. Install dependencies

```bash
pip3 install -r requirements.txt
```

# 3. Make executable

```bash
chmod +x main.py
```

---

 🚀 Usage

Run with the appropriate flags:

```bash
./main.py [OPTIONS]
```

# 📖 View Manual Page

```bash
./main.py --manual
```

# 🔹 Common Commands

```bash
# Scan a disk image for hidden partitions and entropy spikes
./main.py --scan-disk suspect.img

# Analyze a file for steganographic data
./main.py --analyze-media secret.jpg

# Generate an entropy map
./main.py --entropy-map encrypted.avi

# Match file contents with YARA rules
./main.py --signature-match volume.dd --yara-rules custom_rules.yar

# Detect ADS (on NTFS image or mount)
./main.py --scan-ads /mnt/ntfs
```

---

 📂 Project Structure

```
hidden_detector/
├── main.py
├── disk_scanner.py
├── ads_scanner.py
├── stego_analyzer.py
├── entropy_mapper.py
├── signature_matcher.py
├── utils/
│   ├── entropy.py
│   └── timestamp.py
└── signature_db/
    └── yara_rules.yar
```

---

 📊 Sample Output

```bash
[2025-07-06 12:00:23] [*] Scanning disk image: suspect.img
[2025-07-06 12:00:24] [!] High entropy region found at offset 0x200000
[2025-07-06 12:00:24] [!] VeraCrypt signature match
```

```bash
[2025-07-06 12:03:11] [*] Analyzing image.jpg
[2025-07-06 12:03:12] [!] High entropy: 7.91
[2025-07-06 12:03:12] [!] steghide signature detected
```

---

 📦 Dependencies

* Python 3.7+
* `yara-python`
* `matplotlib`
* `Pillow`
* `scikit-image` (optional)
* `pytsk3` (optional for full disk parsing)
* `binwalk`, `steghide`, `foremost` (optional tools)

> Install system tools with:

```bash
sudo apt install steghide binwalk yara
```

---

 🛡️ Use Cases

* 🔍 **Digital Forensics**
* 🎯 **CTF & Red Teaming**
* 🧪 **Data Exfiltration Detection**
* 🧰 **Educational Security Research**

---

> Entropy Map (example)
>
> ![Entropy Graph](docs/entropy_map_sample.png)

> Stego Scan Output
>
> ![Stego Result](docs/stego_scan_output.png)

---

 📄 License

This project is licensed under the **MIT License**.
© 2025 Gautham.V

---

 🙋‍♂️ Author

**Gautham.V**
Cybersecurity & Forensics Enthusiast
📧 \[[vgautham2000@gmail.com](mailto:vgautham2000@gmail.com)]
🔗 [LinkedIn]([https://www.linkedin.com/in/gautham-v-7a903b249/](https://www.linkedin.com/in/gautham-v-7a903b249/))

---

📝Note
I am still in learning stages in cybersecurity, and there is a high chance that my code might not work as intended. However if you spot any scope for improvement or errors in my project, please don't hesitate to reach out to me. Hope this helps... Cheers.

 ⭐️ Contributions

Want to improve or extend the tool? Fork the repo and submit a pull request!

```

---

Would you like:
- A `requirements.txt` auto-generated from the current modules?
- Sample `yara_rules.yar` to include in `signature_db/`?
- Markdown badges (Python version, License, etc.)?

Let me know and I can include those too.
```
