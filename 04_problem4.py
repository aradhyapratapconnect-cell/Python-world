try:
    a = int(input("Enter a number a number: "))
    b = int(input("Enter a number a number: "))
    print(a/b)
except ZeroDivisionError as z:
    print("Infinite")
    
