name = input("Enter Your Name: ")
marks = int(input("Enter Your Marks: "))
phone_number = (input("Enter Your Phone Number: "))

a ="The name of the student is {}, marks are {} and phone number is {}".format(name,marks,phone_number)
print(a)


if len(phone_number) <10:
    print("Invalid Phone Number")

elif len(phone_number) >10:
    print("Invalid Phone Number")

elif len(phone_number) == 10:
    pass

if not phone_number.isdigit():
    print("Phone number must contain only digits ❌")
