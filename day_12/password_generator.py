
for i in range(3):
    password = input("Enter Password : ")
    if password == "python123" :
        print("Welcome Access Granted!")
        break
    else :
        print(f"Wrong password! try again  only {2 - i}  attempts")

else:
    print("Your limit has been reached.")


