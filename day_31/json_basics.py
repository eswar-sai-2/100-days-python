# import json

# student = {
#     "name": "Sai",
#     "age": 19,
#     "branch": "AIML"
# }

# data = json.dumps(student)

# print(data)

# import json

# data = '{"name": "Sai", "age": 19}'

# student = json.loads(data)

# print(student)
# print(student["name"])
# print(student["age"])

# import json

# student = {                                         
#     "name": "Sai",
#     "age": 19,
#     "branch": "AIML"
# }

# with open("student.json", "w") as file:
#     json.dump(student, file)

# print("Data saved successfully!")

import json

with open("student.json", "r") as file:
    student = json.load(file)

print(student)
print(student["name"])
print(student["branch"])


    #              Python
    #                │
    #         ┌──────┴──────┐
    #         ▼             ▼
    #    json.dumps()   json.dump()
    #         │             │
    #         ▼             ▼
    #    JSON string    JSON file


    #              JSON
    #                │
    #         ┌──────┴──────┐
    #         ▼             ▼
    #    json.loads()   json.load()
    #         │             │
    #         ▼             ▼
    #    Python object   Python object