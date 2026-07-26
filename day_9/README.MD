# Day 9 - Swapping Two Numbers

## 📌 Description

This program takes two numbers as input from the user and swaps their values without using a temporary variable.

## 💻 Program

```python
a = int(input("Enter one value: "))
b = int(input("Enter second value: "))

print("Before Swapping:")
print("a value is:", a)
print("b value is:", b)

a, b = b, a

print("After Swapping:")
print("a value is:", a)
print("b value is:", b)
```

## ✅ Sample Output

```
Enter one value: 15
Enter second value: 30

Before Swapping:
a value is: 15
b value is: 30

After Swapping:
a value is: 30
b value is: 15
```

## 📚 Concepts Learned

- input()
- int()
- Variables
- Multiple Assignment
- Swapping Variables
- print()

## 🎯 Key Takeaways

- Python can swap two variables without a temporary variable.
- `a, b = b, a` is a simple and efficient way to swap values.
- User input makes the program interactive.

⭐ Day 9 of my #100DaysOfPython challenge.