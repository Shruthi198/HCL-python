lst=list(map(int,input().split()))
k=int(input())
n=len(lst)
for i in range(k):
    last=lst[n-1]
    for j in range(n-1,0,-1):
        lst[j]=lst[j-1]
    lst[0]=last
print(lst)
