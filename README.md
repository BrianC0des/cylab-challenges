# 🛡️ CyLab Challenges: 100 Progressive CTF Challenges Bank

A complete 100-challenge progressive curriculum and competition training bank for collegiate CTF teams and cybersecurity squads (Hack4Gov PH, picoCTF, Google CTF, OverTheWire, and DEFCON style).

Live companion portal: [https://cylab-warroom.vercel.app](https://cylab-warroom.vercel.app)

---

## 🎯 Progressive Learning Architecture

The 100 challenges are structured into progressive mastery levels within each category:
- 🟢 **Level 1–3 (Foundations / Easy - 31 challenges):** Syntax understanding, fundamental cipher operations, CLI tools (`cyberchef`, `wireshark`, `binwalk`, `strings`, `gtfobins`, `wabt`, `ilspy`).
- 🟡 **Level 4–6 (Intermediate / Medium - 35 challenges):** Protocol forensics, cryptographic variants, interactive web sandboxes, memory carving, assembly flow tracing, binary analysis (`volatility`, `tshark`, `ghidra`, `sqlmap`, `pwntools`).
- 🔴 **Level 7–10 (Advanced Mastery / Hard - 34 challenges):** Cryptanalysis (Hastad CRT, Wiener's continued fractions, Bleichenbacher padding oracle, AES-GCM GHASH forbidden attack, Merkle-Hellman LLL lattice reduction), OS internals (Ext4 JBD2 journal carving, Linux LKM rootkit detection, eBPF bytecode reversing, Frida native JNI hooking, Glibc 2.35 tcache poisoning, Dirty Pipe CVE-2022-0847).

---

## 📊 Category Breakdown (100 Total)

| Category | Easy | Medium | Hard | Total |
| :--- | :---: | :---: | :---: | :---: |
| 🔐 **Cryptography** | 5 | 6 | 6 | **17** |
| 🔍 **Forensics** | 5 | 6 | 6 | **17** |
| 🖼️ **Steganography** | 5 | 6 | 5 | **16** |
| 🌐 **Web Exploitation** | 5 | 6 | 6 | **17** |
| ⚙️ **Reverse Engineering** | 5 | 6 | 6 | **17** |
| 🧭 **Misc / OSINT / Pwn** | 6 | 5 | 5 | **16** |
| **Total** | **31** | **35** | **34** | **100** |

---

## 🔄 Instant Flag Format Switching CLI

Easily switch the flag prefix across all 100 challenges, hints, descriptions, writeups, and categories in 1 second:

```bash
# Standard generic CTF format: flag{...}
python3 set_flag_format.py flag

# Team branded format: CYLAB{...}
python3 set_flag_format.py CYLAB

# Competition specific format: hack4gov{...}
python3 set_flag_format.py hack4gov
```

The script updates `challenges.json`, regenerates `categories/*.json`, and auto-syncs to `cylab-warroom`.

---

## 📡 Live Raw GitHub API Endpoints

- **Master Bank (All 100 Challenges):**
  `https://raw.githubusercontent.com/BrianC0des/cylab-challenges/main/challenges.json`
- **Category Feeds:**
  - Cryptography: `.../categories/cryptography.json`
  - Forensics: `.../categories/forensics.json`
  - Steganography: `.../categories/steganography.json`
  - Web Exploitation: `.../categories/web-exploitation.json`
  - Reverse Engineering: `.../categories/reverse-engineering.json`
  - Misc / OSINT: `.../categories/misc-osint.json`
