import os, struct, wave, zipfile, tarfile, zlib, json, sqlite3, math, py_compile
from PIL import Image

BASE_DIR = 'files'
RAW_URL_BASE = 'https://raw.githubusercontent.com/BrianC0des/cylab-challenges/main/files'

os.makedirs(f'{BASE_DIR}/crypto', exist_ok=True)
os.makedirs(f'{BASE_DIR}/forensics', exist_ok=True)
os.makedirs(f'{BASE_DIR}/stego', exist_ok=True)
os.makedirs(f'{BASE_DIR}/web', exist_ok=True)
os.makedirs(f'{BASE_DIR}/rev', exist_ok=True)
os.makedirs(f'{BASE_DIR}/misc', exist_ok=True)

# Map of challenge_id -> filename
file_map = {}

# ==========================================
# 1. CRYPTOGRAPHY DRILLS
# ==========================================

# crypto-7: Mod 26 Carousel (Affine)
p = f'{BASE_DIR}/crypto/crypto-07.txt'
with open(p, 'w') as f:
    f.write("[INTERCEPTED ADMIRALTY DISPATCH]\n")
    f.write("Algorithm: Affine Cipher E(x) = (5*x + 8) mod 26\n")
    f.write("Target Transmission:\n")
    f.write("Wbgx jv qyv ftxa: flag{4ff1n3_c1ph3r_unw0und}\n")
file_map['crypto-7'] = 'crypto/crypto-07.txt'

# crypto-8: Hastad's Broadcast Attack
p = f'{BASE_DIR}/crypto/crypto-08.json'
with open(p, 'w') as f:
    json.dump({
        "e": 3,
        "transmissions": [
            {"N": "151703906371", "c": "49182390123"},
            {"N": "162810394851", "c": "12984102941"},
            {"N": "173921849203", "c": "98234102948"}
        ],
        "flag_hint": "Recover m using Chinese Remainder Theorem: m^3 mod (N1*N2*N3)",
        "plaintext_flag": "flag{h4st4d_br04dc4st_crt_r00t}"
    }, f, indent=2)
file_map['crypto-8'] = 'crypto/crypto-08.json'

# crypto-9: Bleichenbacher's Padding Oracle
p = f'{BASE_DIR}/crypto/crypto-09.json'
with open(p, 'w') as f:
    json.dump({
        "target": "PKCS#1 v1.5 Padding Oracle Endpoint",
        "modulus_bits": 1024,
        "oracle_uri": "https://oracle.internal.cylab.ph/verify_padding",
        "sample_ciphertext_hex": "3a7b9c...f4a1",
        "flag": "flag{bl31ch3nb4ch3r_1998_p4dd1ng_0r4cl3}"
    }, f, indent=2)
file_map['crypto-9'] = 'crypto/crypto-09.json'

# crypto-10: AES-GCM Nonce Reuse
p = f'{BASE_DIR}/crypto/crypto-10.json'
with open(p, 'w') as f:
    json.dump({
        "nonce_reused": "deadbeefdeadbeefdeadbeef",
        "msg1": {"ct": "a1b2c3d4e5f6...", "tag": "4491029381029381"},
        "msg2": {"ct": "f6e5d4c3b2a1...", "tag": "9910293810293810"},
        "flag": "flag{gcm_f0rb1dd3n_gh4sh_k3y_r3c0v3r3d}"
    }, f, indent=2)
file_map['crypto-10'] = 'crypto/crypto-10.json'

# crypto-11: Rail Fence
p = f'{BASE_DIR}/crypto/crypto-11.txt'
with open(p, 'w') as f:
    f.write("CIPHERTEXT (Rails=3): f{aesLvvR3lgCarI_edon_ieOT}as_D_Lg_1\n")
    f.write("RECOVERED_FLAG: flag{rail_f3nc3_z1gz4g_unf0ld3d}\n")
file_map['crypto-11'] = 'crypto/crypto-11.txt'

# crypto-12: Polybius Square
p = f'{BASE_DIR}/crypto/crypto-12.txt'
with open(p, 'w') as f:
    f.write("TAP CODE PAIRS: 41 34 31 54 12 24 45 43\n")
    f.write("Grid: 5x5 Polybius\n")
    f.write("DECODED: flag{p0lyb1us_t4p_c0d3_d3c0d3d}\n")
file_map['crypto-12'] = 'crypto/crypto-12.txt'

# crypto-13: Beaufort Cipher
p = f'{BASE_DIR}/crypto/crypto-13.txt'
with open(p, 'w') as f:
    f.write("Key: NAVAL\nMode: Beaufort Reciprocal\nTarget: flag{b34uf0rt_r3c1pr0c4l_v1g3n3r3}\n")
file_map['crypto-13'] = 'crypto/crypto-13.txt'

# crypto-14: Solitaire Deck
p = f'{BASE_DIR}/crypto/crypto-14.txt'
with open(p, 'w') as f:
    f.write("Solitaire Keystream Generation\nFlag: flag{s0l1t41r3_c4rd_d3ck_k3ystr34m}\n")
file_map['crypto-14'] = 'crypto/crypto-14.txt'

# crypto-15: Wiener's Continued Fraction
p = f'{BASE_DIR}/crypto/crypto-15.json'
with open(p, 'w') as f:
    json.dump({
        "attack": "Wiener Continued Fraction (Small d)",
        "N": "1797693134862315907729305190789024733617976978942306572734300811577326758055054784379",
        "e": "1198462089908210605152870127192683155745317985961537715156200541051551172036703189587",
        "flag": "flag{w13n3r_c0nt1nu3d_fr4ct10n_d_sm4ll}"
    }, f, indent=2)
file_map['crypto-15'] = 'crypto/crypto-15.json'

# crypto-16: Franklin-Reiter
p = f'{BASE_DIR}/crypto/crypto-16.json'
with open(p, 'w') as f:
    json.dump({
        "attack": "Franklin-Reiter Related Message Attack",
        "e": 3,
        "difference": 42,
        "flag": "flag{fr4nkl1n_r31t3r_p0lyn0m14l_gcd}"
    }, f, indent=2)
file_map['crypto-16'] = 'crypto/crypto-16.json'

# crypto-17: Merkle-Hellman Knapsack
p = f'{BASE_DIR}/crypto/crypto-17.json'
with open(p, 'w') as f:
    json.dump({
        "attack": "Merkle-Hellman LLL Reduction",
        "public_key": [102, 205, 411, 822, 1644, 3288, 6576, 13152],
        "ciphertext": 15483,
        "flag": "flag{m3rkl3_h3llm4n_lll_l4tt1c3_r3duc3d}"
    }, f, indent=2)
file_map['crypto-17'] = 'crypto/crypto-17.json'

# ==========================================
# 2. FORENSICS DRILLS
# ==========================================

# forensics-7: Magic Bytes Reconstruction (evidence.dat -> corrupted PNG)
p = f'{BASE_DIR}/forensics/evidence.dat'
with open(p, 'wb') as f:
    f.write(b"\xDE\xAD\xBE\xEF\x00\x00\x00\x00")
    ihdr = struct.pack(">IIBBBBB", 100, 50, 8, 2, 0, 0, 0)
    ihdr_crc = struct.pack(">I", zlib.crc32(b"IHDR" + ihdr) & 0xffffffff)
    f.write(struct.pack(">I", len(ihdr)) + b"IHDR" + ihdr + ihdr_crc)
    txt_data = b"Comment\x00flag{m4g1c_byt3s_png_h34d3r_f1x3d}"
    txt_crc = struct.pack(">I", zlib.crc32(b"tEXt" + txt_data) & 0xffffffff)
    f.write(struct.pack(">I", len(txt_data)) + b"tEXt" + txt_data + txt_crc)
    f.write(b"\x00\x00\x00\x00IEND\xaeB`\x82")
file_map['forensics-7'] = 'forensics/evidence.dat'

# forensics-8: USB Keystroke HID Capture (usb_hid.pcap)
from scapy.all import Ether, IP, UDP, Raw, wrpcap
pkts = []
for char, keycode in [('f', 0x09), ('l', 0x0f), ('a', 0x04), ('g', 0x0a)]:
    p = Ether()/IP(src="192.168.1.50", dst="192.168.1.1")/UDP(sport=1000, dport=2000)/Raw(load=f"USB_HID_REPORT:{keycode}:flag{{usb_h1d_k3ystr0k3_p4rs3d}}".encode())
    pkts.append(p)
p_hid = f'{BASE_DIR}/forensics/usb_hid.pcap'
wrpcap(p_hid, pkts)
file_map['forensics-8'] = 'forensics/usb_hid.pcap'

# forensics-9: Ext4 Inode Carving & Journal Recovery (disk.img)
p = f'{BASE_DIR}/forensics/disk.img'
with open(p, 'wb') as f:
    f.write(b'\x00' * 32768)
    f.seek(1024)
    f.write(b"EXT4_SUPERBLOCK_MAGIC: \x53\xef\n")
    f.seek(4096)
    f.write(b"JBD2_JOURNAL_BLOCK\n")
    f.seek(8192)
    f.write(b"RECOVERED_JOURNAL_RECORD: rm -rf /var/log/secure\nFLAG: flag{3xt4_j0urn4l_und3l3t3_succ3ss}\n")
file_map['forensics-9'] = 'forensics/disk.img'

# forensics-10: TLS 1.3 Keylog Decryption (sslkeylog.log)
p = f'{BASE_DIR}/forensics/sslkeylog.log'
with open(p, 'w') as f:
    f.write("# SSL/TLS secrets log file, generated by NSS\n")
    f.write("CLIENT_HANDSHAKE_TRAFFIC_SECRET a1b2c3d4e5f6 1234567890abcdef\n")
    f.write("SERVER_HANDSHAKE_TRAFFIC_SECRET a1b2c3d4e5f6 fedcba0987654321\n")
    f.write("EXFILTRATED_HTTP2_PAYLOAD: flag{tls13_k3yl0g_http2_d3crypt3d}\n")
file_map['forensics-10'] = 'forensics/sslkeylog.log'

# forensics-11: Bash History (.bash_history)
p = f'{BASE_DIR}/forensics/bash_history.txt'
with open(p, 'w') as f:
    f.write("ls -la\ncd /opt/admin\n./backup.sh --token=flag{b4sh_h1st0ry_d0tf1l3s_4ud1t}\nexit\n")
file_map['forensics-11'] = 'forensics/bash_history.txt'

# forensics-12: Chromium SQLite History (history.sqlite)
p = f'{BASE_DIR}/forensics/history.sqlite'
conn = sqlite3.connect(p)
cur = conn.cursor()
cur.execute("CREATE TABLE urls (id INTEGER PRIMARY KEY, url TEXT, title TEXT, visit_count INTEGER)")
cur.execute("INSERT INTO urls VALUES (1, 'https://internal.portal/auth?key=flag{chr0m1um_sql1t3_h1st0ry_3xtr4ct}', 'Admin Portal', 5)")
conn.commit()
conn.close()
file_map['forensics-12'] = 'forensics/history.sqlite'

# forensics-13: Windows EVTX (eventlog.xml)
p = f'{BASE_DIR}/forensics/eventlog.xml'
with open(p, 'w') as f:
    f.write("""<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System><EventID>4104</EventID><TimeCreated SystemTime="2026-09-12T08:14:22.000Z"/></System>
  <EventData>
    <Data Name="ScriptBlockText">Invoke-Expression -Command "Write-Host flag{3vtx_p0w3rsh3ll_scr1ptbl0ck_4104}"</Data>
  </EventData>
</Event>""")
file_map['forensics-13'] = 'forensics/eventlog.xml'

# forensics-14: Master Boot Record (drive.raw)
p = f'{BASE_DIR}/forensics/drive.raw'
with open(p, 'wb') as f:
    f.write(b'\x00' * 16384)
    f.seek(510)
    f.write(b'\x55\xaa')
    f.seek(1024)
    f.write(b"VBR_HEADER: flag{mbr_p4rt1t10n_t4bl3_r3c0v3r3d}\n")
file_map['forensics-14'] = 'forensics/drive.raw'

# forensics-15: Offline Registry Hive (sam.hive)
p = f'{BASE_DIR}/forensics/sam.hive'
with open(p, 'wb') as f:
    f.write(b"regf" + b"\x00"*256 + b"SAM_HIVE_SECRETS: Administrator:500:AAD3B435...:flag{s4m_syst3m_h1v3_s3cr3tsdmp_pwn}\n")
file_map['forensics-15'] = 'forensics/sam.hive'

# forensics-16: Shimcache (shimcache.bin)
p = f'{BASE_DIR}/forensics/shimcache.bin'
with open(p, 'wb') as f:
    f.write(b"10ts" + b"\x00"*64 + b"C:\\Windows\\Temp\\malware.exe | SHA1: flag{sh1mc4ch3_4mc4ch3_3x3cut10n_pr0v3d}\n")
file_map['forensics-16'] = 'forensics/shimcache.bin'

# forensics-17: Linux Kernel Core Dump (kernel_vmcore.txt)
p = f'{BASE_DIR}/forensics/kernel_vmcore.txt'
with open(p, 'w') as f:
    f.write("[KERNEL MEMORY DUMP AUDIT]\n")
    f.write("Hooked Syscall: sys_call_table[__NR_read] -> 0xffffffffc0839100 [rootkit_lkm]\n")
    f.write("Extracted Secret: flag{lkm_r00tk1t_hook3d_sysc4ll_t4bl3}\n")
file_map['forensics-17'] = 'forensics/kernel_vmcore.txt'

# ==========================================
# 3. STEGANOGRAPHY DRILLS
# ==========================================

# stego-7: Trailing EOF Concatenation (vacation.jpg)
p = f'{BASE_DIR}/stego/vacation.jpg'
img = Image.new('RGB', (100, 100), color=(73, 109, 137))
img.save(p)
with open(p, 'ab') as f:
    f.write(b"\n--- HIDDEN ATTACHMENT PAST EOF ---\nFLAG: flag{30f_tr41l1ng_d4t4_c4rv3d}\n")
file_map['stego-7'] = 'stego/vacation.jpg'

# stego-8: Audio DTMF Tones (voicemail.wav)
p = f'{BASE_DIR}/stego/voicemail.wav'
with wave.open(p, 'w') as w:
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(8000)
    frames = bytearray()
    for i in range(8000):
        val = int(10000 * (math.sin(2 * math.pi * 697 * i / 8000) + math.sin(2 * math.pi * 1209 * i / 8000)))
        frames.extend(struct.pack('<h', val))
    w.writeframes(frames)
with open(p, 'ab') as f:
    f.write(b"DTMF_LOG: 13374242 -> flag{dtmf_t0n3s_fr3qu3ncy_d14l3d}\n")
file_map['stego-8'] = 'stego/voicemail.wav'

# stego-9: Unicode Zero-Width (secret.txt)
p = f'{BASE_DIR}/stego/secret.txt'
with open(p, 'w', encoding='utf-8') as f:
    f.write("Important announcement regarding system security.\u200b\u200c\u200b\n")
    f.write("# Decoded Zero-Width Sequence: flag{z3r0_w1dth_un1c0d3_st3g4n0}\n")
file_map['stego-9'] = 'stego/secret.txt'

# stego-10: Palette Index Modulo (palette.bmp)
p = f'{BASE_DIR}/stego/palette.bmp'
img = Image.new('P', (32, 32))
img.putpalette([i % 256 for i in range(768)])
img.save(p)
with open(p, 'ab') as f:
    f.write(b"PALETTE_MODULO: flag{clut_p4l3tt3_1nd3x_m0dul4t10n}\n")
file_map['stego-10'] = 'stego/palette.bmp'

# stego-11: Audio Phase Inversion (stereo_track.wav)
p = f'{BASE_DIR}/stego/stereo_track.wav'
with wave.open(p, 'w') as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(8000)
    frames = bytearray()
    for i in range(4000):
        v1 = int(8000 * math.sin(2 * math.pi * 440 * i / 8000))
        v2 = -v1
        frames.extend(struct.pack('<hh', v1, v2))
    w.writeframes(frames)
with open(p, 'ab') as f:
    f.write(b"PHASE_CANCEL: flag{aud10_ph4s3_1nv3rs10n_c4nc3l}\n")
file_map['stego-11'] = 'stego/stereo_track.wav'

# stego-12: BMP Row Padding (padding.bmp)
p = f'{BASE_DIR}/stego/padding.bmp'
img = Image.new('RGB', (17, 17), color=(20, 40, 60))
img.save(p)
with open(p, 'ab') as f:
    f.write(b"ROW_PADDING_LEAK: flag{bmp_p4dd1ng_byt3s_unp4ck3d}\n")
file_map['stego-12'] = 'stego/padding.bmp'

# stego-13: PDF Flate (annotated.pdf)
p = f'{BASE_DIR}/stego/annotated.pdf'
with open(p, 'wb') as f:
    content = b"PDF_DOCUMENT_CONTENT\nFLAG: flag{pdf_fl4t3_str34m_4nn0t4t10n}\n"
    compressed = zlib.compress(content)
    f.write(b"%PDF-1.4\n1 0 obj\n<< /Length " + str(len(compressed)).encode() + b" /Filter /FlateDecode >>\nstream\n" + compressed + b"\nendstream\nendobj\n%%EOF")
file_map['stego-13'] = 'stego/annotated.pdf'

# stego-14: Tar Slack Space (archive.tar)
p = f'{BASE_DIR}/stego/archive.tar'
with tarfile.open(p, 'w') as tar:
    pass
with open(p, 'ab') as f:
    f.write(b"\x00" * 512 + b"TAR_SLACK: flag{t4r_bl0ck_sl4ck_sp4c3_c4rv3d}\n")
file_map['stego-14'] = 'stego/archive.tar'

# stego-15: Video I-Frame (keyframes.txt)
p = f'{BASE_DIR}/stego/keyframes.txt'
with open(p, 'w') as f:
    f.write("GOP Structure Analysis (I-Frame Quantization Matrix):\nFlag: flag{mp4_1fr4m3_g0p_qu4nt1z4t10n}\n")
file_map['stego-15'] = 'stego/keyframes.txt'

# stego-16: Spread Spectrum (frequency_matrix.csv)
p = f'{BASE_DIR}/stego/frequency_matrix.csv'
with open(p, 'w') as f:
    f.write("Time_ms,Freq_MHz,PN_Chip,Flag\n0,2412,1,flag{dsss_spr34d_sp3ctrum_d3spr34d}\n")
file_map['stego-16'] = 'stego/frequency_matrix.csv'

# ==========================================
# 4. WEB EXPLOITATION DRILLS
# ==========================================

web_drills = [
    ('web-7', 'robots_dump.txt', "User-agent: *\nDisallow: /dev-secret-internal-logs/\n# Flag: flag{r0b0ts_txt_d1r_tr4v3rs4l_f0und}\n"),
    ('web-8', 'ping_service.py', "import os\nip = input('Host: ')\nos.system('ping -c 1 ' + ip) # Flag: flag{c0mm4nd_1nj3ct10n_p1ng_pwn3d}\n"),
    ('web-9', 'vuln_merge.js', "function merge(target, source) { for (let k in source) { if (k === '__proto__') target[k] = source[k]; } }\n// Flag: flag{pr0t0typ3_p0llut10n_n0d3_rc3}\n"),
    ('web-10', 'deserialize_app.py', "import pickle, base64\n# Flag: flag{p1ckl3_d3s3r14l1z4t10n_rc3_pwn}\n"),
    ('web-11', 'token.jwt', "eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJzdWIiOiJhZG1pbiIsImZsYWciOiJmbGFne2p3dF9uMG4zXzRsZzByMXRobV9ieXBhc3N9In0.\n"),
    ('web-12', 'cors_policy.json', '{"Access-Control-Allow-Origin": "null", "Access-Control-Allow-Credentials": true, "flag": "flag{c0rs_cr3d3nt14ls_0r1g1n_l34k}"}\n'),
    ('web-13', 'payload.xml', '<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/flag">]><user><name>&xxe;</name><flag>flag{xx3_3xt3rn4l_3nt1ty_f1l3_r34d}</flag></user>\n'),
    ('web-14', 'csrf_poc.html', '<html><body><form action="http://target/profile/update-email" method="POST"><input name="email" value="attacker@evil.com" /></form><!-- flag{csrf_p0st_f0rm_3m41l_t4k30v3r} --></body></html>\n'),
    ('web-15', 'schema.graphql', 'type Query { systemFlag(secretKey: String): String }\n# Output: flag{gr4phql_1ntr0sp3ct10n_sch3m4_l34k}\n'),
    ('web-16', 'rebinding_setup.txt', 'DNS Rebinding Configuration:\nDomain: 7f000001.a8000001.rbndr.us\nTarget: flag{dns_r3b1nd1ng_ssrf_m3t4d4t4_pwn}\n'),
    ('web-17', 'payload_cc5.ser', 'AC ED 00 05 (Java Serialized Object CommonsCollections5)\nFLAG: flag{j4v4_d3s3r14l1z4t10n_ys0s3r14l_rc3}\n')
]

for wid, wfile, wcontent in web_drills:
    wp = f'{BASE_DIR}/web/{wfile}'
    with open(wp, 'w') as f:
        f.write(wcontent)
    file_map[wid] = f'web/{wfile}'

# ==========================================
# 5. REVERSE ENGINEERING DRILLS
# ==========================================

# rev-7: Compiled Python Bytecode (auth_check.pyc)
temp_py = 'temp_auth_check.py'
with open(temp_py, 'w') as f:
    f.write('def check_license(key):\n    if key == "flag{pyc_byt3c0d3_d3c0mp1l3d_34sy}":\n        return True\n    return False\n')
py_compile.compile(temp_py, cfile=f'{BASE_DIR}/rev/auth_check.pyc')
os.remove(temp_py)
file_map['rev-7'] = 'rev/auth_check.pyc'

# rev-8: Anti-Debug Binary
p = f'{BASE_DIR}/rev/license_validator'
with open(p, 'wb') as f:
    f.write(b"\x7fELF\x02\x01\x01\x00" + b"\x00"*32 + b"ptrace_detected_exit\n" + b"FLAG: flag{ptr4c3_4nt1_d3bug_byp4ss3d}\n")
os.chmod(p, 0o755)
file_map['rev-8'] = 'rev/license_validator'

# rev-9: Angr Symbolic Keygen
p = f'{BASE_DIR}/rev/matrix_hasher'
with open(p, 'wb') as f:
    f.write(b"\x7fELF\x02\x01\x01\x00" + b"\x00"*32 + b"angr_symbolic_target: flag{4ngr_symb0l1c_smt_s0lv3d}\n")
os.chmod(p, 0o755)
file_map['rev-9'] = 'rev/matrix_hasher'

# rev-10: Custom VM Bytecode
p = f'{BASE_DIR}/rev/bytecode.bin'
with open(p, 'wb') as f:
    f.write(bytes([0x01, 0x41, 0x02, 0x13, 0x03]) + b"\nVM_FLAG: flag{cust0m_vm_byt3c0d3_d1s4ss3mbl3d}\n")
file_map['rev-10'] = 'rev/bytecode.bin'

# rev-11: WebAssembly (check.wasm)
p = f'{BASE_DIR}/rev/check.wasm'
with open(p, 'wb') as f:
    f.write(b"\x00asm\x01\x00\x00\x00")
    f.write(b"\x0b\x2c\x01\x00\x41\x00\x0b\x24flag{w4sm_w4sm2w4t_byt3c0d3_r34d}")
file_map['rev-11'] = 'rev/check.wasm'

# rev-12: .NET C# Assembly (Vault.exe)
p = f'{BASE_DIR}/rev/Vault.exe'
with open(p, 'wb') as f:
    f.write(b"MZ\x90\x00\x03\x00\x00\x00" + b"\x00"*128 + b"BSJB" + b"\x00"*32 + b"VerifyMasterKey: flag{d0tn3t_csh4rp_1lspy_d3c0mp1l3}\n")
file_map['rev-12'] = 'rev/Vault.exe'

# rev-13: Go Stripped Binary
p = f'{BASE_DIR}/rev/target_go_bin'
with open(p, 'wb') as f:
    f.write(b"\x7fELF\x02\x01\x01\x00" + b"\x00"*32 + b"pclntab_gopclntab: flag{g0l4ng_pclnt4b_symb0ls_r3st0r3d}\n")
file_map['rev-13'] = 'rev/target_go_bin'

# rev-14: Rust Demangled Binary
p = f'{BASE_DIR}/rev/rust_validator'
with open(p, 'wb') as f:
    f.write(b"\x7fELF\x02\x01\x01\x00" + b"\x00"*32 + b"_ZN7my_app13validate_flag17h4f7b2a9e: flag{rust_d3m4ngl3_1t3r4t0r_r3v}\n")
file_map['rev-14'] = 'rev/rust_validator'

# rev-15: Windows PE IAT Hooking
p = f'{BASE_DIR}/rev/packed_pe.exe'
with open(p, 'wb') as f:
    f.write(b"MZ\x90\x00PE\x00\x00" + b"\x00"*64 + b"IAT_HOOK: flag{14t_h00k1ng_scyll4_03p_dump3d}\n")
file_map['rev-15'] = 'rev/packed_pe.exe'

# rev-16: Android Native Library (libnative-lib.so)
p = f'{BASE_DIR}/rev/libnative-lib.so'
with open(p, 'wb') as f:
    f.write(b"\x7fELF\x02\x01\x01\x00" + b"\x00"*32 + b"Java_ph_gov_cylab_Check_verifyFlag: flag{fr1d4_jn1_n4t1v3_h00k_succ3ss}\n")
file_map['rev-16'] = 'rev/libnative-lib.so'

# rev-17: Linux eBPF Bytecode (filter.o)
p = f'{BASE_DIR}/rev/filter.o'
with open(p, 'wb') as f:
    f.write(b"\x7fELF\x02\x01\x01\x00" + b"\x00"*32 + b"bpf_prog_sec: flag{3bpf_byt3c0d3_k3rn3l_f1lt3r_r3v}\n")
file_map['rev-17'] = 'rev/filter.o'

# ==========================================
# 6. MISC / OSINT DRILLS
# ==========================================

# misc-7: SUID Check
p = f'{BASE_DIR}/misc/suid_audit.txt'
with open(p, 'w') as f:
    f.write("-rwsr-xr-x 1 root root /usr/bin/find\n# Exploit: find . -exec /bin/sh -p \\;\n# Flag: flag{su1d_gtf0b1ns_r00t_pr1v3sc}\n")
file_map['misc-7'] = 'misc/suid_audit.txt'

# misc-8: Stack Buffer Overflow (vuln)
p = f'{BASE_DIR}/misc/vuln'
with open(p, 'wb') as f:
    f.write(b"\x7fELF\x02\x01\x01\x00" + b"\x00"*32 + b"ret2win: flag{r3t2w1n_st4ck_b0f_c0ntr0l}\n")
os.chmod(p, 0o755)
file_map['misc-8'] = 'misc/vuln'

# misc-9: ROP Chain Binary (rop_vuln)
p = f'{BASE_DIR}/misc/rop_vuln'
with open(p, 'wb') as f:
    f.write(b"\x7fELF\x02\x01\x01\x00" + b"\x00"*32 + b"pop_rdi_ret: flag{r3t2l1bc_r0p_ch41n_nx_byp4ss}\n")
os.chmod(p, 0o755)
file_map['misc-9'] = 'misc/rop_vuln'

# misc-10: Heap Tcache Poisoning (heap_vuln)
p = f'{BASE_DIR}/misc/heap_vuln'
with open(p, 'wb') as f:
    f.write(b"\x7fELF\x02\x01\x01\x00" + b"\x00"*32 + b"tcache_poison: flag{gl1bc_tc4ch3_p01s0n_s4f3_l1nk}\n")
os.chmod(p, 0o755)
file_map['misc-10'] = 'misc/heap_vuln'

# misc-11: Zip Slip (submission.zip)
p = f'{BASE_DIR}/misc/submission.zip'
with zipfile.ZipFile(p, 'w') as z:
    z.writestr("../../var/www/html/shell.php", "<?php // flag{z1p_sl1p_p4th_tr4v3rs4l_wr1t3} ?>")
file_map['misc-11'] = 'misc/submission.zip'

# misc-12: Wi-Fi PMKID (pmkid.22000)
p = f'{BASE_DIR}/misc/pmkid.22000'
with open(p, 'w') as f:
    f.write("WPA*02*4a91029381...*flag{wpa2_pmk1d_h4shc4t_cr4ck3d}\n")
file_map['misc-12'] = 'misc/pmkid.22000'

# misc-13: Flight ADS-B Logs (adsb_flight.json)
p = f'{BASE_DIR}/misc/adsb_flight.json'
with open(p, 'w') as f:
    json.dump({
        "icao_hex": "4A12BC",
        "squawk": "7700",
        "lat": 14.5086,
        "lon": 121.0194,
        "flag": "flag{4dsb_fl1ght_tr4ck1ng_1c40_0s1nt}"
    }, f, indent=2)
file_map['misc-13'] = 'misc/adsb_flight.json'

# misc-14: Suncalc Calculation (shadow.jpg)
p = f'{BASE_DIR}/misc/shadow.jpg'
img = Image.new('RGB', (100, 100), color=(180, 160, 120))
img.save(p)
with open(p, 'ab') as f:
    f.write(b"EXIF: Bearing 48 deg | Shadow ratio 1.42 | flag{sunc4lc_sh4d0w_t1m3_g30l0c4t10n}\n")
file_map['misc-14'] = 'misc/shadow.jpg'

# misc-15: Format String Write (fmtstr_app)
p = f'{BASE_DIR}/misc/fmtstr_app'
with open(p, 'wb') as f:
    f.write(b"\x7fELF\x02\x01\x01\x00" + b"\x00"*32 + b"fmtstr_got_overwrite: flag{fmtstr_4rb1tr4ry_wr1t3_g0t_pwn}\n")
os.chmod(p, 0o755)
file_map['misc-15'] = 'misc/fmtstr_app'

# misc-16: Dirty Pipe Kernel Exploit (dirtypipe.c)
p = f'{BASE_DIR}/misc/dirtypipe.c'
with open(p, 'w') as f:
    f.write("// CVE-2022-0847 Dirty Pipe Exploit\n// Target: Linux Kernel 5.16.10\n// FLAG: flag{d1rty_p1p3_cv3_2022_0847_r00t}\n")
file_map['misc-16'] = 'misc/dirtypipe.c'

print(f"Generated {len(file_map)} drill asset files successfully!")

# Now update challenges.json with their file_urls
with open('challenges.json', 'r') as f:
    challenges = json.load(f)

updated_count = 0
for c in challenges:
    cid = c['id']
    if cid in file_map:
        rel_path = file_map[cid]
        c['file_url'] = f"{RAW_URL_BASE}/{rel_path}"
        updated_count += 1

with open('challenges.json', 'w') as f:
    json.dump(challenges, f, indent=2)

print(f"Updated challenges.json with {updated_count} file_urls!")
