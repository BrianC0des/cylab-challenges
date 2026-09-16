#!/usr/bin/env python3
import sys, json, os, re, shutil

if len(sys.argv) < 2:
    print("Usage: python3 set_flag_format.py <NEW_PREFIX>")
    print("Example: python3 set_flag_format.py flag")
    print("Example: python3 set_flag_format.py CYLAB")
    print("Example: python3 set_flag_format.py hack4gov")
    sys.exit(1)

new_prefix = sys.argv[1].strip().rstrip('{')

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
CHALLENGES_FILE = os.path.join(REPO_ROOT, 'challenges.json')
WARROOM_SRC = os.path.expanduser('~/Work/cylab-warroom/src/data/challenges.json')
WARROOM_DEFAULT = os.path.expanduser('~/Work/cylab-warroom/data/default-challenges.json')

with open(CHALLENGES_FILE, 'r') as f:
    challenges = json.load(f)

count = 0
for c in challenges:
    old_flag = c['flag']
    match = re.match(r'^[a-zA-Z0-9_\-.]+{(.*)}$', old_flag)
    if match:
        body = match.group(1)
        new_flag = f"{new_prefix}{{{body}}}"
        c['flag'] = new_flag
        
        # Replace occurrences in description, hints, and writeup
        c['description'] = c['description'].replace(old_flag, new_flag)
        c['writeup'] = c['writeup'].replace(old_flag, new_flag)
        for h in c.get('hints', []):
            if isinstance(h, dict) and 'text' in h:
                h['text'] = h['text'].replace(old_flag, new_flag)
        count += 1

# Save updated challenges.json
with open(CHALLENGES_FILE, 'w') as f:
    json.dump(challenges, f, indent=2)

# Update categories
cats_dir = os.path.join(REPO_ROOT, 'categories')
os.makedirs(cats_dir, exist_ok=True)
cats = {}
for c in challenges:
    cat = c['category'].lower().replace(' ', '-').replace('/', '-')
    cats.setdefault(cat, []).append(c)

for cat_name, items in cats.items():
    with open(os.path.join(cats_dir, f"{cat_name}.json"), 'w') as out:
        json.dump(items, out, indent=2)

# Sync to cylab-warroom if exists
if os.path.exists(os.path.dirname(WARROOM_SRC)):
    shutil.copyfile(CHALLENGES_FILE, WARROOM_SRC)
if os.path.exists(os.path.dirname(WARROOM_DEFAULT)):
    shutil.copyfile(CHALLENGES_FILE, WARROOM_DEFAULT)

print(f" Successfully updated {count} challenge flags to prefix '{new_prefix}{{{{...}}}}'!")
print(f" Updated {CHALLENGES_FILE}")
print(f" Updated categories in {cats_dir}")
if os.path.exists(WARROOM_SRC):
    print(f" Synced to CyLab Warroom ({WARROOM_SRC})")
