'''
a = int(input("Enter your number: "))
b = int(input("Enter your number: "))
c = int(input("Enter your number: "))

average = (a+b+c)/3
print(average)

a = int(input("Enter your number: "))
b = int(input("Enter your number: "))
c = int(input("Enter your number: "))

average = (a+b+c)/3
print(average)

a = int(input("Enter your number: "))
b = int(input("Enter your number: "))
c = int(input("Enter your number: "))

average = (a+b+c)/3
print(average)

def avg():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))

    average = (a+b+c)/3
    print(average)

avg()
avg()
avg()
avg()
avg()
'''


# Function Definition:
def n1():
    for i in range(100):
     if(i== 55):
             break       #  Exit this loop right away
    print(i)


    for i in range(10):
        if(i== 5): 
         continue      #  Skip this iteration
        print(i)
        
    for i in range (9):
        print("Printing")
        if i == 7:
            continue
        print(i)

# Function Call
n1()
n1()
n1()