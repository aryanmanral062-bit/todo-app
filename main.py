tasks=[]

def add_task():
    while True:
        user_input=input("enter your task:").strip()
        if user_input==" ":
            print("Task is empty")
            continue
        tasks.append(user_input)
        print("Task added sucessfully")

        while True:
            continue_choice=input("do you want to cnotinue or not?(yes or no)").lower()
            if(continue_choice=="yes"):
                break
            elif(continue_choice=="no"):
                return
            else:
                print("input input")
                continue_choice=input("do you want to cnotinue or not?(yes or no)").lower()
add_task()

print("\nCurrent Tasks:")
print(tasks)

'''
INPUT WORKFLOW

FUNCTION STARTS
    ↓
OUTER LOOP STARTS
    ↓
take task input
    ↓
strip spaces
    ↓
check empty?

    YES → error message
           ↓
        continue
           ↓
    OUTER LOOP restarts

    NO
    ↓
append task
    ↓
show success message
    ↓
INNER LOOP STARTS
    ↓
ask continue choice
    ↓
convert to lowercase
    ↓
check choice?

    "yes"
        ↓
      break
        ↓
    INNER LOOP ends
        ↓
    OUTER LOOP naturally restarts
        ↓
    ask task again

    "no"
        ↓
      return
        ↓
    ENTIRE FUNCTION ENDS

    invalid input
        ↓
    show error message
        ↓
    INNER LOOP repeats
        ↓
    ask continue choice again'''

def delete_task():
    if not tasks:
        print("No avaialable tasks to delete")
        return
    task_name=input("enter task name to delete").strip()
    if task_name=="":
        print("error")
        return
        
    if task_name in tasks:
        tasks.remove(task_name)
        print("Task deleted sucessfully")
    else:
        print("Task not found")

delete_task()

print("\nupdated Tasks:")
print(tasks)

'''
DELETE Workflow

DELETE TASK WORKFLOW


FUNCTION STARTS
    ↓

check:
is task list empty?
    ↓

YES
    ↓
print:
"No available tasks to delete"
    ↓
return
    ↓
FUNCTION ENDS


NO
    ↓

ask user:
"Enter task name to delete"
    ↓

strip extra spaces
    ↓

check:
is input empty?
    ↓

YES
    ↓
print:
"Task name cannot be empty"
    ↓
return
    ↓
FUNCTION ENDS


NO
    ↓

check:
does task exist in tasks list?
    ↓

YES
    ↓

remove task from list
    ↓

print:
"Task deleted successfully"
    ↓

FUNCTION ENDS


NO
    ↓

print:
"Task not found"
    ↓

FUNCTION ENDS '''

def view_task():
    if not tasks:
        print("there is no current tasks")
        return

    for index,task in enumerate(tasks,start=1):
            print(f"{index}.{task}")

view_task()

'''
VIEW Workflow

view_task() starts
    ↓

check:
if tasks list empty
    ↓

YES
    ↓
show:
"there is no current tasks"
    ↓
return
    ↓
function ends


NO
    ↓

start enumerate loop
    ↓

take:
index + task
one-by-one
    ↓

print:
1. task_name
2. task_name
3. task_name
    ↓

loop ends
    ↓
function ends '''

def main_menu():
    while True:
        print("\n==TODO Menu==")
        print("1. Add tasks")
        print("2. Delete tasks")
        print("3. view tasks")
        print("4. Exit tasks")

        choice=input("enter your chocie:").strip()

        if choice=="1":
            add_task()
        elif choice=="2":
            delete_task()
        elif choice=="3":
            view_task()
        elif choice=="4":
            print("Exiting TODO app. Please select between 1 to 4")

main_menu()

'''
FUNCTION STARTS
    ↓

MAIN LOOP STARTS
    ↓

display menu options
    ↓

take user choice
    ↓

check choice


1
↓
call add_task()
↓
return back to menu


2
↓
call delete_task()
↓
return back to menu


3
↓
call view_task()
↓
return back to menu


4
↓
show exit message
↓
break main loop
↓
APPLICATION ENDS


invalid input
↓
show error message
↓
main loop repeats '''
         

    