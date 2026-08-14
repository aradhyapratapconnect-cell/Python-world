'''
class employee:
    name = "Buggu"
    language = "Py"
    salary = 1000000

nemu = employee()
print(nemu.name, nemu.salary)
'''

class employee:
    language = "Python"  
    salary = 1000000

buggu = employee()
buggu.name = "Buggu"
print(buggu.name,buggu.language, buggu.salary)

Dev = employee()
Dev.name = "Dev the ashiq"
print(Dev.name,Dev.salary, Dev.language)


'''
Here name is instance attribute and salary and language Are
class attributes as they directly belong to the class
'''