def signup():
    with open("user_data.txt" , "a") as f:
        name = input("Enter Your Username: ")
        email = input("Enter Your Email: ")
        password = input("Enter Password: ")
        f.write(name + "," +email + ","+ password + "\n")
        print("Signup was sucessfully done👍")


def login():
    name = input("Enter Your Username: ")
    email = input("Enter Your Email: ")
    password = input("Enter Password: ")
    found = False
    with open("user_data.txt" , "r") as s:
        for line in s:
            stored_data, stored_email,stored_pass = line.strip().split(",")

            if name == stored_data and email == stored_email and password == stored_pass:
                print("Login Sucessfully")
                found = True
                break
        if not found:
            print("❌ Invalid credentials")

# login()
# signup()

while True:
    print("\n1. for signup")
    print("2. for login")
    print("3. for exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        signup()

    elif choice == 2:
        login()
 
    elif choice == 3:
        break

    else:
        print("Invalid Choice")



