import json
import os
from datetime import datetime

FILE_NAME = "notes.json"


def load_notes():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_notes(notes):
    with open(FILE_NAME, "w") as file:
        json.dump(notes, file, indent=4)


def add_note():
    notes = load_notes()

    title = input("Enter note title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return

    content = input("Enter note content: ").strip()
    if not content:
        print("Content cannot be empty.")
        return

    new_id = max([note["id"] for note in notes], default=0) + 1

    note = {
        "id": new_id,
        "title": title,
        "content": content,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    notes.append(note)
    save_notes(notes)

    print(f"Note added successfully (ID: {new_id})")


def view_notes():
    notes = load_notes()

    if not notes:
        print("No notes found.")
        return

    print("\n--- All Notes ---")
    for note in notes:
        print(f"\nID: {note['id']}")
        print(f"Title: {note['title']}")
        print(f"Content: {note['content']}")
        print(f"Created: {note['created_at']}")


def search_notes():
    notes = load_notes()

    if not notes:
        print("No notes available to search.")
        return

    keyword = input("Enter keyword to search: ").lower().strip()
    if not keyword:
        print("Keyword cannot be empty.")
        return

    found = False
    for note in notes:
        if keyword in note["title"].lower() or keyword in note["content"].lower():
            print(f"\nID: {note['id']}")
            print(f"Title: {note['title']}")
            print(f"Content: {note['content']}")
            print(f"Created: {note['created_at']}")
            found = True

    if not found:
        print("No matching notes found.")


def delete_note():
    notes = load_notes()

    if not notes:
        print("No notes available to delete.")
        return

    try:
        note_id = int(input("Enter note ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    for note in notes:
        if note["id"] == note_id:
            confirm = input(f"Delete note '{note['title']}'? (y/n): ").lower()
            if confirm == "y":
                notes.remove(note)
                save_notes(notes)
                print("Note deleted successfully.")
            else:
                print("Deletion cancelled.")
            return

    print("Note with this ID not found.")


def menu():
    while True:
        print("\n===== NOTES APP =====")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Search Notes")
        print("4. Delete Note")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            search_notes()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
