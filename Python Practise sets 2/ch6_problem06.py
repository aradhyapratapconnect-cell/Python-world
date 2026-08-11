marks = int(input("Enter Your Marks:"))

if(marks<=100 and marks>=90):
    print("Your Grade is Ex,", marks)
elif(marks<=90 and marks>=80):
    print("Your Grade is A,", marks)
elif(marks<=800 and marks>=70):
    print("Your Grade is B,", marks)
elif(marks<=70 and marks>=60):
    print("Your Grade is C,", marks)    
elif(marks>=50 ):
    print("Your Grade is F,", marks)    
