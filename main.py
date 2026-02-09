# tasks=[{"id":1,"task":"learnpython","status":"In progress"},
#       {"id":2,"task":"task manager project","status":"In progress"}
#       ]
import json

# define function
def add_task(new_task):
    tasks = load_tasks()

    # If file had a single dict earlier, fix it
    if isinstance(tasks, dict):
        tasks = [tasks]

    tasks.append(new_task)

    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=2)


#define function
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(task)

    
def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            data = json.load(f)
            if isinstance(data, dict):
                return [data] 
            return data
    except FileNotFoundError:
        return []


def update_status(id):
    tasks = load_tasks()
    found = False

    for task in tasks:
        if task["id"] == str(id):
            task["status"] = "done"
            found = True
            break

    if not found:
        print("Task not found")
        return

    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=2)

def delete_task(id):
    tasks = load_tasks()

    for i, task in enumerate(tasks):
        if task["id"]==str(id):
            tasks.pop(i)
            break
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=2)

    return tasks
        
while True:
    print("---------------------")
    print("1. Add Task")
    print("2. view Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")
    print("---------------------")

    try:
        choice=int(input("choose option: "))
    except ValueError:
        print("---------------------")
        print("Please enter a number")
        continue
    if choice == 1:
        # new_id=input("enter new id: ")
        new_id=input("enter new id:")
        title=input("enter new task: ")
        new_task_status=input("enter task status: ")
        new_task={"id":new_id,"task":title,"status":new_task_status}
        #func call
        add_task(new_task)
        print("your new task is appended!")

    elif choice == 2:
        print("you task lists: ")
        view_tasks()

    elif choice == 3:
        id=int(input("enter task id: "))
        update_status(id)
        print("status changed")

    elif choice == 4:
        id=int(input("enter task id: "))
        delete_task(id)
        # print("deleted the task id",+id)

    elif choice == 5:
        print("Thank you!!")
        break
    
    else:
        print("Invalid choice. Try again.")

#--------------------------------------------------------------------------------------------------------------------------------------
# new_task=list(({"id":1,"task":"learnpython","status":"In progress"},{"id":2,"task":"task manager project","status":"In progress"}))
# print("list as a constructor.")
# print(new_task)
# print(task)
# print(len(task))
# print(type(task))
# print(task[0]), print(task[1])

# for i in task:
#     print(i)

# for i in range(len(task)-1):
#     print(i)
#     print(task[i+1])

# i=0
# while i<(len(task)):
#     print(task[i])
#     i=i+1

# for item in task:
#     print(item["task"])

# task1=[{"id":1,"task":"learnpython","status":"In progress"},{"id":2,"task":"task manager project","status":"pending"},{"id":3,"task":"task manager project","status":"pending"}]
# for item in task1:
#     if item["status"]=="pending":
#         item["status"]="Completed"
    
# print(task1)
#-------------------------------------------------------------------------------------------------------------------------------------