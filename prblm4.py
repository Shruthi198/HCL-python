amount=float(input(" Enter the amount: "))
if amount<1000:
 discount=0
elif 1000<= amount<=4999:
 discount=5
else:
  discount=10
discount=((amount*discount)/100)
amount=amount-discount
print(amount)
