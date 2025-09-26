
todo_list=[]

def show_tasks():
    if not todo_list:
        print("no task yet")
    else:
        for i,task in enumerate(todo_list,1):
            print(f"{i}  {task}")

def add_task():
    task=input("enter a task:")
    todo_list.append(task)
    print("task added")

def delete_task(index):
    if 0<=index<=len(todo_list):
        removed=todo_list.pop(index-1)
        print(removed)
while True:
    print("\n=== To-Do List ===\n")
    print("1,Add tasks")
    print("2.delete tasks")
    print("3.view tasks")
    print("4.exit")

    choice=input("enter you choice:")
    if choice=="1":
        add_task()
    elif choice=="2":
        show_tasks()
        try:
            idx=int(input("enter the index:"))
            delete_task(idx)
        except ValueError:
            print("please enter a valid choice:")
    elif choice=="3":
        show_tasks()
    elif choice=="4":
        print("goodbye")
        break
    else:
        print("invalid choice")

