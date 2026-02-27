import re
a=input("enter a sentence: ")
b=input("enter the word: ")
c=re.search(b,a)
if c:
    print("match found")
else:
    print("no match")
