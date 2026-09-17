while True:
    print("\n===== NOTES APP =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Delete Note")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        note = input("Enter your note: ")

        with open("notes.txt", "a") as file:
            file.write(note + "\n")

        print("Note saved successfully!")

    elif choice == "2":
        try:
            with open("notes.txt", "r") as file:
                notes = file.readlines()

            if not notes:
                print("No notes found.")
                continue

            print("\n===== YOUR NOTES =====")

            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note.strip()}")

        except FileNotFoundError:
            print("No notes found.")

    elif choice == "3":
        try:
            with open("notes.txt", "r") as file:
                notes = file.readlines()

            if not notes:
                print("No notes to delete.")
                continue

            print("\n===== YOUR NOTES =====")

            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note.strip()}")

            number = int(input("Enter note number to delete: "))

            if 1 <= number <= len(notes):
                deleted_note = notes.pop(number - 1)

                with open("notes.txt", "w") as file:
                    file.writelines(notes)

                print("Deleted:", deleted_note.strip())

            else:
                print("Invalid note number.")

        except FileNotFoundError:
            print("No notes found.")

        except ValueError:
            print("Please enter a number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")







































































# file = open("sample.txt","r")

# content = file.read()
# print(content)
# file.close()



# file = open("sample.txt", "w")
# file.write("Hello sai!\n")
# file.write("I am learning file handilng in python.")
# file.close()
# print("Data is written into file successfully.")





# file = open("sample.txt", "a")
# file.write("\n This is a new line. ")
# file.write("\n I am learning python this is day 30.")
# file.close()
# print("data is written successful.")

# with open("sample.txt", "r") as file:
#     content = file.read()

# print(content)

# with open("sample.txt", "w") as file:
#     file.write("Hello sai!")
# print("data is written into file successfully.")

# with open("sample.txt", "a") as file:
#     file.write("\n I am learning python.")


# with open("sample.txt", "r") as file:
#     content = file.read()

# print(content)

# with open("sample.txt", "r") as file:
#     line = file.readline()

# print(line)

# with open("sample.txt", "r") as file:
#     lines = file.readlines()

# print(lines)

# with open("sample.txt", "r") as file:
#     for line in file:
#         print(line.strip())



