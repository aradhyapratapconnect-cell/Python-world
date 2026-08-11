marks1 = int(input("Enter Marks1: "))
marks2 = int(input("Enter Marks2: "))
marks3 = int(input("Enter Marks3: "))

total_percentage = (100*(marks1 + marks2 + marks3 ))/300


print("Your Percentage is", total_percentage)


if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed")

else:
    print("YOu are failed ")    