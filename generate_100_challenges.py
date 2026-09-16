import json

with open('challenges.json', 'r') as f:
    challenges = json.load(f)

existing_ids = {c['id'] for c in challenges}

additions = [
    # --- CRYPTOGRAPHY (7 new -> 17 total) ---
    {
        "id": "crypto-11",
        "title": "Rail Fence Transposition (Level 1)",
        "category": "Cryptography",
        "points": 100,
        "difficulty": "Easy",
        "description": "The cipher message bounces in a zigzag rail fence across 3 rails: 'f{aesLvvR3lgCarI_edon_ieOT}as_D_Lg_1'. Reconstruct the rails and read the original message.",
        "hints": [
            {"text": "A 3-rail fence alternates down then up: row 0, 1, 2, 1, 0, 1, 2...", "penalty": 10},
            {"text": "CyberChef has a 'Rail Fence Cipher Decode' recipe. Set Rails to 3.", "penalty": 20}
        ],
        "flag": "flag{rail_f3nc3_z1gz4g_unf0ld3d}",
        "concept": "Transposition Ciphers, Rail Fence, Geometric Permutation",
        "cheatsheet": "python3 -c \"import sys; # use CyberChef Rail Fence Decode\"",
        "badge": "Rail Master",
        "writeup": "1. Put the ciphertext into CyberChef.\n2. Add 'Rail Fence Cipher Decode' recipe with Rails = 3, Offset = 0.\n3. The decrypted message appears directly.\n4. Flag: `flag{rail_f3nc3_z1gz4g_unf0ld3d}`"
    },
    {
        "id": "crypto-12",
        "title": "Polybius Square & Tap Code (Level 2)",
        "category": "Cryptography",
        "points": 100,
        "difficulty": "Easy",
        "description": "Prisoner transmission using tap code pairs: '41 34 31 54 12 24 45 43'. Decrypt the 5x5 Polybius grid where C and K share coordinates (1,3).",
        "hints": [
            {"text": "Each letter is represented by two numbers: Row and Column (1 to 5).", "penalty": 10},
            {"text": "Row 1: A B C/K D E, Row 2: F G H I J, Row 3: L M N O P, Row 4: Q R S T U, Row 5: V W X Y Z.", "penalty": 20}
        ],
        "flag": "flag{p0lyb1us_t4p_c0d3_d3c0d3d}",
        "concept": "Polybius Square, Coordinate Ciphers, Tap Code",
        "cheatsheet": "CyberChef -> 'Polybius Square Decode'",
        "badge": "Grid Decoder",
        "writeup": "1. Convert coordinate pairs using the 5x5 Polybius grid.\n2. Coordinates map out the plaintext characters.\n3. Flag: `flag{p0lyb1us_t4p_c0d3_d3c0d3d}`"
    },
    {
        "id": "crypto-13",
        "title": "Beaufort Cipher Reciprocal Variant (Level 4)",
        "category": "Cryptography",
        "points": 200,
        "difficulty": "Medium",
        "description": "An Italian maritime cipher uses the Beaufort formula: $C = (K - P) \\pmod{26}$. Key is 'NAVAL'. Decrypt the ciphertext stream.",
        "hints": [
            {"text": "Unlike standard Vigenere ($C = P + K$), Beaufort subtracts plaintext from key: $P = (K - C) \\pmod{26}$.", "penalty": 15},
            {"text": "Notice that encrypting and decrypting are identical reciprocal operations in Beaufort.", "penalty": 25}
        ],
        "flag": "flag{b34uf0rt_r3c1pr0c4l_v1g3n3r3}",
        "concept": "Beaufort Cipher, Polyalphabetic Substitution, Key Modulo",
        "cheatsheet": "CyberChef -> 'Vigenère Decode' with variant Beaufort",
        "badge": "Naval Cryptor",
        "writeup": "1. In CyberChef, add 'Beaufort Cipher Decode' with key 'NAVAL'.\n2. The reciprocal subtraction reveals the plaintext and flag.\n3. Flag: `flag{b34uf0rt_r3c1pr0c4l_v1g3n3r3}`"
    },
    {
        "id": "crypto-14",
        "title": "Solitaire Deck Keystream (Level 5)",
        "category": "Cryptography",
        "points": 250,
        "difficulty": "Medium",
        "description": "Bruce Schneier's Solitaire cipher generates keystream numbers from a 54-card deck with two jokers (A and B). Shift jokers, perform triple cut and count cut, and generate the first 16 keystream bytes.",
        "hints": [
            {"text": "Step 1: Move Joker A down 1 card. Step 2: Move Joker B down 2 cards.", "penalty": 15},
            {"text": "Step 3: Triple cut around jokers. Step 4: Count cut based on bottom card. Output card value = keystream byte.", "penalty": 25}
        ],
        "flag": "flag{s0l1t41r3_c4rd_d3ck_k3ystr34m}",
        "concept": "Solitaire Cipher, Pseudo-Random Generation, Manual Cryptography",
        "cheatsheet": "python3 -c \"import solitaire; print(...)\"",
        "badge": "Card Shark",
        "writeup": "1. Implement Schneier's deck permutation algorithm in Python.\n2. Generate keystream integers $K_i$ and subtract from ciphertext letters modulo 26.\n3. Flag: `flag{s0l1t41r3_c4rd_d3ck_k3ystr34m}`"
    },
    {
        "id": "crypto-15",
        "title": "Wiener's Continued Fraction Attack (Level 7)",
        "category": "Cryptography",
        "points": 400,
        "difficulty": "Hard",
        "description": "An RSA key was generated with a small private exponent $d < \\frac{1}{3} N^{1/4}$ to speed up cryptographic signatures. Recover the private key $d$ using the continued fraction expansion of $e/N$.",
        "hints": [
            {"text": "Wiener proved that if $d < \\frac{1}{3} N^{1/4}$, then $\\frac{k}{d}$ is one of the convergents of the continued fraction of $\\frac{e}{N}$.", "penalty": 20},
            {"text": "Compute convergents $k_i/d_i$. For each, compute $\\phi = (e d_i - 1)/k_i$ and test if roots of $x^2 - (N - \\phi + 1)x + N = 0$ are integers.", "penalty": 40}
        ],
        "flag": "flag{w13n3r_c0nt1nu3d_fr4ct10n_d_sm4ll}",
        "concept": "RSA Cryptanalysis, Wiener Attack, Continued Fractions, SageMath",
        "cheatsheet": "python3 -m owiener -e <e> -n <n>",
        "badge": "Wiener Cracker",
        "writeup": "1. Install `owiener` (`pip install owiener`).\n2. Run `d = owiener.attack(e, N)`.\n3. Decrypt ciphertext: `m = pow(c, d, N)` and convert to ASCII.\n4. Flag: `flag{w13n3r_c0nt1nu3d_fr4ct10n_d_sm4ll}`"
    },
    {
        "id": "crypto-16",
        "title": "Franklin-Reiter Related Message Attack (Level 8)",
        "category": "Cryptography",
        "points": 450,
        "difficulty": "Hard",
        "description": "Two messages $m_1$ and $m_2$ differ by a known linear affine relation $m_2 = a \\cdot m_1 + b \\pmod N$. Both were encrypted with RSA exponent $e = 3$ under the same public modulus $N$. Recover $m_1$ by taking the greatest common divisor of polynomial ideals in SageMath.",
        "hints": [
            {"text": "Let $P_1(x) = x^e - c_1$ and $P_2(x) = (a x + b)^e - c_2$. Both polynomials have $m_1$ as a common root modulo $N$.", "penalty": 20},
            {"text": "The greatest common divisor $\\gcd(P_1, P_2) = x - m_1 \\pmod N$.", "penalty": 40}
        ],
        "flag": "flag{fr4nkl1n_r31t3r_p0lyn0m14l_gcd}",
        "concept": "RSA Polynomial Rings, Franklin-Reiter, GCD in Z/NZ, SageMath",
        "cheatsheet": "sage -c 'P.<x> = PolynomialRing(Zmod(N)); ...'",
        "badge": "Ring Theorist",
        "writeup": "1. In SageMath: define polynomial ring over integers modulo $N$.\n2. Compute monic polynomial GCD of $x^3 - c_1$ and $(a x + b)^3 - c_2$.\n3. The linear remainder gives $-m_1$, revealing the message.\n4. Flag: `flag{fr4nkl1n_r31t3r_p0lyn0m14l_gcd}`"
    },
    {
        "id": "crypto-17",
        "title": "Merkle-Hellman Knapsack LLL Reduction (Level 9)",
        "category": "Cryptography",
        "points": 500,
        "difficulty": "Hard",
        "description": "The Merkle-Hellman knapsack cryptosystem generates a public key sequence $B_i$. The ciphertext is the subset sum $S = \\sum m_i B_i$. Break the low-density subset sum problem using the Lenstra-Lenstra-Lovasz (LLL) lattice basis reduction algorithm.",
        "hints": [
            {"text": "Construct the $(n+1) \\times (n+1)$ lattice matrix with public weights $B_i$ on the top row and $1/2$ on the diagonal.", "penalty": 25},
            {"text": "Run LLL lattice reduction. The shortest vector in the reduced basis contains the binary vector $m_i \\in \\{0, 1\\}$.", "penalty": 50}
        ],
        "flag": "flag{m3rkl3_h3llm4n_lll_l4tt1c3_r3duc3d}",
        "concept": "Lattice Cryptanalysis, Merkle-Hellman Knapsack, LLL Algorithm, Shortest Vector Problem",
        "cheatsheet": "sage -c 'M = Matrix(...); M.LLL()'",
        "badge": "Lattice Architect",
        "writeup": "1. Build the basis matrix in SageMath.\n2. Apply `.LLL()` to find the shortest lattice vector.\n3. Check coordinates for $\\pm 1/2$ or $0/1$ assignments to reconstruct $m$.\n4. Flag: `flag{m3rkl3_h3llm4n_lll_l4tt1c3_r3duc3d}`"
    },

    # --- FORENSICS (7 new -> 17 total) ---
    {
        "id": "forensics-11",
        "title": "Bash History & Logout Forensics (Level 1)",
        "category": "Forensics",
        "points": 100,
        "difficulty": "Easy",
        "description": "An attacker compromised a user account and executed cleanup scripts. However, they forgot about `.bash_logout` and unlinked history buffers. Triage the home directory dotfiles to extract commands executed right before exit.",
        "hints": [
            {"text": "Check `cat ~/.bash_history`, `cat ~/.bash_logout`, and look for hidden files with `ls -la`.", "penalty": 10},
            {"text": "Look for base64 encoded strings in command line exports.", "penalty": 20}
        ],
        "flag": "flag{b4sh_h1st0ry_d0tf1l3s_4ud1t}",
        "concept": "Linux Artifacts, Bash History, Dotfiles, Command Audit",
        "cheatsheet": "cat ~/.bash_history | grep -E 'export|flag|key'",
        "badge": "Shell Auditor",
        "writeup": "1. Inspect `.bash_history` and `.bash_logout`.\n2. Recover uncommitted export string: `export SECRET_TOKEN=flag{b4sh_h1st0ry_d0tf1l3s_4ud1t}`.\n3. Flag: `flag{b4sh_h1st0ry_d0tf1l3s_4ud1t}`"
    },
    {
        "id": "forensics-12",
        "title": "Chromium SQLite History & Cookies (Level 2)",
        "category": "Forensics",
        "points": 100,
        "difficulty": "Easy",
        "description": "Extracted a suspect's Google Chrome profile folder `Default/`. Query the SQLite database `History` and `Cookies` to uncover visited darknet URL parameters and session tokens.",
        "hints": [
            {"text": "Chrome stores browsing history in an SQLite 3 database located at `Default/History`.", "penalty": 10},
            {"text": "Run `sqlite3 History 'SELECT url, title FROM urls;'`.", "penalty": 20}
        ],
        "flag": "flag{chr0m1um_sql1t3_h1st0ry_3xtr4ct}",
        "concept": "Browser Forensics, SQLite Database, Chromium Artifacts",
        "cheatsheet": "sqlite3 History \"SELECT url FROM urls WHERE url LIKE '%flag%';\"",
        "badge": "Web Tracker",
        "writeup": "1. Open `History` in `sqlite3` or DB Browser for SQLite.\n2. Query URLs table: `SELECT url FROM urls WHERE url LIKE '%flag%';`.\n3. URL contains parameter `?token=flag{chr0m1um_sql1t3_h1st0ry_3xtr4ct}`.\n4. Flag: `flag{chr0m1um_sql1t3_h1st0ry_3xtr4ct}`"
    },
    {
        "id": "forensics-13",
        "title": "Windows EVTX PowerShell Auditing (Level 4)",
        "category": "Forensics",
        "points": 200,
        "difficulty": "Medium",
        "description": "A Windows Server 2022 domain controller logged a malicious PowerShell script execution. Parse `Microsoft-Windows-PowerShell%4Operational.evtx` for Event ID 4104 (Script Block Logging) to assemble the attacker's deobfuscated payload.",
        "hints": [
            {"text": "Event ID 4104 records complete script blocks even if obfuscated with backticks or base64.", "penalty": 15},
            {"text": "Use `python-evtx` or `Chainsaw` or `Hayabusa` to parse the `.evtx` file.", "penalty": 25}
        ],
        "flag": "flag{3vtx_p0w3rsh3ll_scr1ptbl0ck_4104}",
        "concept": "Windows Event Logs, EVTX Forensics, Script Block Logging, Event ID 4104",
        "cheatsheet": "chainsaw hunt -s evtx_dir/ --mapping rules.yml",
        "badge": "Log Hunter",
        "writeup": "1. Extract Event ID 4104 script block text using `python-evtx`.\n2. Reconstruct chunks from the multi-stage logging.\n3. The script block reveals: `$flag = 'flag{3vtx_p0w3rsh3ll_scr1ptbl0ck_4104}'`.\n4. Flag: `flag{3vtx_p0w3rsh3ll_scr1ptbl0ck_4104}`"
    },
    {
        "id": "forensics-14",
        "title": "Master Boot Record (MBR) Repair (Level 5)",
        "category": "Forensics",
        "points": 250,
        "difficulty": "Medium",
        "description": "A disk image `drive.raw` fails to mount because sector 0 (MBR) was zeroed out by wiper malware. However, the volume boot record (VBR) at sector 2048 remains intact. Rebuild the 16-byte partition table entry in the MBR and mount the partition.",
        "hints": [
            {"text": "An MBR partition table starts at byte offset 446 (0x1BE) with 16 bytes per entry, ending with boot signature `55 AA`.", "penalty": 15},
            {"text": "Inspect sector 2048 using hexedit to verify the NTFS/FAT32 signature, then point LBA start to 2048.", "penalty": 25}
        ],
        "flag": "flag{mbr_p4rt1t10n_t4bl3_r3c0v3r3d}",
        "concept": "MBR Partition Table, Sector 0 Forensics, VBR Reconstruction, Hex Editing",
        "cheatsheet": "testdisk /dev/loop0 OR xxd drive.raw | head -n 35",
        "badge": "Disk Surgeon",
        "writeup": "1. Run `testdisk` or manually edit sector 0 with `hexedit`.\n2. Set byte 446: Bootable flag (0x80), Partition type (0x07 for NTFS), Start LBA (2048 = `00 08 00 00` little endian).\n3. Mount loop device: `losetup -P /dev/loop0 drive.raw`.\n4. Read `flag.txt` from mounted partition.\n5. Flag: `flag{mbr_p4rt1t10n_t4bl3_r3c0v3r3d}`"
    },
    {
        "id": "forensics-15",
        "title": "Offline Registry SAM & SYSTEM Hive Secrets (Level 6)",
        "category": "Forensics",
        "points": 300,
        "difficulty": "Medium",
        "description": "Recovered raw Windows registry hives `SAM` and `SYSTEM` from an unallocated volume snapshot. Extract the local Administrator NTLM hash and decrypt cached secrets using `impacket-secretsdump`.",
        "hints": [
            {"text": "The `SYSTEM` hive contains the syskey used to decrypt the password hashes stored in `SAM`.", "penalty": 15},
            {"text": "Run: `impacket-secretsdump -sam SAM -system SYSTEM LOCAL`.", "penalty": 30}
        ],
        "flag": "flag{s4m_syst3m_h1v3_s3cr3tsdmp_pwn}",
        "concept": "Windows Registry, SAM Database, SysKey, Impacket Secretsdump",
        "cheatsheet": "impacket-secretsdump -sam SAM -system SYSTEM LOCAL",
        "badge": "Hive Harvester",
        "writeup": "1. Execute `impacket-secretsdump -sam SAM -system SYSTEM LOCAL`.\n2. Observe extracted user accounts.\n3. The Administrator password description field contains the flag.\n4. Flag: `flag{s4m_syst3m_h1v3_s3cr3tsdmp_pwn}`"
    },
    {
        "id": "forensics-16",
        "title": "Shimcache & Amcache Execution Timeline (Level 7)",
        "category": "Forensics",
        "points": 400,
        "difficulty": "Hard",
        "description": "Malware executed from a USB flash drive and self-deleted immediately. Prove execution presence and obtain the SHA-1 hash of the deleted binary by parsing `Amcache.hve` and `SYSTEM\\CurrentControlSet\\Control\\Session Manager\\AppCompatCache` (Shimcache).",
        "hints": [
            {"text": "Shimcache stores executable path and last modified timestamp of executed binaries.", "penalty": 20},
            {"text": "Use Eric Zimmerman's `AppCompatCacheParser.exe` or python `ShimCacheParser.py`.", "penalty": 40}
        ],
        "flag": "flag{sh1mc4ch3_4mc4ch3_3x3cut10n_pr0v3d}",
        "concept": "Shimcache Forensics, Amcache.hve, Program Execution Artifacts, Timeline Analysis",
        "cheatsheet": "python3 ShimCacheParser.py -i SYSTEM -o out.csv",
        "badge": "Cache Investigator",
        "writeup": "1. Run `ShimCacheParser.py -i SYSTEM -o output.csv`.\n2. Search CSV for executables running from removable drives (`E:\\malware.exe`).\n3. Correlate with `Amcache.hve` to verify SHA-1 hash and flag string.\n4. Flag: `flag{sh1mc4ch3_4mc4ch3_3x3cut10n_pr0v3d}`"
    },
    {
        "id": "forensics-17",
        "title": "Linux Kernel Core Dump & LKM Rootkit (Level 9)",
        "category": "Forensics",
        "points": 500,
        "difficulty": "Hard",
        "description": "A mission-critical Debian server experienced a kernel panic. A vmcore crash dump was preserved. Using Volatility 3 or GDB against the vmlinux debug symbol table, detect a hidden Loadable Kernel Module (LKM) that hooked the sys_call_table to hide processes.",
        "hints": [
            {"text": "In Volatility 3, use the `linux.check_modules` and `linux.check_syscall` plugins.", "penalty": 25},
            {"text": "Look for hijacked syscall table entries pointing to addresses outside the kernel `.text` range.", "penalty": 50}
        ],
        "flag": "flag{lkm_r00tk1t_hook3d_sysc4ll_t4bl3}",
        "concept": "Kernel Crash Dump, Volatility 3 Linux, LKM Rootkits, Syscall Hooking",
        "cheatsheet": "vol -f vmcore linux.check_syscall.Check_syscall",
        "badge": "Kernel Detective",
        "writeup": "1. Run `vol -f vmcore linux.check_syscall`.\n2. Entry `sys_kill` (syscall 62) points to anomalous unlinked module address.\n3. Disassemble the hook function to find the authorization token.\n4. Flag: `flag{lkm_r00tk1t_hook3d_sysc4ll_t4bl3}`"
    },

    # --- STEGANOGRAPHY (6 new -> 16 total) ---
    {
        "id": "stego-11",
        "title": "Audio Stereo Phase Inversion (Level 1)",
        "category": "Steganography",
        "points": 100,
        "difficulty": "Easy",
        "description": "An MP3 audio track `track.mp3` sounds like noisy ambient static. However, the left and right stereo channels contain inverted identical waveforms with a hidden center channel secret. Invert one channel and sum to mono to cancel out the background music.",
        "hints": [
            {"text": "Phase cancellation: $A + (-A) = 0$. When identical signals are 180 degrees out of phase, they completely cancel.", "penalty": 10},
            {"text": "Open Audacity -> Split Stereo Track -> Select one channel -> Effect -> Invert -> Mix and Render to Mono.", "penalty": 20}
        ],
        "flag": "flag{aud10_ph4s3_1nv3rs10n_c4nc3l}",
        "concept": "Audio Phase Inversion, Audacity, Channel Subtraction, Stereo Forensics",
        "cheatsheet": "ffmpeg -i track.mp3 -af 'pan=mono|c0=0.5*c0-0.5*c1' out.wav",
        "badge": "Acoustic Filter",
        "writeup": "1. Load `track.mp3` into Audacity.\n2. Invert Channel R and merge with Channel L to mono.\n3. The static cancels out completely, revealing clear spoken voice speaking the flag.\n4. Flag: `flag{aud10_ph4s3_1nv3rs10n_c4nc3l}`"
    },
    {
        "id": "stego-12",
        "title": "BMP Scanline Row Padding Stego (Level 2)",
        "category": "Steganography",
        "points": 100,
        "difficulty": "Easy",
        "description": "A 24-bit BMP image has an unaligned width (e.g., 201 pixels). In the BMP format, every scanline row must be padded to a multiple of 4 bytes. An attacker hid secret characters inside these trailing padding bytes.",
        "hints": [
            {"text": "Each row in a 24-bit BMP takes $3 \\times \\text{width}$ bytes. Extra bytes are added until divisible by 4.", "penalty": 10},
            {"text": "Write a Python script to seek past image data and read only the padding bytes at the end of each scanline.", "penalty": 20}
        ],
        "flag": "flag{bmp_p4dd1ng_byt3s_unp4ck3d}",
        "concept": "BMP Image Format, Scanline Padding, Pixel Array Alignment",
        "cheatsheet": "python3 -c \"# extract row padding bytes\"",
        "badge": "Pixel Aligner",
        "writeup": "1. Parse BMP header: get width, height, and data offset.\n2. Calculate row padding: `pad = (4 - (width * 3) % 4) % 4`.\n3. Read the `pad` bytes after every scanline to extract the hidden string.\n4. Flag: `flag{bmp_p4dd1ng_byt3s_unp4ck3d}`"
    },
    {
        "id": "stego-13",
        "title": "PDF Invisible FlateDecode Annotation (Level 4)",
        "category": "Steganography",
        "points": 200,
        "difficulty": "Medium",
        "description": "A PDF memo appears completely blank on page 2. Inspect PDF object streams for hidden annotations with transparency masks and uncompressed `/FlateDecode` streams.",
        "hints": [
            {"text": "Use `pdf-parser.py` or `qpdf --qdf --object-streams=disable memo.pdf memo_raw.pdf`.", "penalty": 15},
            {"text": "Search for `/Annot` objects or text rendered with color identical to background (`1 1 1 rg`).", "penalty": 25}
        ],
        "flag": "flag{pdf_fl4t3_str34m_4nn0t4t10n}",
        "concept": "PDF Object Streams, FlateDecode, qpdf, Didier Stevens PDF Tools",
        "cheatsheet": "qpdf --qdf memo.pdf decompressed.pdf && grep -a flag decompressed.pdf",
        "badge": "PDF Inspector",
        "writeup": "1. Decompress PDF streams: `qpdf --qdf --object-streams=disable memo.pdf raw.pdf`.\n2. Grep raw text: `grep -i 'flag{' raw.pdf`.\n3. Flag: `flag{pdf_fl4t3_str34m_4nn0t4t10n}`"
    },
    {
        "id": "stego-14",
        "title": "Tar Archive Slack Space Injection (Level 5)",
        "category": "Steganography",
        "points": 250,
        "difficulty": "Medium",
        "description": "A standard POSIX tar archive stores files in 512-byte blocks. If a file is 100 bytes, the remaining 412 bytes in the block are normally zeroed. Carve non-zero payload hidden inside the slack blocks of `archive.tar`.",
        "hints": [
            {"text": "Tar headers and file contents are always aligned to 512-byte block boundaries.", "penalty": 15},
            {"text": "Iterate through tar blocks. When a file block ends, check if the remaining bytes before the next header contain data.", "penalty": 25}
        ],
        "flag": "flag{t4r_bl0ck_sl4ck_sp4c3_c4rv3d}",
        "concept": "Tar Block Structure, Slack Space Steganography, Byte Alignment",
        "cheatsheet": "xxd archive.tar | grep -v '0000 0000'",
        "badge": "Slack Hunter",
        "writeup": "1. Parse tar headers and calculate file sizes.\n2. Read bytes between `offset + filesize` and `ceil(filesize / 512) * 512`.\n3. The non-zero slack bytes assemble into the flag.\n4. Flag: `flag{t4r_bl0ck_sl4ck_sp4c3_c4rv3d}`"
    },
    {
        "id": "stego-15",
        "title": "Video Keyframe I-Frame Steganography (Level 7)",
        "category": "Steganography",
        "points": 400,
        "difficulty": "Hard",
        "description": "An MP4 video file contains secret data encoded across the GOP (Group of Pictures) keyframe intervals. Extract intra-coded frames (I-frames) using FFmpeg and inspect quantization tables.",
        "hints": [
            {"text": "Extract only I-frames with: `ffmpeg -i video.mp4 -vf 'select=eq(pict_type\\,I)' -vsync vfr iframe_%03d.png`.", "penalty": 20},
            {"text": "Compare pixel variance across sequential I-frames.", "penalty": 40}
        ],
        "flag": "flag{mp4_1fr4m3_g0p_qu4nt1z4t10n}",
        "concept": "Video Codecs, I-Frame Extraction, GOP Structure, FFmpeg",
        "cheatsheet": "ffprobe -show_frames -select_streams v video.mp4 | grep pict_type",
        "badge": "Video Frame Crafter",
        "writeup": "1. Dump I-frames with FFmpeg.\n2. Diff first and second I-frame in Python to isolate injected pixels.\n3. Flag: `flag{mp4_1fr4m3_g0p_qu4nt1z4t10n}`"
    },
    {
        "id": "stego-16",
        "title": "Spread Spectrum Frequency Hopping (Level 8)",
        "category": "Steganography",
        "points": 450,
        "difficulty": "Hard",
        "description": "A high-fidelity FLAC audio recording hides a carrier signal using Direct Sequence Spread Spectrum (DSSS). The pseudorandom chipping code is generated by a 16-bit LFSR. Correlate the signal against the PN sequence to recover the hidden data.",
        "hints": [
            {"text": "DSSS hides signals beneath the acoustic noise floor by spreading energy across a wide frequency band.", "penalty": 20},
            {"text": "Cross-correlate the audio spectrum against candidate PN sequences to produce sharp despreading peaks.", "penalty": 40}
        ],
        "flag": "flag{dsss_spr34d_sp3ctrum_d3spr34d}",
        "concept": "DSSS Audio Stego, LFSR Chipping Sequences, Cross-Correlation, SciPy",
        "cheatsheet": "python3 -c \"import scipy.signal; ...\"",
        "badge": "Signal Specialist",
        "writeup": "1. Load audio in Python using `scipy.io.wavfile`.\n2. Generate LFSR chipping sequence and multiply with windowed FFT bins.\n3. Peak correlation indices decode the bitstream.\n4. Flag: `flag{dsss_spr34d_sp3ctrum_d3spr34d}`"
    },

    # --- WEB EXPLOITATION (7 new -> 17 total) ---
    {
        "id": "web-11",
        "title": "JWT None Algorithm Signature Bypass (Level 1)",
        "category": "Web Exploitation",
        "points": 100,
        "difficulty": "Easy",
        "description": "The target dashboard authenticates users via JSON Web Tokens (JWT). The backend JWT verification library permits the `alg: none` header. Modify the token payload to set `{\"role\": \"admin\"}` and remove the signature to bypass authentication.",
        "hints": [
            {"text": "A JWT consists of Header.Payload.Signature. Change `alg: HS256` to `alg: none` in the base64-encoded header.", "penalty": 10},
            {"text": "Keep the trailing dot after the payload: `header.payload.` (empty signature).", "penalty": 20}
        ],
        "flag": "flag{jwt_n0n3_4lg0r1thm_byp4ss}",
        "concept": "JSON Web Tokens, Alg None Vulnerability, Authentication Bypass",
        "cheatsheet": "jwt_tool <token> -X a",
        "badge": "Token Forger",
        "writeup": "1. Decode JWT header: change `{\"alg\":\"HS256\"}` to `{\"alg\":\"none\"}`.\n2. Decode JWT payload: change `\"role\":\"user\"` to `\"role\":\"admin\"`.\n3. Base64url encode both and append trailing dot: `eyJhbGciOiJub25lIn0.ey...`.\n4. Submit as Cookie to `/dashboard` to capture flag.\n5. Flag: `flag{jwt_n0n3_4lg0r1thm_byp4ss}`"
    },
    {
        "id": "web-12",
        "title": "CORS Misconfiguration & Origin Reflection (Level 2)",
        "category": "Web Exploitation",
        "points": 100,
        "difficulty": "Easy",
        "description": "An internal banking API `/api/account/secret` naively reflects any incoming `Origin` header with `Access-Control-Allow-Credentials: true`. Craft an exploit HTML page that exfiltrates user private keys via cross-origin fetch.",
        "hints": [
            {"text": "Check headers: `curl -H 'Origin: https://evil.com' https://target/api/account/secret -I`.", "penalty": 10},
            {"text": "If `Access-Control-Allow-Origin: https://evil.com` and `Access-Control-Allow-Credentials: true` are returned, any website can steal authenticated data.", "penalty": 20}
        ],
        "flag": "flag{c0rs_cr3d3nt14ls_0r1g1n_l34k}",
        "concept": "CORS Misconfiguration, Credentialed Cross-Origin Requests, Web Security",
        "cheatsheet": "curl -H 'Origin: https://attacker.com' -I https://target/api",
        "badge": "Origin Breaker",
        "writeup": "1. Verify reflected CORS origin and credentials headers.\n2. Deploy exploit page with `fetch('/api/account/secret', {credentials: 'include'})`.\n3. Exfiltrate JSON response containing the flag.\n4. Flag: `flag{c0rs_cr3d3nt14ls_0r1g1n_l34k}`"
    },
    {
        "id": "web-13",
        "title": "XML External Entity (XXE) Injection (Level 4)",
        "category": "Web Exploitation",
        "points": 200,
        "difficulty": "Medium",
        "description": "An enterprise invoice processing service parses XML uploads without disabling external DTD entities. Inject a custom `SYSTEM` entity declaration to read `/etc/passwd` and `/app/flag.txt` from the server filesystem.",
        "hints": [
            {"text": "Add DTD declaration before root element: `<!DOCTYPE foo [ <!ENTITY xxe SYSTEM 'file:///app/flag.txt'> ]>`.", "penalty": 15},
            {"text": "Reference the entity in an output field: `<name>&xxe;</name>`.", "penalty": 25}
        ],
        "flag": "flag{xx3_3xt3rn4l_3nt1ty_f1l3_r34d}",
        "concept": "XXE Injection, XML DTD, Local File Inclusion, OWASP Top 10",
        "cheatsheet": "curl -d '<!DOCTYPE r [<!ENTITY x SYSTEM \"file:///flag.txt\">]><r>&x;</r>' target",
        "badge": "XML Sapper",
        "writeup": "1. Intercept XML upload request in Burp Suite.\n2. Inject entity: `<!DOCTYPE x [ <!ENTITY leak SYSTEM \"file:///app/flag.txt\"> ]>`.\n3. Insert `&leak;` into XML body.\n4. Response reflects file content.\n5. Flag: `flag{xx3_3xt3rn4l_3nt1ty_f1l3_r34d}`"
    },
    {
        "id": "web-14",
        "title": "Cross-Site Request Forgery (CSRF) Profile State (Level 5)",
        "category": "Web Exploitation",
        "points": 250,
        "difficulty": "Medium",
        "description": "The user email update form at `/profile/update-email` lacks CSRF tokens and uses `SameSite=None` session cookies. Craft an automatic self-submitting HTML exploit form to change the admin's recovery email to an attacker address.",
        "hints": [
            {"text": "Write an HTML document with `<form action='...' method='POST'>` and `<script>document.forms[0].submit()</script>`.", "penalty": 15},
            {"text": "Test if the endpoint accepts URL-encoded POST requests without custom headers.", "penalty": 25}
        ],
        "flag": "flag{csrf_p0st_f0rm_3m41l_t4k30v3r}",
        "concept": "Cross-Site Request Forgery, SameSite Cookies, Account Takeover",
        "cheatsheet": "Burp Suite -> Engagement Tools -> Generate CSRF PoC",
        "badge": "State Forger",
        "writeup": "1. Generate CSRF form targeting `/profile/update-email` with `email=attacker@evil.com`.\n2. Deliver URL to victim administrator.\n3. Trigger password reset to claim administrator session and flag.\n4. Flag: `flag{csrf_p0st_f0rm_3m41l_t4k30v3r}`"
    },
    {
        "id": "web-15",
        "title": "GraphQL Introspection & Batch Query Leak (Level 6)",
        "category": "Web Exploitation",
        "points": 300,
        "difficulty": "Medium",
        "description": "A modern React frontend queries a GraphQL endpoint `/graphql`. The introspection query is enabled in production. Query the `__schema` to discover unpublished administrative mutations and query batching endpoints to extract the flag.",
        "hints": [
            {"text": "Send POST payload with `{\"query\": \"{ __schema { types { name fields { name } } } }\"}`.", "penalty": 15},
            {"text": "Look for fields like `adminFlag` or mutations like `generateAuditReport`.", "penalty": 30}
        ],
        "flag": "flag{gr4phql_1ntr0sp3ct10n_sch3m4_l34k}",
        "concept": "GraphQL Forensics, Introspection Query, Batch Attacks, API Security",
        "cheatsheet": "npx graphql-voyager OR inql query https://target/graphql",
        "badge": "Schema Cartographer",
        "writeup": "1. Run GraphQL introspection query via curl.\n2. Discover hidden query `systemFlag(secretKey: String)`.\n3. Execute query to retrieve the flag.\n4. Flag: `flag{gr4phql_1ntr0sp3ct10n_sch3m4_l34k}`"
    },
    {
        "id": "web-16",
        "title": "SSRF via DNS Rebinding IP Filter Bypass (Level 8)",
        "category": "Web Exploitation",
        "points": 450,
        "difficulty": "Hard",
        "description": "An image caching proxy checks IP addresses against private ranges (`127.0.0.1`, `10.0.0.0/8`, `169.254.169.254`). However, the URL validation resolves DNS first, and then makes a separate HTTP request. Use DNS rebinding with TTL=0 to bypass the IP whitelist and read cloud instance metadata.",
        "hints": [
            {"text": "DNS Rebinding: First DNS resolution returns a legitimate public IP (passes filter). Second DNS resolution returns `127.0.0.1`.", "penalty": 20},
            {"text": "Use a public rebinding tool like `rbndr.us` (e.g. `7f000001.34d4a4b4.rbndr.us`).", "penalty": 40}
        ],
        "flag": "flag{dns_r3b1nd1ng_ssrf_m3t4d4t4_pwn}",
        "concept": "DNS Rebinding, SSRF Bypass, Time-of-Check to Time-of-Use (TOCTOU), Cloud Metadata",
        "cheatsheet": "curl 'https://target/fetch?url=http://7f000001.c0a80101.rbndr.us/meta'",
        "badge": "DNS Conjurer",
        "writeup": "1. Configure rebinding domain to toggle between public IP and `169.254.169.254`.\n2. Submit URL to proxy.\n3. Verification succeeds against public IP, while fetch retrieves AWS metadata token.\n4. Flag: `flag{dns_r3b1nd1ng_ssrf_m3t4d4t4_pwn}`"
    },
    {
        "id": "web-17",
        "title": "Java Deserialization via CommonsCollections (Level 9)",
        "category": "Web Exploitation",
        "points": 500,
        "difficulty": "Hard",
        "description": "A Spring Boot legacy microservice accepts serialized Java objects via HTTP header `X-Java-Serialized-Object` (`\\xac\\xed\\x00\\x05`). Exploit the Apache Commons Collections 3.1 `InvokerTransformer` gadget chain using `ysoserial` to achieve Remote Code Execution.",
        "hints": [
            {"text": "Java serialized streams always start with magic bytes `AC ED 00 05` (base64 `rO0AB`).", "penalty": 25},
            {"text": "Generate gadget with `java -jar ysoserial.jar CommonsCollections5 'cat /flag.txt' | base64`.", "penalty": 50}
        ],
        "flag": "flag{j4v4_d3s3r14l1z4t10n_ys0s3r14l_rc3}",
        "concept": "Java Deserialization, ysoserial, CommonsCollections Gadgets, Remote Code Execution",
        "cheatsheet": "java -jar ysoserial.jar CommonsCollections6 'touch /tmp/pwn' | base64",
        "badge": "Java Puppeteer",
        "writeup": "1. Generate ysoserial payload with `CommonsCollections5`.\n2. Deliver via `X-Java-Serialized-Object` header.\n3. Server deserializes object, executing arbitrary commands and writing flag to output.\n4. Flag: `flag{j4v4_d3s3r14l1z4t10n_ys0s3r14l_rc3}`"
    },

    # --- REVERSE ENGINEERING (7 new -> 17 total) ---
    {
        "id": "rev-11",
        "title": "WebAssembly Text Decompilation (Level 1)",
        "category": "Reverse Engineering",
        "points": 100,
        "difficulty": "Easy",
        "description": "A client-side verification function is compiled to WebAssembly (`check.wasm`). Convert the `.wasm` binary module into WebAssembly Text format (`.wat`) using WABT tools and inspect the memory string validation logic.",
        "hints": [
            {"text": "Install WABT (WebAssembly Binary Toolkit) and run `wasm2wat check.wasm -o check.wat`.", "penalty": 10},
            {"text": "Search the `.wat` file for `(data ...)` blocks containing ASCII byte constants.", "penalty": 20}
        ],
        "flag": "flag{w4sm_w4sm2w4t_byt3c0d3_r34d}",
        "concept": "WebAssembly, WABT wasm2wat, WAT Disassembly, Memory Blocks",
        "cheatsheet": "wasm2wat check.wasm | grep -C 5 data",
        "badge": "Wasm Dissector",
        "writeup": "1. Run `wasm2wat check.wasm -o check.wat`.\n2. Locate the memory section: `(data (i32.const 1024) \"flag{w4sm_w4sm2w4t_byt3c0d3_r34d}\")`.\n3. Flag: `flag{w4sm_w4sm2w4t_byt3c0d3_r34d}`"
    },
    {
        "id": "rev-12",
        "title": ".NET C# Managed Binary Decompilation (Level 2)",
        "category": "Reverse Engineering",
        "points": 100,
        "difficulty": "Easy",
        "description": "Recovered a Windows GUI password manager `Vault.exe` compiled in C# .NET. Open the assembly in ILSpy, dnSpy, or AvaloniaILSpy to decompile CIL (Common Intermediate Language) back into clean C# source code.",
        "hints": [
            {"text": ".NET binaries contain rich metadata with full method names, types, and variable structures.", "penalty": 10},
            {"text": "Search for class `KeyManager` or method `VerifyMasterKey`.", "penalty": 20}
        ],
        "flag": "flag{d0tn3t_csh4rp_1lspy_d3c0mp1l3}",
        "concept": ".NET Decompilation, CIL Bytecode, ILSpy, dnSpy",
        "cheatsheet": "ilspycmd Vault.exe -p > decompiled.cs",
        "badge": "C# Revealer",
        "writeup": "1. Run `ilspycmd Vault.exe > source.cs`.\n2. Open `source.cs` and inspect `VerifyMasterKey` method.\n3. The hardcoded flag string is compared directly with user input.\n4. Flag: `flag{d0tn3t_csh4rp_1lspy_d3c0mp1l3}`"
    },
    {
        "id": "rev-13",
        "title": "Go Binary Stripped Symbol Recovery (Level 4)",
        "category": "Reverse Engineering",
        "points": 200,
        "difficulty": "Medium",
        "description": "Target is a statically linked, stripped 64-bit Linux binary compiled in Go (`go build -ldflags='-s -w'`). Recover function names and type definitions by parsing the Go `pclntab` (PC Line Table) structure.",
        "hints": [
            {"text": "Go runtime embeds function metadata in `runtime.pclntab` even when stripped.", "penalty": 15},
            {"text": "Use the Ghidra script `GoHelper` or IDA plugin `GoReSym` to restore all symbols automatically.", "penalty": 25}
        ],
        "flag": "flag{g0l4ng_pclnt4b_symb0ls_r3st0r3d}",
        "concept": "Go Reversing, pclntab Structure, GoReSym, Static Binaries",
        "cheatsheet": "GoReSym -t -p ./target_go_bin",
        "badge": "Gopher Reverser",
        "writeup": "1. Run `GoReSym ./target_go_bin > symbols.json`.\n2. Reconstruct `main.checkLicense` function in Ghidra.\n3. Follow the byte comparison loop to extract the flag.\n4. Flag: `flag{g0l4ng_pclnt4b_symb0ls_r3st0r3d}`"
    },
    {
        "id": "rev-14",
        "title": "Rust Binary Demangling & Enum Matching (Level 5)",
        "category": "Reverse Engineering",
        "points": 250,
        "difficulty": "Medium",
        "description": "An authentic Rust CLI executable processes user input through `Option<T>` and `Result<T, E>` monads. Demangle the symbol names (`rustfilt`) and reverse the iterator fold operation to reveal the target string.",
        "hints": [
            {"text": "Demangle Rust symbols with: `nm ./rust_bin | rustfilt`.", "penalty": 15},
            {"text": "Rust iterators (`.bytes().map().fold()`) compile to efficient unrolled assembly loops in Ghidra.", "penalty": 25}
        ],
        "flag": "flag{rust_d3m4ngl3_1t3r4t0r_r3v}",
        "concept": "Rust Reversing, Symbol Demangling, rustfilt, Iterators Assembly",
        "cheatsheet": "nm -C ./rust_app | grep 'crate_name'",
        "badge": "Rust Crab",
        "writeup": "1. Demangle binary symbols using `rustfilt`.\n2. Locate `my_app::validate_flag` in Ghidra.\n3. Reverse the XOR mapping and bitwise rotation.\n4. Flag: `flag{rust_d3m4ngl3_1t3r4t0r_r3v}`"
    },
    {
        "id": "rev-15",
        "title": "Windows PE Import Address Table Hooking (Level 7)",
        "category": "Reverse Engineering",
        "points": 400,
        "difficulty": "Hard",
        "description": "A protected Windows x64 executable dynamically unpacks its payload into memory and hooks its own Import Address Table (IAT) to redirect API calls to custom stubs. Dump the unmapped memory region and rebuild the IAT using Scylla.",
        "hints": [
            {"text": "Set hardware breakpoint on execution (`hrx`) at the original entry point (OEP).", "penalty": 20},
            {"text": "Use x64dbg + Scylla plugin to dump process memory and fix PE imports.", "penalty": 40}
        ],
        "flag": "flag{14t_h00k1ng_scyll4_03p_dump3d}",
        "concept": "PE Format, IAT Hooking, OEP Unpacking, x64dbg Scylla",
        "cheatsheet": "x64dbg -> Plugins -> Scylla -> Dump -> Fix Dump",
        "badge": "PE Unpacker",
        "writeup": "1. Trace execution in x64dbg until reaching the long jump to the OEP.\n2. Launch Scylla: click 'IAT Autosearch' and 'Get Imports'.\n3. Dump process to disk and fix PE headers.\n4. Open unpacked executable in Ghidra to view plain validation logic.\n5. Flag: `flag{14t_h00k1ng_scyll4_03p_dump3d}`"
    },
    {
        "id": "rev-16",
        "title": "Android Native JNI Function Hooking with Frida (Level 8)",
        "category": "Reverse Engineering",
        "points": 450,
        "difficulty": "Hard",
        "description": "An Android financial app delegates flag verification to a native shared library `libnative-lib.so` via JNI function `Java_ph_gov_cylab_Check_verifyFlag()`. Write a Frida JavaScript hook to intercept arguments and return values at runtime.",
        "hints": [
            {"text": "Use `Module.findExportByName('libnative-lib.so', 'Java_ph_gov_cylab_Check_verifyFlag')`.", "penalty": 20},
            {"text": "Attach with: `frida -U -f ph.gov.cylab -l hook.js --no-pause`.", "penalty": 40}
        ],
        "flag": "flag{fr1d4_jn1_n4t1v3_h00k_succ3ss}",
        "concept": "Android JNI, Frida Dynamic Instrumentation, Native Hooking, Shared Objects",
        "cheatsheet": "frida -U -n ph.gov.cylab -l hook.js",
        "badge": "Frida Enchanter",
        "writeup": "1. Write Frida hook script intercepting `verifyFlag`.\n2. Log the raw C string pointers from `args[2]`.\n3. Enter random text in the app; Frida console prints expected flag string.\n4. Flag: `flag{fr1d4_jn1_n4t1v3_h00k_succ3ss}`"
    },
    {
        "id": "rev-17",
        "title": "Linux Kernel eBPF Bytecode Reversing (Level 9)",
        "category": "Reverse Engineering",
        "points": 500,
        "difficulty": "Hard",
        "description": "A Linux endpoint monitoring agent drops an eBPF program into the kernel via `bpf(BPF_PROG_LOAD)` to inspect raw network sockets. Extract the 64-bit eBPF instructions from the binary and reverse the filter state machine to construct the bypass packet.",
        "hints": [
            {"text": "eBPF uses 64-bit registers (r0-r10) and 8-byte instruction format: `opcode, dst:4, src:4, off:16, imm:32`.", "penalty": 25},
            {"text": "Disassemble with `llvm-objdump -d` or Python `bpf-disasm`.", "penalty": 50}
        ],
        "flag": "flag{3bpf_byt3c0d3_k3rn3l_f1lt3r_r3v}",
        "concept": "eBPF Bytecode, Linux Kernel Tracing, LLVM eBPF Disassembler, Socket Filters",
        "cheatsheet": "bpftool prog dump xlated id <prog_id>",
        "badge": "eBPF Whisperer",
        "writeup": "1. Dump raw eBPF bytecode section.\n2. Disassemble instructions: identify packet header offset checks.\n3. The eBPF filter requires a magic TCP sequence and specific payload bytes.\n4. Flag: `flag{3bpf_byt3c0d3_k3rn3l_f1lt3r_r3v}`"
    },

    # --- MISC / OSINT / PWN (6 new -> 16 total) ---
    {
        "id": "misc-11",
        "title": "Zip Slip Path Traversal Exploitation (Level 1)",
        "category": "Misc/OSINT",
        "points": 100,
        "difficulty": "Easy",
        "description": "An automated homework grading server extracts student ZIP submissions without validating canonical file paths. Craft a malicious ZIP containing directory traversal sequences (`../../../../root/.ssh/authorized_keys`) to overwrite server files.",
        "hints": [
            {"text": "Zip file headers allow relative paths containing `../`.", "penalty": 10},
            {"text": "Use python `zipfile` with custom `ZipInfo` where filename is `../../../../tmp/flag.txt`.", "penalty": 20}
        ],
        "flag": "flag{z1p_sl1p_p4th_tr4v3rs4l_wr1t3}",
        "concept": "Zip Slip, Arbitrary File Overwrite, Archive Security, Path Traversal",
        "cheatsheet": "python3 -c \"import zipfile; # craft zip with ../../ path\"",
        "badge": "Archive Infiltrator",
        "writeup": "1. Craft ZIP with filename `../../var/www/html/shell.php`.\n2. Submit ZIP to extraction endpoint.\n3. Access `shell.php` to execute commands and read flag.\n4. Flag: `flag{z1p_sl1p_p4th_tr4v3rs4l_wr1t3}`"
    },
    {
        "id": "misc-12",
        "title": "Wi-Fi WPA2 PMKID Hashcat Cracking (Level 2)",
        "category": "Misc/OSINT",
        "points": 100,
        "difficulty": "Easy",
        "description": "Captured a Wi-Fi WPA2 PMKID from a wireless access point beacon without needing a full 4-way client handshake. Extract the PMKID hash line and crack it against rockyou.txt using Hashcat mode 22000.",
        "hints": [
            {"text": "Convert PCAP to Hashcat format using `hcxpcapngtool -o hash.22000 capture.pcapng`.", "penalty": 10},
            {"text": "Run `hashcat -m 22000 hash.22000 rockyou.txt`.", "penalty": 20}
        ],
        "flag": "flag{wpa2_pmk1d_h4shc4t_cr4ck3d}",
        "concept": "Wireless Security, WPA2 PMKID, Hashcat 22000, hcxtools",
        "cheatsheet": "hashcat -m 22000 wifi.hc22000 /usr/share/wordlists/rockyou.txt",
        "badge": "Wi-Fi Cracker",
        "writeup": "1. Extract PMKID using `hcxpcapngtool`.\n2. Run Hashcat mode 22000 against dictionary.\n3. Recovered password is the flag.\n4. Flag: `flag{wpa2_pmk1d_h4shc4t_cr4ck3d}`"
    },
    {
        "id": "misc-13",
        "title": "Flight ADS-B Transponder Route OSINT (Level 4)",
        "category": "Misc/OSINT",
        "points": 200,
        "difficulty": "Medium",
        "description": "An adversary fled the country on a private charter flight. Given an intercepted ADS-B transponder squawk code `7700` and ICAO 24-bit hex address `4B1234`, reconstruct the aircraft's flight path, departure runway, and arrival waypoint using FlightRadar24 and ADS-B Exchange archives.",
        "hints": [
            {"text": "ICAO 24-bit addresses uniquely identify airframes worldwide.", "penalty": 15},
            {"text": "Search ADS-B Exchange historical tracker for the hex identifier on September 15, 2026.", "penalty": 25}
        ],
        "flag": "flag{4dsb_fl1ght_tr4ck1ng_1c40_0s1nt}",
        "concept": "Aviation OSINT, ADS-B Transponders, FlightRadar24, ICAO Identifiers",
        "cheatsheet": "curl -s 'https://globe.adsbexchange.com/?icao=...'",
        "badge": "Sky Tracker",
        "writeup": "1. Look up ICAO hex address in ADS-B Exchange historical database.\n2. Trace radar breadcrumb logs to destination airport (Zamboanga International Airport / RPMZ).\n3. Flag: `flag{4dsb_fl1ght_tr4ck1ng_1c40_0s1nt}`"
    },
    {
        "id": "misc-14",
        "title": "Suncalc Shadow & Geolocation Calculation (Level 5)",
        "category": "Misc/OSINT",
        "points": 250,
        "difficulty": "Medium",
        "description": "A covert photo shows a flagpole casting a shadow that is exactly 1.42 times its physical height at bearing 48 degrees northeast. Using Suncalc, calculate the solar altitude angle and determine the exact date and minute the photo was captured.",
        "hints": [
            {"text": "Shadow length formula: $\\tan(\\theta) = \\frac{\\text{height}}{\\text{shadow}} = \\frac{1}{1.42} \\implies \\theta \\approx 35.1^\\circ$.", "penalty": 15},
            {"text": "Cross-reference solar azimuth and altitude for the latitude coordinates in Suncalc.org.", "penalty": 25}
        ],
        "flag": "flag{sunc4lc_sh4d0w_t1m3_g30l0c4t10n}",
        "concept": "Shadow Analysis, Suncalc, Ephemeris Geolocation, Chronolocation",
        "cheatsheet": "python3 -c \"import suncalc; # calculate solar azimuth & altitude\"",
        "badge": "Solar Cartographer",
        "writeup": "1. Compute solar elevation angle: $\\arctan(1 / 1.42) = 35.1^\\circ$.\n2. In Suncalc: find time when sun was at $35.1^\\circ$ altitude and opposite bearing (228 degrees azimuth).\n3. Reconstructed timestamp matches target flag format.\n4. Flag: `flag{sunc4lc_sh4d0w_t1m3_g30l0c4t10n}`"
    },
    {
        "id": "misc-15",
        "title": "Format String Memory Arbitrary Write (%n) (Level 8)",
        "category": "Misc/OSINT",
        "points": 450,
        "difficulty": "Hard",
        "description": "A 64-bit networked daemon prints user greetings via `printf(user_input)`. The binary has partial RELRO and no PIE. Leverage the `%n` format specifier to overwrite a Global Offset Table (GOT) entry with the address of `system()`.",
        "hints": [
            {"text": "`%n` writes the number of bytes printed so far into a pointer provided on the stack.", "penalty": 20},
            {"text": "Use pwntools `fmtstr_payload(offset, {got_puts: sym_system})` to generate the write payload.", "penalty": 40}
        ],
        "flag": "flag{fmtstr_4rb1tr4ry_wr1t3_g0t_pwn}",
        "concept": "Format String Exploitation, Arbitrary Memory Write (%n), GOT Overwriting, pwntools",
        "cheatsheet": "python3 -c \"from pwn import *; print(fmtstr_payload(6, {0x404018: 0x401150}))\"",
        "badge": "Format Smasher",
        "writeup": "1. Determine argument stack offset using `%p.%p.%p...`.\n2. Write exploit using pwntools `fmtstr_payload` targeting `puts@GOT`.\n3. Send payload; next call to `puts` spawns interactive shell.\n4. Flag: `flag{fmtstr_4rb1tr4ry_wr1t3_g0t_pwn}`"
    },
    {
        "id": "misc-16",
        "title": "Linux Dirty Pipe Kernel Privilege Escalation (Level 9)",
        "category": "Misc/OSINT",
        "points": 500,
        "difficulty": "Hard",
        "description": "Target Linux kernel version is 5.16.10, vulnerable to CVE-2022-0847 (Dirty Pipe). Exploit the uninitialized pipe buffer flags (`PIPE_BUF_FLAG_CAN_MERGE`) to overwrite read-only page cache pages, injecting a root password hash into `/etc/passwd`.",
        "hints": [
            {"text": "Dirty Pipe allows overwriting cached file data in the page cache without write permissions.", "penalty": 25},
            {"text": "Splice file data into a pipe, then write attacker bytes into the pipe to overwrite page cache.", "penalty": 50}
        ],
        "flag": "flag{d1rty_p1p3_cv3_2022_0847_r00t}",
        "concept": "Kernel Exploitation, CVE-2022-0847, Dirty Pipe, Page Cache Corruption",
        "cheatsheet": "gcc dirtypipe.c -o dirtypipe && ./dirtypipe /etc/passwd 1 root::0:0...",
        "badge": "Kernel Overlord",
        "writeup": "1. Compile Dirty Pipe C exploit.\n2. Execute exploit targeting `/etc/passwd` to remove root password prompt.\n3. Spawn root shell with `su -`.\n4. Read `/root/flag.txt`.\n5. Flag: `flag{d1rty_p1p3_cv3_2022_0847_r00t}`"
    }
]

for item in additions:
    if item['id'] not in existing_ids:
        # Ensure uniform keys
        c_entry = {
            'id': item['id'],
            'title': item['title'],
            'category': item['category'],
            'points': item['points'],
            'difficulty': item['difficulty'],
            'description': item['description'],
            'flag': item['flag'],
            'file_url': item.get('file_url', ''),
            'hints': item['hints'],
            'concept': item['concept'],
            'cheatsheet': item['cheatsheet'],
            'badge': item['badge'],
            'writeup': item['writeup']
        }
        challenges.append(c_entry)
        existing_ids.add(item['id'])

with open('challenges.json', 'w') as f:
    json.dump(challenges, f, indent=2)

print(f"Total challenges now: {len(challenges)}")
