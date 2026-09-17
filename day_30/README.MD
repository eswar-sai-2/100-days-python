# 📝 Python Notes App

A simple command-line **Notes App built with Python** using **File Handling**.

This project allows users to add, view, and delete notes. All notes are stored in a text file (`notes.txt`), so the data remains available after the program is closed.

## 🚀 Features

- ➕ Add a note
- 📖 View all saved notes
- 🗑️ Delete a selected note
- 💾 Store notes permanently in a text file
- 🔢 Display notes with numbers
- 🛡️ Handle missing files
- ⚠️ Handle invalid user input
- 🔄 Menu-driven interface

## 🧠 Concepts Used

### File Handling
- `open()`
- `with open()`
- Read mode (`"r"`)
- Write mode (`"w"`)
- Append mode (`"a"`)
- `read()`
- `readlines()`
- `write()`
- `writelines()`

### Exception Handling
- `try`
- `except`
- `FileNotFoundError`
- `ValueError`

### Python Concepts
- `while` loop
- `if / elif / else`
- `input()`
- Lists
- `enumerate()`
- `pop()`
- `strip()`

## 📂 Project Structure

```text
day_30/
│
├── notes_app.py
└── notes.txt