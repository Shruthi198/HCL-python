import csv
data=[
      {"author":"shru","book":"short stories","pages":"323"},
      {"author":"andrew","book":"powerless","pages":"500"}
    ]
with open("student.csv","w",newline="") as f:
    d=csv.DictWriter(f,fieldnames=["author","book","pages"])
    d.writeheader()
    d.writerows(data)
print("CSV file created successfully")
    