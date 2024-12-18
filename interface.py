from utils import *
from student import Student
from employee import Employee
from menu import Menu
import pandas as pd
import os
 
def printMenu():
    idx = 1
    for option in Menu:
        print(str(option.value) + ". " + option.name.replace("_", " ").capitalize())
        idx += 1

def saveNewEntry(dict_by_id, list_of_person):
    types_of_person = [Employee, Student]
    try:
        id = checkParamIsNumber("ID")
        if id in dict_by_id:
            print("Error: ID already exists: ", end="")
            print(dict_by_id[id].getName() + " - " + str(dict_by_id[id].getAge()))
            return 0

        name = input("Please enter the name: ")
        age = checkParamIsNumber("age")
    except ValueError as e:
        return 0
    
    for idx, person in enumerate(types_of_person):
        # str_to_print = str(person).replace("<class '", "").replace("'>", "").split(".")[0]
        str_to_print = person.__name__.lower()
        if isvowel(str_to_print[0]):
            articule = "an"
        else:
            articule = "a"
        print("If you are " + articule + " " + str_to_print + " - press " + str(idx))

    type_to_create = None
    while type_to_create not in range(len(types_of_person)):
        type_to_create = input()
        if not type_to_create.isdigit():
            continue
        type_to_create = int(type_to_create)

    person = types_of_person[type_to_create](id, name, age)
    
    dict_by_id[id] = person
    list_of_person.append(person)     
    print("ID [" + str(id) + "] saved successfully")
    return int(age)
    

def searchById(dict_by_id):
    try:
        id = checkParamIsNumber("ID")
    except ValueError as e:
        return
    
    if id in dict_by_id:
        dict_by_id[id].printMySelf()
    else:
        print("Error: ID " + str(id) + " is not saved")


def printAgesAverage(sum_of_ages, list_of_person):
    if len(list_of_person) == 0:
        print("0")
        return
    res = sum_of_ages / len(list_of_person)
    print(str(res))



def printAllNames(list_of_person):
    # why to use iteratore, when we use index any way :)
    for idx in range(len(list_of_person)):
        print(str(idx) + ". " + list_of_person[idx].getName())



def printAllIds(list_of_person):
    for idx in range(len(list_of_person)):
        print(str(idx) + ". " + str(list_of_person[idx].getId()))


def printAllEntries(list_of_person):
    for idx in range(len(list_of_person)):
        list_of_person[idx].printMySelf(idx)



def printEntryByIndex(list_of_person):
    try:
        idx = checkParamIsNumber("Index")
    except ValueError:
        return

    if idx >= len(list_of_person) or idx < 0:
        printIndexErrorOutOfRange(idx, len(list_of_person))
    else:
        list_of_person[idx].printMySelf()

def importData(dict_by_id, list_of_person):
    import_filename = input("What is your input file name? ")
    if not os.path.exists(import_filename):
        print("Error: import file does not exist")
        return 0
    types_of_person = [Employee, Student]
    sum_of_ages = 0
    imported_amount = 0
    with open(import_filename, "r") as f:
        people_df = pd.read_csv(import_filename)
        for idx, dict_to_add in people_df.iterrows():
            for curr_type in types_of_person:
                if dict_to_add["type"]== curr_type.__name__:
                    person = curr_type(dict_to_import=dict_to_add)
                    dict_by_id[person.getId()] = person
                    list_of_person.append(person)
                    sum_of_ages += person.getAge()
                    imported_amount += 1
                    break
                else:
                    print("Invalid type of person: " + dict_to_add["type"])
    print("Succesfully imported " + str(imported_amount) + " entries")
    return sum_of_ages


def saveAllData(list_of_person):
    output_filename = input("What is your output file name? ")

    peolpe_list = []
    for person in list_of_person:
        peolpe_list.append(person.mySelfAsDict())

    people_df = pd.DataFrame(peolpe_list)
    people_df.to_csv(output_filename, index = False)


def exitSystem():
    flag = None
    while flag != "y" and flag != "n":
        flag = input("Are you sure you want to exit? (y/n) ")
    if flag == "y":
        print("Goodbye!")
        exit()