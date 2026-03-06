my_list=list(map(int,input().split()))
result=[]
total=0
for i in  my_list:
    if i<=0:
      break
    total+=i
    result.append(total)

print(result)