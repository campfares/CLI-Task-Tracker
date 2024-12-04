import json
import random
from colorama import Fore , Back , Style , init
import os

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

# the databse to deal with data and put it into file
data_base = [{ "task":"do home work", "id":30, "status":"in progress"},{ "task":"do home work", "id":10, "status":"done"}]
# y = json.dumps(data_base)
# data_base_file = open("data_base.json","a")
# data_base_file.write(y)
# data_base_file.close

# --------------------------------------------------
class Operations :
    def __init__(self) :
        self.task = ""
        self.id = int()
        self.status = ""

    def add_operation(self) :
        task = input("what task do you want add : ")
        self.id = random.randrange(0,100)
        while True :
            status = input("choose the status of the task (to do , in progress , done ) : ")
            self.task = task
            if status == "to do" or status == "in progress" or status == "done" :
                self.status = status
                data_base.append({"task":{self.task}, "id":{self.id}, "status":{self.status}})
                print('the task add successfully')
                break
            print("invalid choice")

    def remove_operation(self):
        while True :
            end = False
            item_to_remove = input("please write the (id) of the item : ")
            for x in data_base:
                if x["id"] == int(item_to_remove) :
                    data_base.remove(x)
                    print("the item removed successfully")
                    print(data_base)
                    end = True
                    break
            if end == True :
                break
            else:
                print("there is task have this id please check again")

    def update_operation(self) :
        i = 0
        while True :
            update =int(input("please enter the id of the task : "))
            if data_base[i]["id"] == update :
                clear_screen()
                print(Fore.WHITE + "--------------------------------------------------------")
                print(f'| {Fore.GREEN + "task"} | {Fore.WHITE+data_base[i]["task"]} | {Fore.BLUE + "status" } | { Fore.GREEN + data_base[i]["status"] if data_base[i]["status"] == "done" else Fore.RED + data_base[i]["status"] } | {Fore.RED + "id"} | {data_base[i]["id"]} |')
                print(Fore.WHITE + "--------------------------------------------------------")
                init(autoreset=True)
                new_task = input("the new task : ")
                new_staus = input("enter the new status : ")
                data_base[i]["task"] = new_task
                data_base[i]["status"] = new_staus
                i += 1
                break
            print("there no item with this id")

    def mark_as_done():
        i = 0
        while True :
            mark_as_done =int(input("please enter the id of the task : "))
            if data_base[i]["id"] == mark_as_done :
                clear_screen()
                print(Fore.WHITE + "--------------------------------------------------------")
                print(f'| {Fore.GREEN + "task"} | {Fore.WHITE+data_base[i]["task"]} | {Fore.BLUE + "status" } | { Fore.GREEN + data_base[i]["status"] if data_base[i]["status"] == "done" else Fore.RED + data_base[i]["status"] } | {Fore.RED + "id"} | {data_base[i]["id"]} |')
                print(Fore.WHITE + "--------------------------------------------------------")
                init(autoreset=True)
                data_base[i]["status"] = "done"
                i += 1
                break
            print("there no item with this id")

    def mark_as_inprogress():
        i = 0
        while True :
            mark_as_inprogress =int(input("please enter the id of the task : "))
            if data_base[i]["id"] == mark_as_inprogress :
                clear_screen()
                print(Fore.WHITE + "--------------------------------------------------------")
                print(f'| {Fore.GREEN + "task"} | {Fore.WHITE+data_base[i]["task"]} | {Fore.BLUE + "status" } | { Fore.GREEN + data_base[i]["status"] if data_base[i]["status"] == "done" else Fore.RED + data_base[i]["status"] } | {Fore.RED + "id"} | {data_base[i]["id"]} |')
                print(Fore.WHITE + "--------------------------------------------------------")
                init(autoreset=True)
                data_base[i]["status"] = "in progress"
                i += 1
                break
            print("there no item with this id")

class Show :
    def show_tasks(self):
        clear_screen()
        i = 0
        while i<= len(data_base) - 1: 
            print(Fore.WHITE + "--------------------------------------------------------")
            print(f'| {Fore.GREEN + "task"} | {Fore.WHITE+data_base[i]["task"]} | {Fore.BLUE + "status" } | { Fore.GREEN + data_base[i]["status"] if data_base[i]["status"] == "done" else Fore.RED + data_base[i]["status"] } | {Fore.RED + "id"} | {data_base[i]["id"]} |')
            i += 1
            init(autoreset=True)

    def list_on_status_done(self) :
        i= 0
        while i <= len(data_base)-1 :
            if data_base[i]["status"] == "done" :
                print(Fore.WHITE + "--------------------------------------------------------")
                print(f'| {Fore.GREEN + "task"} | {Fore.WHITE+data_base[i]["task"]} | {Fore.BLUE + "status" } | { Fore.GREEN + data_base[i]["status"] if data_base[i]["status"] == "done" else Fore.RED + data_base[i]["status"] } | {Fore.RED + "id"} | {data_base[i]["id"]} |')
                break
        i += 1

    def list_on_status_inprogress(self) :
        i= 0
        while i <= len(data_base)-1 :
            if data_base[i]["status"] == "in progress" :
                print(Fore.WHITE + "--------------------------------------------------------")
                print(f'| {Fore.GREEN + "task"} | {Fore.WHITE+data_base[i]["task"]} | {Fore.BLUE + "status" } | { Fore.GREEN + data_base[i]["status"] if data_base[i]["status"] == "done" else Fore.RED + data_base[i]["status"] } | {Fore.RED + "id"} | {data_base[i]["id"]} |')
                break
        i += 1
    
    def list_on_status_todo(self) :
        i= 0
        while i <= len(data_base)-1 :
            print(Fore.WHITE + "--------------------------------------------------------")
            if data_base[i]["status"] == "to do" :
                print(f'| {Fore.GREEN + "task"} | {Fore.WHITE+data_base[i]["task"]} | {Fore.BLUE + "status" } | { Fore.GREEN + data_base[i]["status"] if data_base[i]["status"] == "done" else Fore.RED + data_base[i]["status"] } | {Fore.RED + "id"} | {data_base[i]["id"]} |')
                break
        i += 1

class Menu :
    def display_menu () :
        print ("welcome to cli task tracker")
        print('''
        1. add : to add new task
        2. update (the number of task) : to update task data
        3. delete (the number of task) : to delete task
        4. list : Listing all tasks
        5. mark-in-progress (the number of task) : Marking a task as in progress
        6. mark-done (the number of task) : Marking a task as done
        7. list done
        8. list todo
        9. list in-progress
        ''')
        while True :
            menu_choice =  input ("inter your choice : ")
            if int(menu_choice) < 10 and int(menu_choice) > 0 :
                break
            print('invaild choice')

class the_application:
    def __init__(self) -> None:
        self.menu = Menu
        self.show = Show
        self.operation = Operations

    def start(self) :
        self.menu.display_menu()


start_the_application = the_application()
start_the_application.start()