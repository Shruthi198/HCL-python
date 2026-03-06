lst=input().split()
for i in range(len(lst)):
    lst[i]=lst[i].lower()
lst=sorted(set(lst))
print(lst)