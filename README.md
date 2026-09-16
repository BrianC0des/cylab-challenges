# 🛡️ CyLab Challenges: Hack4Gov PH Regional & Collegiate CTF Storage

Centralized challenge bank and writeup repository for collegiate CTF training, national hackathons, and regional competition readiness (Hack4Gov PH, picoCTF, Google CTF, OverTheWire, and DEFCON style).

This repository serves as the remote raw API source for the **CyLab PH Warroom** simulation portal (`https://cylab-warroom.vercel.app`).

---

## 🎯 Repository Overview

- **Format:** Structured JSON format strictly compatible with CyLab Warroom, CTFd, and automated evaluation harnesses.
- **Total Challenges:** 60 curated challenges across all difficulty tiers:
  - 🟢 **Easy (19 challenges):** Foundational drills, syntax recognition, standard tooling (`cyberchef`, `wireshark`, `binwalk`, `strings`, `gtfobins`).
  - 🟡 **Medium (21 challenges):** Realistic collegiate regional problems (RSA modular arithmetic, USB HID parsing, DTMF audio, Blind SQLi, Command Injection, Ptrace anti-debugging, Ret2Win buffer overflows).
  - 🔴 **Hard (20 challenges):** Advanced exploitation (Hastad CRT, Bleichenbacher padding oracle, AES-GCM forbidden attack, Ext4 journal carving, TLS 1.3 decryption, Unicode zero-width stego, Prototype pollution, Python pickle deserialization, Angr symbolic execution, VM bytecode reversing, Ret2Libc ROP chains, Glibc 2.35 tcache poisoning).

---

## 📂 Category Breakdown (10 per Category)

1. 🔐 **Cryptography** (10 challenges)
   - Easy: Caesar/Affine, Vigenere, Base64/XOR
   - Medium: RSA small exponent, MD5 collisions, Linear Congruential PRNG, Hastad Broadcast CRT
   - Hard: AES-CBC Bit-flipping, Bleichenbacher PKCS#1 v1.5 padding oracle, AES-GCM GHASH forbidden attack
2. 🔍 **Forensics** (10 challenges)
   - Easy: Wireshark plaintext auth, PNG magic bytes header repair, Corrupted PDF
   - Medium: Memory dump LSASS triage, NTFS USN journal carving, USB HID keystroke extraction
   - Hard: DNS covert exfiltration, Audio spectrogram parsing, Ext4 journal undeleter, TLS 1.3 keylog + HTTP/2 reassembly
3. 🖼️ **Steganography** (10 challenges)
   - Easy: JPEG EOF trailing payload carving, Steghide passphrase extraction, EXIF GPS tags
   - Medium: LSB RGB color planes, PNG chunk injection, Audio phase shift, DTMF frequency dialing
   - Hard: ZIP polyglot archives, Unicode zero-width homoglyph encoding, CLUT palette index modulation
4. 🌐 **Web Exploitation** (10 challenges)
   - Easy: Robots.txt & directory traversal, Basic HTML/JS bypass, SQLi auth bypass *(interactive sandbox)*
   - Medium: Stored XSS cookie exfil *(interactive sandbox)*, IDOR document permits *(interactive sandbox)*, Command injection ping, CSRF
   - Hard: SSTI Jinja2 sandbox escape, SSRF AWS IAM metadata, Node.js prototype pollution, Python pickle deserialization RCE
5. ⚙️ **Reverse Engineering** (10 challenges)
   - Easy: Linux ELF strings triage, Decompiled Python `.pyc` bytecode, Basic assembly comparison
   - Medium: x86-64 password verifier, Stripped binary Ghidra analysis, PyInstaller archive extraction, Ptrace anti-debugging
   - Hard: WebAssembly table crackme, Angr symbolic execution keygen, Custom VM bytecode interpreter
6. 🧭 **Misc / OSINT / Pwn** (10 challenges)
   - Easy: Linux SUID privilege escalation (GTFOBins), Git reflog leak hunting, Base64 layered decoding
   - Medium: Philippine geolocation investigation, Docker registry token scrape, Discord OSINT recon, Stack buffer overflow (Ret2Win)
   - Hard: Matrix QR code repair, Ret2Libc ROP chain, Glibc 2.35 tcache poisoning heap exploit

---

## 📡 Live API Endpoints (Raw GitHub)

Direct CDN URLs for in-browser client fetching in CyLab Warroom:

- **Master Challenge Bank (All 60 Challenges):**
  \`https://raw.githubusercontent.com/BrianC0des/cylab-challenges/main/challenges.json\`

- **Category-Specific Feeds:**
  - Cryptography: \`https://raw.githubusercontent.com/BrianC0des/cylab-challenges/main/categories/cryptography.json\`
  - Forensics: \`https://raw.githubusercontent.com/BrianC0des/cylab-challenges/main/categories/forensics.json\`
  - Steganography: \`https://raw.githubusercontent.com/BrianC0des/cylab-challenges/main/categories/steganography.json\`
  - Web Exploitation: \`https://raw.githubusercontent.com/BrianC0des/cylab-challenges/main/categories/web-exploitation.json\`
  - Reverse Engineering: \`https://raw.githubusercontent.com/BrianC0des/cylab-challenges/main/categories/reverse-engineering.json\`
  - Misc / OSINT: \`https://raw.githubusercontent.com/BrianC0des/cylab-challenges/main/categories/misc-osint.json\`

---

## 📋 Schema Definition

\`\`\`typescript
interface Challenge {
  id: string;                      // e.g. "crypto-7"
  title: string;                   // Challenge title
  category: 'Cryptography' | 'Forensics' | 'Steganography' | 'Web Exploitation' | 'Reverse Engineering' | 'Misc/OSINT';
  points: number;                  // 100 to 500
  difficulty: 'Easy' | 'Medium' | 'Hard';
  source?: string;                 // e.g. "picoCTF style", "Google CTF", "Hack4Gov Regional"
  description: string;             // Detailed scenario and instructions
  hints: string[];                 // Progressive hints
  hintPenalties: number[];         // Score deductions (e.g. [-10, -25])
  flag: string;                    // Target flag e.g. "CYLAB{...}"
  concepts: string[];              // Key knowledge tags
  hasSandbox?: boolean;            // In-browser interactive sandbox support
  sandboxType?: 'sqli' | 'xss' | 'idor';
  writeup?: string;                // Complete step-by-step solution methodology
}
\`\`\`
