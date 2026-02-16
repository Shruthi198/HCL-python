str="ababa"
s="aba"
count=0
for i in range(len(str)-len(s)+1):
  if(str[i:i+len(s)] == s):
    count+=1
    
print(count)