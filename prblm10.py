num=input("Enter the input with space : ")
my_list=num.split()
result=[]
seen=set()
for i in reversed(my_list):
    if i not in seen:
     result.append(i)
     seen.add(i)

result.reverse()
print(result)





