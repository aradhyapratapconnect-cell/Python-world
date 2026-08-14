'''
class programmer:
    company = "Ultron "
    def show(self):
        print(f"The  name is {self.name} and the salary is {self.salary}")

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")
'''


class employee:
    salary =123456789
    language =  "Python"
    company = "Kyzin.AI"
    def show(self,name,salary,language):
        self.name = name
        self.salary = salary
        self.language = language
        print(f"The  name of the employee is {self.name} and the salary is {self.salary}")

class programmer(employee):
    company = "Ultron "
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = employee()
b = programmer()
print(a.salary,a.language)
print(a.company , b.company)