import re
with open("example2.txt","r")as f:
 d=f.read()
 a=re.sub(r"\bpython\b","java",d,flags=re.IGNORECASE)
print(a)