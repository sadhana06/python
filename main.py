tasks=[{"id":1,"task":"learnpython","status":"In progress"},
      {"id":2,"task":"task manager project","status":"In progress"}
      ]

# define function
def add_task(new_task):
    tasks.append(new_task)

#define function
def view_tasks(tasks):
    for i in tasks:
        print(i)

while True:
    print("1. Add Task")
    print("2. view Tasks")
    print("3. Exit")

    choice=int(input("choose option: "))
    if choice == 1:
        new_id=input("enter new id: ")
        title=input("enter new task: ")
        new_task_status=input("enter task status: ")
        new_task={"id":new_id,"task":title,"status":new_task_status}
        #func call
        add_task(new_task)
        print("your new task is appended!")

    elif choice == 2:
        print("you task lists: ")
        view_tasks(tasks)

    elif choice == 3:
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