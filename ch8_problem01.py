a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

def greatest(a,b,c):
    if(a>b and a>c):
        return a 
    elif(b>a and b>c):
        return b
    elif(c>a and c>a):
        return c
    

print("Greatset numbers is:", greatest(a,b,c))