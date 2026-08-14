class employee:
    def __init__(self):
        print("Constructor of employee")        
    a = 1

class programmer(employee):
    def __init__(self):
        print("Constructor of programer")
    b = 23

class manager(programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of manager")
    c = 45

# o = employee()
# print(o.a) 

# p = programmer()
# print(p.a, p.b)

x = manager()
print(x.a,x .b,x.c)