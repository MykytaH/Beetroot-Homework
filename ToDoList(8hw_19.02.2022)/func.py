import datetime


def get_task_id(tasks):
    try:
        return tasks[-1].get("id") + 1
    except:
        return 1


def get_title():
    while True:
        title = input("Write here the task title: ")
        if len(title) > 60:
            print("Title must be no longer 60 symbols!")
        elif len(title) == 0:
            print("Title is a required field!")
        else:
            return title


def get_description():
    return input("Write here the description of your task: ")


def get_priority():
    while True:
        priority_list = [i + 1 for i in range(10)]

        priority = input("Write here the task priority (from 1 to 10): ")
        try:
            if int(priority) not in priority_list:
                print("Priority must be integer number from 1 to 10!")
            else:
                return priority
        except:
            print("Priority must be integer number from 1 to 10!")


def get_date():
    while True:
        due_date = input("Write here when your task must be complete: ")
        try:
            date_check = datetime.datetime.strptime(due_date, "%d.%m.%Y")
            return due_date
        except:
            print("Error date! Date format must be dd.mm.yyyy!")


