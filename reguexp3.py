import re
b=re.sub(r"\d(?=\d{4})","#",(input()))
print(b)