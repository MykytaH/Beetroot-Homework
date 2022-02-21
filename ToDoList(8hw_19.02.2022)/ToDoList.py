import func as f

tasks = []
ids = []
status = (
        "pending",
        "in progress",
        "done"
)
while True:
    print("ToDo list functions:\n"
          "\t1 - Create new task\n"
          "\t2 - View a list of tasks\n"
          "\t3 - View task details\n"
          "\t0 - Exit")
    navigator = int(input("Enter the number of the function you want to go to: "))

    if navigator == 1:
        new_task = {
            "id": f.get_task_id(tasks),
            "title": f.get_title(),
            "descr": f.get_description(),
            "status": status[0],
            "priority": f.get_priority(),
            "due_date": f.get_date()
        }
        ids.append(f.get_task_id(tasks))
        tasks.append(new_task)

    elif navigator == 2:
        for task in tasks:
            print(f"{task.get('id')}. {task.get('title')} - {task.get('status')}")

    elif navigator == 3:
        while True:
            input_id = int(input("Enter the desired task id: "))
            if input_id not in ids:
                print("There is no task with that id!")
            else:
                for task in tasks:
                    if task.get('id') == input_id:
                        print(task)
                        break

    elif navigator == 0:
        print("Good bye")
        break

    else:
        print("You can only enter int 0 - 4 to select a function!")

