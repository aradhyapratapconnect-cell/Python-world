def gree1():
    print("Good night user")

a = int(input("Enter Your Age: "))

if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("Invalid Age")

elif(a==0):
    print("0 is not a valid age") 


else:
    print("You are below the age of consent")   

gree1()