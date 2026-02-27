with open("example.txt","r") as s:
    count=0
    for i in s:
       words=i.split()
    count+=words.count("shru")
    print("Count:" ,count)
