balance = 300000

def atm():
    global balance

    while True:
        print("\n1. for Check Balance")
        print("2. for Deposit")
        print("3. for Withdraw")
        print("4. for exit")

        choice = int(input("Choose the option for which you want to do: "))

        if choice == 1:
            print("Your Balance is", balance)

        elif choice == 2:
            amount = int(input("Enter the amount to Deposit: "))
            balance += amount
            print("Deposit Sucessfully")

        elif choice == 3:
            amount = int(input("Enter the amount to Withdraw: "))
            if amount <= balance:
                balance -= amount

            else:
                print("Insufficient Amount")

        else:
            break
    

atm()