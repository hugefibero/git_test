todos = []

def add(todo):
    todos.append(todo)

def list_todos():
    for i, t in enumerate(todos, 1):
        print(f"{i}. {t}")

if __name__ == "__main__":
    print("Todo App v1")
    while True:
        cmd = input("add/list/quit > ")

        if cmd == "add":
            add(input("todo: "))
        elif cmd == "list":
            list_todos()
        elif cmd == "quit":
            break