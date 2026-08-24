n = int(input("Enter a number: "))

def sum(n):
    if(n==1):
        return 1 
    return sum(n-1)+n

print(f"The sum of first {n} natural number is {sum(n)}")