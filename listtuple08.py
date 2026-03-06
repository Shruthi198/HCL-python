pass_=input()
count = 0
while count < 3:
    attempt = input()
    if attempt == pass_:
        print("unlocked")
        break
    count += 1
if count == 3:
    print("locked")
