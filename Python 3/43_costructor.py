class employee:
    language = "Python"  
    salary = 1000000

    def __init__(self, name,salary,language):# Dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I'am Buggu the coder") 
    


    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good Morning,\n\tBuggu the Coder")

buggu = employee
buggu.greet()
buggu = employee("Buggu" , 1234567890, "Java")
# buggu.name = "Bhoomick Pratap Singh"
print(buggu.name, buggu.salary , buggu.language)
# buggu.getInfo()

