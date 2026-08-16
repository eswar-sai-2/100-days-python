import time 

sentence = """Furthermore, practicing poor technique will impede your progress by reinforcing your mistakes and bad habits."""
print("\n Type this exactly...")
print(sentence)

input("Press enter to start Typing..")

start_time = time.time()

typed_sentence = input("\nType the sentence:  ")

end_time = time.time()

time_taken = end_time - start_time

print("Time Taken to type : ", round(time_taken, 2), "seconds")

c = len(typed_sentence)

typing_speed = c / time_taken

print("Typing  speed :", round(typing_speed, 2), "characters/second")

if typed_sentence == sentence:
    print("Perfect! You typed the sentence correctly.")
    
else:
    print("There are some mistakes in your typing.")
