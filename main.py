import json

todos = []

def add(todo):
    todos.append(todo)

def list_todos():
    for i, t in enumerate(todos, 1):
        print(f"{i}. {t}")

def save():
    with open("todos.json", "w") as f:
        json.dump(todos, f)

if __name__ == "__main__":
    print("Todo App v1")
    while True:
        cmd = input("add/list/save/quit > ")

        if cmd == "add":
            add(input("todo: "))
        elif cmd == "list":
            list_todos()
        elif cmd == "quit":
            break
        elif cmd == "save":
            save()