# n = int(input("Enter a Number: "))

# for i in range(2,n):
#     if(n%i) == 0:
#         print("This number is not a prime number")
#         break
# else:
#     print("This number is a prime number")    



n = int(input("Enter a no.: "))
for i in range(2,n):
    if(n%i) == 0:
        print(" not Prime")
        break 
 
else:
    print(" prime")

