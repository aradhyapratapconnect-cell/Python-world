def main():


    try:
        a = int(input("Hey, There entre a number: "))
        print(a)
        return
    
    except Exception as e:
        print(e)
        return
    
    finally:
        print("Yoo, i am inside finally")


main()