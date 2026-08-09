a = int(input("Enter Your Age: "))


# IF statement no.:1
if(a%2 ==0):
    print("a is Even")
# End of if statement: 1


# IF statement no.:2
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("Invalid Age")

elif(a==0):
    print("0 is not a valid age") 


else:
    print("You are below the age of consent")    

# End of if statement: 2

print("Have a Nice Day!")    