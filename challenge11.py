#Challenge 11: Order to do list

# This program lets the user pick off items from a todo list. Some items needs to be picked off before others

from typing import List

#Class used to represent an entry in a list. The dependencies are the items in the todo list that is needed to be done first
class to_do_list_item():
    def __init__(self, task: str, *dependencies: int):
        self.task = task
        self.dependencies = list(dependencies)

    #This item is used to define what other tasks are needed to be done before this task
    def add_dependencies(self, *depndencies: int):
        for i in depndencies:
            self.dependencies.append(i)
    
    #This makes the list item independent from all other to do tasks
    def clear_dependency(self):
        self.task = "✅"
        self.dependencies = []

#Check if all the dependencies (items that needs to be checked off first) are cleared
def check_for_independencies(dependencies_list: List[to_do_list_item], item: int) -> bool:
    for elem in dependencies_list[item].dependencies:
        if dependencies_list[elem].task != "✅":
            return False
        
    return True

#Check if the to do list is cleared
def check_if_clear(dependencies_list: List[to_do_list_item]):
    for elem in dependencies_list:
        if elem.task != "✅":
            return False
    return True

#Print the to do list
def print_list(dep_arr: to_do_list_item):
    print()
    for index, elem in enumerate(dep_arr):
        print(f"{index + 1}. {elem.task}")
    print()
    
#This is the to do list input (Can be modified together with the add_dependencies part below)
to_do_list_arr = ["Eat breakfast", "Make Toast", "Shower", "Brush Teeth", "Get dressed", "Go to work"]

#This part converts the to do list items into objects of the to_do_list_item class
to_do_list = []
for task in to_do_list_arr:
    to_do_list.append(to_do_list_item(task))

print_list(to_do_list)

#This part is defining what items are needed to be done before other items (Can be modified together with the initiatation of to_do_list_arr above)
to_do_list[0].add_dependencies(1) #The second task must be done before the first task
to_do_list[3].add_dependencies(2) #The third task must be done before the 4th task
to_do_list[4].add_dependencies(2) #The third task must be done before the 5th task
to_do_list[5].add_dependencies(0, 1, 2, 3, 4) #All other tasks must be done before going to work

#Loop until full to do list is cleared
while(True):

    #Controlled user input (valid inputs are numbers 1-6)
    while(True):
        user_input = input("What task do you want to check off? (1-6): ")
        if not user_input.isdigit() or int(user_input) not in [i for i in range(1, len(to_do_list) + 1)]:
            print("\nInvalid input\n")
        else:
            break

    #Parsing input to int
    user_input = int(user_input)

    #Select the to do task that is to be cleared off
    to_do_item = to_do_list[user_input - 1]

    #Clear off item if no other tasks are needed to be done first
    if to_do_item.task == "✅":
        print("Task already done!")
    elif not check_for_independencies(to_do_list, user_input - 1):
        print(f"\nFirst you must do the following tasks: {[to_do_list[i].task for i in to_do_item.dependencies if to_do_list[i].task !="✅"]}")
    else:
        print("\nChecking off task")
        to_do_list[user_input - 1].clear_dependency()

    print_list(to_do_list)

    #Exit program when all tasks are done
    if check_if_clear(to_do_list):
        print("\n✨All tasks done!✨\n")
        exit()
