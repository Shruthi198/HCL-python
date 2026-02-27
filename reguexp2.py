import re
a=input("enter your mailid: ")
b=re.findall(r"@([\w\.]+)",a)
print(b)