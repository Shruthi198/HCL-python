str=input("Enter the input: ")
result=""
for i in str:
    if i.isdigit():
        result+="#"
    else:
     result+= i
print(result)

