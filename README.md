# 🛡️ CyLab Challenges: Hack4Gov PH Regional CTF Storage

Centralized challenge bank and writeup repository for collegiate CTF training and regional competition readiness (Hack4Gov PH Regional & National benchmarks).

This repository serves as the remote raw API source for the **CyLab PH Warroom** simulation portal (`cylab-warroom`).

---

## 🎯 Repository Overview

- **Format:** Structured JSON format strictly compatible with CyLab Warroom, CTFd, and automated evaluation harnesses.
- **Total Challenges:** 36 curated, realistic challenges (6 per category).
- **Categories Covered:**
  - 🔐 **Cryptography** (6 challenges: Vigenere, RSA modular arithmetic, Base64/XOR streams, Hash collision, Custom PRNG, AES-CBC bit-flipping)
  - 🔍 **Forensics** (6 challenges: PCAP packet triage, Memory dump extraction, Corrupted PDF analysis, NTFS USN Journal carving, Exfiltration DNS covert channel, Audio spectral analysis)
  - 🖼️ **Steganography** (6 challenges: LSB RGB pixel extraction, PNG chunk injection, EXIF GPS metadata, Audio phase shift, Whitespace stego, ZIP concatenated polyglot)
  - 🌐 **Web Exploitation** (6 challenges: SQL injection auth bypass, Stored XSS cookie stealing, IDOR document permits, SSTI Jinja2 execution, SSRF AWS metadata retrieval, JWT none algorithm signature forgery)
  - ⚙️ **Reverse Engineering** (6 challenges: Linux ELF string triage, x86-64 assembly password check, Striped Ghidra keygen, PyInstaller decompilation, Anti-debugging ptrace bypass, WebAssembly crackme)
  - 🧭 **Misc / OSINT** (6 challenges: Philippine geolocation investigation, Git commit history leaks, Docker registry token extraction, Discord OSINT reconnaissance, Matrix QR code reconstruction, Linux privilege escalation)

---

## 📡 Live API Endpoints (Raw GitHub)

Direct CDN URLs for in-browser client fetching in CyLab Warroom:

- **Master Challenge Bank (All Categories):**
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

Each challenge adheres to this TypeScript interface:

\`\`\`typescript
interface Challenge {
  id: string;                      // e.g. "crypto-1"
  title: string;                   // Display title
  category: 'Cryptography' | 'Forensics' | 'Steganography' | 'Web Exploitation' | 'Reverse Engineering' | 'Misc/OSINT';
  points: number;                  // 100 to 500
  difficulty: 'Easy' | 'Medium' | 'Hard';
  description: string;             // Detailed scenario, briefing, and instructions
  hints: string[];                 // Progressive hints
  hintPenalties: number[];         // Score deductions (e.g. [-10, -25])
  flag: string;                    // Target flag e.g. "flag{...}" or "CYLAB{...}"
  concepts: string[];              // Knowledge Vault links e.g. ["RSA", "Wireshark"]
  hasSandbox?: boolean;            // In-browser interactive sandbox support
  sandboxType?: 'sqli' | 'xss' | 'idor';
  writeup?: string;                // Complete solution methodology (unlocked in Free Mode or Debrief)
}
\`\`\`

---

## 🔄 Syncing with CyLab Warroom

In **CyLab Warroom**:
1. Click **Import / Export** on the top navigation bar.
2. Enter the raw URL \`https://raw.githubusercontent.com/BrianC0des/cylab-challenges/main/challenges.json\`.
3. Click **Fetch & Load Bank**. The entire squad's challenge board updates instantly!
