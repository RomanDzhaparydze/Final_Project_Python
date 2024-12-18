from person import Person 
import pandas as pd
from utils import checkParamIsNumber

class Employee(Person):
    def __init__(self, id=None, name=None, age=None, dict_to_import=None):
        if isinstance(dict_to_import,(pd.Series, pd.DataFrame)):
            super().__init__(dict_to_import["id"], dict_to_import["name"], dict_to_import["age"])
            self._field = dict_to_import["field"]
            self._salary = dict_to_import["salary"]
        else:
            super().__init__(id, name, age)
            self._field = input("Please enter the field of work: ")
            self._salary = checkParamIsNumber("salary")

    def getField(self):
        return self._field
    
    def setField(self, field):
        self._field = field

    def getSalary(self):
        return self._salary
    
    def setSalary(self, salary):
        self._salary = salary

    def printEmployee(self, idx):     
        tab_str = super().printPerson(idx)
        print(tab_str + "Field: " + self.getField())
        print(tab_str + "Salary: " + str(self.getSalary()))

    def printMySelf(self, idx=-1):     
        self.printEmployee(idx)

    def employeeAsDict(self):
        emp_dict = super().personAsDict()
        emp_dict["field"] = self.getField()
        emp_dict["salary"] = self.getSalary()
        emp_dict["type"] = self.__class__.__name__
        return emp_dict

    def mySelfAsDict(self):
        return self.employeeAsDict()

