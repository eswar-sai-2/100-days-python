
username = "sai-eswar"
password = "220"

for i in range(3):
    u = input("Enter Username : ")
    p = input("Enter Password : ")
    if u == username and p == password:
        print("Login Successfully")
        break
    else:
        print(f"Attempt {i + 1} failed.")
        print("Login Failed!")
else :
    print("Your 3 attempts are finished")



    
