import time
import random

password = input("Enter your password.")
chars = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"

guess = ""

while(guess != password):
    guess = ""
    for i in range(len(password)):
        
        guess += random.choice(chars)

    print("guessing your password..", guess)
    time.sleep(0.1)

print("\nPassword Cracked!",password)








