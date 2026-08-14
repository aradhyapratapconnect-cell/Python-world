'''
class programmer:
    company = "Ultron "
    def show(self):
        print(f"The  name is {self.name} and the salary is {self.salary}")

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")
'''


class employee:
    company = "Kyzin.AI"
    salary = 1234567
    name = "Buggu"
    def show(self):
        print(f"The  name of the employee is {self.name} and the salary is {self.salary}")

class coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all language your language is: {self.language}")

class programmer(employee,coder):
    company = "Kyzin.AI "
    def showLanguage(self):
        print(f"The commpany name is {self.company} and he is good with {self.language} language")

b = programmer()
b.show()
b.printLanguage()

b.showLanguage()
