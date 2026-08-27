try:
    a = int(input("Hey, There entre a number: "))
    print(a)

except ValueError as v:
    print(v)

except Exception as e:
    print(e)

print("Try again")  