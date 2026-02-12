import json
import os

todos = []

def add(todo):
    todos.append(todo)

def list_todos():
    for i, t in enumerate(todos, 1):
        print(f"{i}. {t}")

def save():
    with open("todos.json", "w") as f:
        json.dump(todos, f)

def load():
    global todos

    if not os.path.exists("todos.json"):
        print("No saved todos found.")
        return

    try:
        with open("todos.json", "r") as f:
            todos = json.load(f)
        print("Todos loaded.")
    except Exception as e:
        print("Failed to load todos:", e)

if __name__ == "__main__":
    print("Todo App v1")
    while True:
        cmd = input("add/list/save/load/quit > ")

        if cmd == "add":
            add(input("todo: "))
        elif cmd == "list":
            list_todos()
        elif cmd == "quit":
            break
        elif cmd == "save":
            save()
        elif cmd == "load":
            load()