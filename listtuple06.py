lst=list(map(int,input().split()))
result=[]
for i in lst:
    if i%2==0:
        result.append(i*i)
print(result)


