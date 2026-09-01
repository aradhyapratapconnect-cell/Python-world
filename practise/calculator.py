print("1. for Add")
print("2. for Subtract")
print("3. for Multiply")
print("4. for Divide")

choice = int(input("Enter the choice:"))

a = int(input("Enter the number:"))
b = int(input("Enter the number:"))

if choice == 1:
    print(a+b)

elif choice == 2:
    print(a-b)

elif choice == 3:
    print(a*b)

elif choice == 4:
    print(a/b)

else:
    ("Invalid Choice")

