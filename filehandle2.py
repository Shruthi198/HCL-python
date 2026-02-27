import json
data={"name":"shru",
      "age":"21",}
with open("student.json","w")as f:
    d=json.dump(data,f)
with open("student.json","r") as f:
    a=json.load(f)
    print(a["age"])