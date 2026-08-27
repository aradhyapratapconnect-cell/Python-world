a = int(input("There entre first number: "))
b = int(input("There entre second number: "))

if(b == 0):
    raise ZeroDivisionError("Hey, there our program is not meant to divide numbers by zero(0)")
else:
    print(f"The division a/b is {a/b}")