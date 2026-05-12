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
print(tasks)

'''
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