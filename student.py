from person import Person
from utils import checkParamIsNumber

class Student(Person):
    def __init__(self, id, name, age):
        super().__init__(id, name, age)
        self._field = input("Please enter the field of study: ")
        self._year = checkParamIsNumber("year of study")
        self._avg = checkParamIsNumber("average score", float_value=True)
    
    def getField(self):
        return self._field
    
    def setField(self, field):
        self._field = field

    def getYear(self):
        return self._year
    
    def setYear(self, year):
        self._year = year

    def getAvg(self):
        return self._avg
    
    def setAvg(self, avg):
        self._avg = avg

    def printStudent(self, idx):
        tab_str = super().printPerson(idx)
  
        print(tab_str + "Field: " + self.getField())
        print(tab_str + "Year of study: " + str(self.getYear()))
        print(tab_str + "Average score: " + str(self.getAvg()))
    
    def printMySelf(self, idx=-1):
        self.printStudent(idx)

    def studentAsDict(self):
        stud_dict = super().personAsDict()
        stud_dict["field"] = self.getField()
        stud_dict["year of study"] = self.getYear()
        stud_dict["average score"] = self.getAvg()
        return stud_dict
    
    def mySelfAsDict(self):
        return self.studentAsDict()