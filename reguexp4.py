import re
b=re.match(r"/d{4}-/d{2}-/d{2}","2026-11-30")

if b:
    print("Match found")
else:
    print("No match")