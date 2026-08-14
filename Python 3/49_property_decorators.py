class nonu:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname} {self.wname}"
    
    @name.setter
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
        self.wname = value.split(" ")[2]
e = nonu()
e.a = 45
e.name = "Buggu Pratap Singh"
# print(e.name)
print(e.fname,e.lname,e.wname)
e.show()