list1 = [14,64,35,77,245,45]

def div(n,):
    if(n%7 == 0):
        return True
    return False

filr = list(filter(div,list1))
print(filr)