# ⏰ Day 14 - Countdown Timer

## 📖 Description

This Python program creates a simple countdown timer.

The user enters the number of seconds, and the program counts down from that number to 1. After the countdown is complete, it displays **"Time is UP!"**.

---

## 🚀 Features

- Takes countdown time from the user
- Displays the countdown every second
- Uses the `time` module
- Prints a message when the timer ends

---

## 🛠️ Concepts Used

- Variables
- input()
- int()
- for loop
- range()
- import
- time module
- time.sleep()

---

## 💻 Code

```python
import time

seconds = int(input("Enter time in seconds : "))

for i in range(seconds, 0, -1):
    print(i)
    time.sleep(1)

print("Time is UP!")
```

---

## ▶️ Sample Output

```
Enter time in seconds : 5

5
4
3
2
1

Time is UP!
```

---

## 📚 What I Learned

- How to import the `time` module
- How to pause a program using `time.sleep()`
- How to create a countdown timer
- How to use `range(start, stop, step)` for reverse counting

---

## 🎯 Future Improvements

- Display minutes and seconds
- Play a sound when the timer finishes
- Allow multiple timers
- Build a stopwatch

---

### 📅 100 Days of Python Challenge

**Day 14 Completed ✅**

Learning Python one day at a time! 🚀