import os, struct, wave, zipfile, zlib, json
from PIL import Image, PngImagePlugin

os.makedirs('files/crypto', exist_ok=True)
os.makedirs('files/forensics', exist_ok=True)
os.makedirs('files/stego', exist_ok=True)
os.makedirs('files/web', exist_ok=True)
os.makedirs('files/rev', exist_ok=True)
os.makedirs('files/misc', exist_ok=True)

# 1. CRYPTO
# crypto-01.txt (ROT13)
with open('files/crypto/crypto-01.txt', 'w') as f:
    f.write("CONFIDENTIAL TRANSMISSION // INTERCEPTED\n\n")
    flag = "flag{Caesar_Is_Dead_Long_Live_ROT13}"
    rot13 = flag.translate(str.maketrans(
        "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
        "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"
    ))
    f.write(f"CIPHERTEXT: {rot13}\n")

# crypto-02.enc (Vigenere)
with open('files/crypto/crypto-02.enc', 'w') as f:
    key = "DICT"
    flag = "flag{V1g3n3r3_K3y_Wa5_DICT}"
    f.write(f"# Vigenere Encrypted Stream (Key Length: 4)\n# Target: {flag}\n")
    enc = []
    for i, c in enumerate(flag):
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            k = ord(key[i % len(key)].upper()) - ord('A')
            enc.append(chr(base + (ord(c) - base + k) % 26))
        else:
            enc.append(c)
    f.write("".join(enc) + "\n")

# crypto-03.json (RSA small e)
with open('files/crypto/crypto-03.json', 'w') as f:
    import math
    p = 1000000007
    q = 1000000009
    n = p * q
    e = 3
    # m as int
    msg = b"flag{Cub3_R00t_Att4ck_On_R54}"
    m = int.from_bytes(msg, 'big')
    c = pow(m, e, n)
    json.dump({"N": str(n), "e": e, "c": str(c), "hint": "Small public exponent attack"}, f, indent=2)

# crypto-04.txt (DB Logs)
with open('files/crypto/crypto-04.txt', 'w') as f:
    f.write("""[FINANCIAL AUDIT LOG - DISCLOSURE RESTRICTED]
2026-09-10 14:02:11 Alice transferred 5,000 PHP to Acct #8812
2026-09-10 14:05:43 Bob transferred 12,000 PHP to Acct #9931
2026-09-10 14:12:09 Fumie transferred 2,450,000 PHP to Acct #0000 [FLAG: flag{Th3_Emb3zzl3r_15_Fumie}]
2026-09-10 14:15:30 Charlie transferred 1,200 PHP to Acct #4419
""")

# crypto-05.bin (XOR stream)
with open('files/crypto/crypto-05.bin', 'wb') as f:
    key = b"CYBER"
    flag = b"flag{X0R_K3y_R3c0v3ry_Succ3ss}"
    enc = bytes([flag[i] ^ key[i % len(key)] for i in range(len(flag))])
    f.write(enc)

# crypto-06.json (Diffie-Hellman)
with open('files/crypto/crypto-06.json', 'w') as f:
    json.dump({
        "p": 7919,
        "g": 2,
        "A": 4512,
        "B": 1289,
        "ciphertext": "6861636b34676f765f6468",
        "flag": "flag{D1ff13_H3llm4n_Sm4ll_P_Br0k3n}"
    }, f, indent=2)

# 2. FORENSICS
# forensics-01: usb_image.dd
with open('files/forensics/usb_image.dd', 'wb') as f:
    f.write(b'\x00' * 1024 * 16) # 16KB disk image
    f.seek(512)
    f.write(b"EXT4_RAW_PARTITION_SECTOR\nDELETED_FILE: secret_key.txt\n")
    f.seek(2048)
    f.write(b"FLAG_RECOVERED: flag{F1l3_C4rv1ng_101}\n")

# forensics-02: capture.pcapng (using scapy)
from scapy.all import Ether, IP, UDP, DNS, DNSQR, DNSRR, wrpcap
pkts = []
queries = [
    "c3ludHsw.tunnel.exfil.org",
    "ZG5zX3R1.tunnel.exfil.org",
    "bm5lbGlu.tunnel.exfil.org",
    "Z19jYXVn.tunnel.exfil.org",
    "aHR9.tunnel.exfil.org" # base64 chunks
]
for q in queries:
    p = Ether()/IP(src="192.168.1.105", dst="8.8.8.8")/UDP(sport=53421, dport=53)/DNS(rd=1, qd=DNSQR(qname=q))
    pkts.append(p)
# Also plain HTTP packet with flag
from scapy.all import TCP, Raw
p_http = Ether()/IP(src="192.168.1.105", dst="10.0.0.1")/TCP(sport=44122, dport=80)/Raw(load=b"POST /login HTTP/1.1\r\nHost: admin.gov.ph\r\n\r\nuser=admin&token=flag{DN5_Tunn3l1ng_C4ught}\r\n")
pkts.append(p_http)
wrpcap('files/forensics/capture.pcapng', pkts)

# forensics-03: memdump.raw
with open('files/forensics/memdump.raw', 'wb') as f:
    f.write(b"WINDOWS_MEMORY_SAMPLE_DUMP\x00\x00\x00")
    f.write(b"\x90" * 4096)
    f.write(b"PROCESS: lsass.exe PID: 644 INJECTION: flag{V0l4t1l1ty_F1nd5_Pr0c3ss_Inj3ct10n}\x00")
    f.write(b"\x90" * 4096)

# forensics-04: broken_head.zip
# Normal zip has PK\x03\x04 header. We replace header with XX\x03\x04 so repair is required.
temp_zip = 'temp_broken.zip'
with zipfile.ZipFile(temp_zip, 'w') as z:
    z.writestr('flag.txt', 'flag{M4g1c_Byt3s_P4tch3d}\n')
with open(temp_zip, 'rb') as zf:
    zip_bytes = bytearray(zf.read())
zip_bytes[0] = ord('X')
zip_bytes[1] = ord('X')
with open('files/forensics/broken_head.zip', 'wb') as out_zf:
    out_zf.write(zip_bytes)
os.remove(temp_zip)

# forensics-05: document.pdf
with open('files/forensics/document.pdf', 'wb') as f:
    f.write(b"""%PDF-1.4
1 0 obj << /Type /Catalog /Pages 2 0 R >> endobj
2 0 obj << /Type /Pages /Kids [3 0 R] /Count 1 >> endobj
3 0 obj << /Type /Page /Parent 2 0 R /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >> endobj
4 0 obj << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >> endobj
5 0 obj << /Length 78 >> stream
BT /F1 12 Tf 50 700 Td (Official Memo: Confidential Flag Inside) Tj ET
% flag{H1dd3n_PDF_Str34m_Unp4ck3d}
endstream endobj
xref
0 6
0000000000 65535 f 
0000000009 00000 n 
0000000058 00000 n 
0000000115 00000 n 
0000000216 00000 n 
0000000293 00000 n 
trailer << /Size 6 /Root 1 0 R >>
startxref
422
%%EOF
""")

# forensics-06: https_traffic.pcapng
wrpcap('files/forensics/https_traffic.pcapng', pkts)

# 3. STEGANOGRAPHY
# stego-01: badge.png with tEXt metadata
img = Image.new('RGBA', (200, 200), color=(15, 23, 42, 255))
meta = PngImagePlugin.PngInfo()
meta.add_text("Secret", "flag{LSB_P1x3l_Extr4ct10n_Succ3ss}")
img.save('files/stego/badge.png', pnginfo=meta)

# stego-02: transmission.wav
with wave.open('files/stego/transmission.wav', 'w') as w:
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(44100)
    # 2 seconds of 1000Hz tone with flag marker
    samples = []
    import math
    for i in range(44100 * 2):
        val = int(32767.0 * 0.5 * math.sin(2.0 * math.pi * 1000.0 * i / 44100))
        samples.append(val)
    raw_audio = struct.pack('<' + ('h' * len(samples)), *samples)
    w.writeframes(raw_audio)
# Append flag in WAV comment block or at end
with open('files/stego/transmission.wav', 'ab') as f:
    f.write(b"FLAG_DATA: flag{Aud10_Sp3ctr0gr4m_M0rs3}")

# stego-03: datacenter.jpg
img = Image.new('RGB', (300, 200), color=(30, 41, 59))
img.save('files/stego/datacenter.jpg', 'JPEG', comment=b"FLAG: flag{Ex1f_M3t4d4t4_R3v34l3d}")

# stego-04: tampered.png
img = Image.new('RGBA', (100, 100), color=(2, 6, 23))
meta = PngImagePlugin.PngInfo()
meta.add_text("Comment", "flag{PNG_Chunky_M0nk3y}")
img.save('files/stego/tampered.png', pnginfo=meta)

# stego-05: wallpaper.jpg
img = Image.new('RGB', (100, 100), color=(10, 15, 30))
img.save('files/stego/wallpaper.jpg', 'JPEG')
with open('files/stego/wallpaper.jpg', 'ab') as f:
    f.write(b"\nEOF_EMBEDDED_ZIP\nflag{Jp3g_E0F_Tr41l1ng_D4t4}\n")

# stego-06: ordinance.txt
with open('files/stego/ordinance.txt', 'w') as f:
    f.write("Municipal Cyber Ordinance 2026-09.\n")
    # Add zero width spaces
    zw_flag = "\u200B\u200C\u200B\u200D"
    f.write(f"Section 1. Cyber Security Measures.{zw_flag}\n")
    f.write("flag{Wh1t3sp4c3_St3g0_Cl34r}\n")

# 4. WEB EXPLOITATION
for i in range(1, 7):
    with open(f'files/web/web-0{i}.txt', 'w') as f:
        f.write(f"""TARGET BRIEFING // CHALLENGE web-0{i}
==================================================
Target Endpoint: https://sandbox.cylab.gov.ph/web-0{i}/
Vulnerability Class: Web Exploitation Drill
Hint: Interactive Target Sandbox is also playable directly inside CyLab Warroom!
Local flag reference: flag{{Web_Exploit_Level_0{i}_Pwn3d}}
""")

# 5. REVERSE ENGINEERING
# rev-01: licensed_app (ELF binary with embedded string)
with open('files/rev/licensed_app', 'wb') as f:
    # Minimal 64-bit ELF header + strings
    f.write(b'\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00>\x00\x01\x00\x00\x00\x78\x00@\x00\x00\x00\x00\x00')
    f.write(b'\x90' * 128)
    f.write(b"CYLAB_LICENSE_VALIDATOR_v1.0\x00")
    f.write(b"USAGE: ./licensed_app <key>\x00")
    f.write(b"PASSWORD_CHECK: flag{Str1ngs_R3v34ls_S3cr3t}\x00")
    f.write(b"Access Granted!\x00")
os.chmod('files/rev/licensed_app', 0o755)

# rev-02: hardened_app
with open('files/rev/hardened_app', 'wb') as f:
    f.write(b'\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00>\x00')
    f.write(b'\x90' * 256)
    f.write(b"HARDENED_APP_STRIPPED\x00flag{Ghdr4_D3c0mp1l3r_W1n}\x00")
os.chmod('files/rev/hardened_app', 0o755)

# rev-03: packed_binary
with open('files/rev/packed_binary', 'wb') as f:
    f.write(b'\x7fELF\x02\x01\x01\x00UPX!_HEADER_PACKED\x00')
    f.write(b'\x90' * 128)
    f.write(b"FLAG_REVEAL: flag{Unp4ck_UPX_B1n4ry}\x00")
os.chmod('files/rev/packed_binary', 0o755)

# rev-04: script.pyc
# Generate real compiled pyc using compile()
code = compile("flag = 'flag{Pyc_D3c0mp1l3_34sy}'\nprint('Enter password:')", '<string>', 'exec')
import importlib.util
with open('files/rev/script.pyc', 'wb') as f:
    f.write(importlib.util.MAGIC_NUMBER)
    f.write(b'\x00' * 12) # timestamp & size padding
    import marshal
    f.write(marshal.dumps(code))

# rev-05: vuln_server
with open('files/rev/vuln_server', 'wb') as f:
    f.write(b'\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00')
    f.write(b'VULNERABLE_STACK_SERVER\x00gets() function used at 0x401122\x00')
    f.write(b'WIN_FUNCTION: flag{B0F_Ov3rfl0w_St4ck}\x00')
os.chmod('files/rev/vuln_server', 0o755)

# rev-06: app.apk (Zip containing classes.dex and AndroidManifest.xml)
with zipfile.ZipFile('files/rev/app.apk', 'w') as z:
    z.writestr('AndroidManifest.xml', '<manifest package="ph.gov.cylab"><application android:name="WarRoom"/></manifest>')
    z.writestr('res/values/strings.xml', '<resources><string name="flag">flag{Andr01d_Sm4l1_R3v3rs3}</string></resources>')
    z.writestr('classes.dex', b'DEX\n035\x00' + b'flag{Andr01d_Sm4l1_R3v3rs3}')

# 6. MISC / OSINT
# misc-01: social_post.png
img = Image.new('RGB', (400, 300), color=(14, 116, 144))
meta = PngImagePlugin.PngInfo()
meta.add_text("Location", "Zamboanga City Hall, Philippines (6.9044 N, 122.0790 E)")
meta.add_text("Flag", "flag{0s1nt_G30l0c4t10n_M4st3r}")
img.save('files/misc/social_post.png', pnginfo=meta)

# misc-02: damaged_qr.png
img = Image.new('RGB', (200, 200), color=(255, 255, 255))
meta = PngImagePlugin.PngInfo()
meta.add_text("QR_DATA", "flag{QR_C0d3_R3c0nstruct10n}")
img.save('files/misc/damaged_qr.png', pnginfo=meta)

# misc-03: sample.bin
with open('files/misc/sample.bin', 'wb') as f:
    f.write(b"SAMPLE_RAW_STREAM\n" + b"flag{B1n4ry_Str34m_P4rs3d}\n")

# misc-04: repo.bundle
with open('files/misc/repo.bundle', 'wb') as f:
    f.write(b"# v2 git bundle\nCOMMIT_HASH_HEAD: a1b2c3d4\nFLAG_IN_COMMIT: flag{G1t_L34k_C0mm1t_H1st0ry}\n")

# misc-05: cipher_chain.txt
import base64
raw = b"flag{N3st3d_B4s364_Enc0d1ng}"
layer1 = base64.b64encode(raw)
layer2 = base64.b64encode(layer1)
with open('files/misc/cipher_chain.txt', 'w') as f:
    f.write("# NESTED BASE64 CIPHER CHAIN\n")
    f.write(layer2.decode() + "\n")

# misc-06: dns_zone.txt
with open('files/misc/dns_zone.txt', 'w') as f:
    f.write("""; Zone file for ctf.hack4gov.ph
@       IN  SOA ns1.hack4gov.ph. admin.hack4gov.ph. ( 2026091601 3600 1800 604800 86400 )
@       IN  NS  ns1.hack4gov.ph.
@       IN  A   10.10.10.50
flag    IN  TXT "flag{DNS_Txt_R3c0rd_L34k}"
""")

print("Successfully generated all 36 challenge asset files!")
