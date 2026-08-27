class employee():
    salary = 123
    increment = 22

    @property
    def salaryAfterIncrement(self):
        return(self.salary + self.salary *(self.increment/100))

    @salaryAfterIncrement.setter
    def salaryAfterincrement(self,salary):
        self.increment = ((salary/self.salary)-1)*100


e = employee()
# print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 123
print(e.increment)