credit_score=float(input(" Enter the credits: "))
existing_debt=float(input(" Enter the debt: "))
if credit_score >= 700 and existing_debt <= 40 :
  print("Eligible")
elif 650 <= credit_score <= 699 and 41 <= existing_debt <= 50:
  print("Review")
else:
  print("Reject") 
   
  

