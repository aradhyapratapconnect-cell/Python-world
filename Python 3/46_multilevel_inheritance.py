class employee:
    a = 1

class programmer(employee):
    b = 23

class manager(programmer):
    c = 45

o = employee()
print(o.a) #Prints the a attribute
# print(o.b) shows an error as there is no b attribute in employee class

p = programmer()
print(p.a, p.b)

x = manager()
print(o.a,p.b,x.c)