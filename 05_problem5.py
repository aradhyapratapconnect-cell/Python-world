a = int(input("Enter a number a number: "))

table = [a*i for i  in range(1,11)]
with open ("Tables.txt", "a") as f:
    f.write(f"Table of {a} is: {str(table)} \n")
