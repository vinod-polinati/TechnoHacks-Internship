todo_list = []
def display_todo_list():
    print("To-do List:")
    for i, item in enumerate(todo_list):
        print(f"{i+1}. {item}")
    print()
def add_todo_item():
    item = input("Enter a new item to add to the to-do list: ")
    todo_list.append(item)
    print(f"{item} has been added to the to-do list.\n")
def remove_todo_item():
    display_todo_list()
    item_num = input("Enter the number of the item to remove: ")
    try:
        item_num = int(item_num)
        item = todo_list[item_num - 1]
        todo_list.pop(item_num - 1)
        print(f"{item} has been removed from the to-do list.\n")
    except (ValueError, IndexError):
        print("Invalid item number. Please try again.\n")
def clear_todo_list():
    todo_list.clear()
    print("To-do list has been cleared.\n")
def show_menu():
    print("To-do List Manager")
    print("1. Display to-do list")
    print("2. Add an item to the to-do list")
    print("3. Remove an item from the to-do list")
    print("4. Clear the to-do list")
    print("5. Quit")
    choice = input("Enter your choice (1-5): ")
    print()
    return choice
while True:
    choice = show_menu()
    if choice == "1":
        display_todo_list()
    elif choice == "2":
        add_todo_item()
    elif choice == "3":
        remove_todo_item()
    elif choice == "4":
        clear_todo_list()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")