class employee:
    language = "Python"  
    salary = 1000000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good Morning,\n\tBuggu the Coder.")



buggu = employee()
buggu.language = "JavaScript"
# print(buggu.language, buggu.salary)
buggu.salary = 1234567890


# employee.getInfo(buggu)
buggu.greet()
buggu.getInfo() 