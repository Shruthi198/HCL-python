import csv
data=[]
n=int(input("enter no of stu: "))
for i in range(n):
    print(f"\nenter deets of stu:{i+1}")
    name=input("enter name: ")
    age=int(input("enter age: "))
    year=int(input("enter year: "))
    data.append({"name":name,"age":age,"year":year})
with open("deets.csv","w",newline="")as f:
    d=csv.DictWriter(f,fieldnames=["name","age","year"])
    d.writeheader()
    d.writerows(data)
    if len(data)>=50:
        print("description of the item")
    else:
        print("item not over 50")