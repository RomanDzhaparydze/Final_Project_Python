from utils import *
from interface import *

dict_by_id = {}
list_of_person = list()
sum_of_ages = 0
error_indicator = False

while True:
    error_indicator = False
    choise = None
    printMenu()
    try:
        try:
            choise_input = input("Please enter your choise: ")
            choise = int(choise_input)
        except ValueError:
            choise = choise_input
        
        if choise == Menu.SAVE_NEW_ENTRY.value:
            age = saveNewEntry(dict_by_id, list_of_person)
            sum_of_ages += age
        elif choise == Menu.SEARCH_BY_ID.vlue:
            searchById(dict_by_id)
        elif choise == Menu.PRINT_AGES_AVERAGE.value:
            printAgesAverage(sum_of_ages, list_of_person)
        elif choise == Menu.PRINT_ALL_NAMES.value:
            printAllNames(list_of_person)
        elif choise == Menu.PRINT_ALL_IDS.value:
            printAllIds(list_of_person)
        elif choise == Menu.PRINT_ALL_ENTRIES.value:
            printAllEntries(list_of_person)
        elif choise == Menu.PRINT_ENTRY_BY_INDEX.value:
            printEntryByIndex(list_of_person)
        elif choise == Menu.IMPORT_DATA_FRAME.value:
            sum_of_ages += importData(dict_by_id, list_of_person)
        elif choise == Menu.SAVE_ALL_DATA.value:
            saveAllData(list_of_person)
            continue
        elif choise == Menu.EXIT.value:
            exitSystem()
        else:
            print("Error: Option [" + choise + "] does not exists. Please try again")
            error_indicator = True
            continue
    except KeyboardInterrupt:
        print("Error: to finish the program, please choose " + str(Menu.EXIT.value) +" in the main menu")
    finally:
        try:
            if (choise != Menu.EXIT.value) and (not error_indicator):
                holder = input("Press enter to continue ")
        except KeyboardInterrupt:
            print("\nError: to finish the program, please choose " + str(Menu.EXIT.value) +" in the main menu")
            continue

       
    