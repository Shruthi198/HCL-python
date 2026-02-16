pass_word=input("Enter the pass_word: ")
count=0
max_attempt=3
if pass_word != "shrumadhu25":
  print("not valid")
  count+=1
  while count<max_attempt:
    pass_word=input()
    if pass_word=="shrumadhu25":
     print("valid")
    else:
      count+=1
      print("not valid")
      if count==max_attempt:
       print("no more attempts")
    
     

  


