sentence=input("Enter the sentence: ")
abrev=["AI","ML"]
result=[]
words=sentence.split()
for w in words:
   if w.upper() in abrev:
    result.append(w.upper())
   else:
    w.capitalize()
    result.append(w.capitalize()) 

print(" ".join(result))


