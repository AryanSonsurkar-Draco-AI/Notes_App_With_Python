Notes App (File-Based)

A simple yet powerful command-line Notes Application built with Python that allows users to add, view, search, and delete notes. All notes are stored persistently in a JSON file, making the application reliable across multiple runs.

This project focuses on core programming concepts such as file handling, data persistence, input validation, and menu-driven program design.

Features :-
Add new notes with title and content
View all saved notes
Search notes using keywords (title or content)
Delete notes using unique IDs
Persistent storage using a JSON file
Safe handling of first-run and empty files
Menu-driven continuous execution

Tech Stack :-
Language: Python
Storage: JSON (file-based)
Interface: Command Line Interface (CLI)

Project Structure
notes_app.py     # Main application file
notes.json       # Auto-generated file used to store notes

The notes.json file is automatically created when the first note is added.

How to Run :-

Ensure Python is installed on your system
Clone the repository or download the files
Run the application using:
python notes_app.py

How It Works

Menu Options :-
Add Note
View Notes
Search Notes
Delete Note
Exit

Data Handling :-
Notes are loaded from notes.json at runtime
All modifications are made in memory
The file is rewritten safely after every update

Each note contains:-
A unique ID
Title
Content
Creation timestamp

Learning Outcomes :- 
File handling in Python
Working with JSON data
CRUD operations (Create, Read, Delete)
Menu-driven application design
Input validation and error handling

Future Improvements:-
Edit existing notes
Add categories or tags
Password-protected notes
Export notes to text or PDF
GUI or web-based version

Author :-
Aryan Sonsurkar
First-year Computer Engineering student