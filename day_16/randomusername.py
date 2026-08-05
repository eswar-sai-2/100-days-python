import random

name = input("Enter your name : ")

vibes = ["cool","pro","soft","introvert","x_x","$##"]

count = int(input("How many usernames do you want? "))
for i in range(count):
    username = f"{name}{random.choice(vibes)}{random.randint(1,99)}"
    print(username)