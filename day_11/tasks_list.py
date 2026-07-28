# tasks = []

# for i in range(5):
#     task = input(f"Enter task {i+1}: ")
#     tasks.append(task)

# print("\nYour To-Do List:")
# for task in tasks:
#     print("-", task)

tasks = []
n = int(input("enter your task size : "))
for i in range(n):
    task = input(f"enter {i + 1} task : ")
    tasks.append(task)
print("\n YOUR TASKS ARE : ")
for i in range(len(tasks)):
    print(f" {i+1}. {tasks[i]} ")
