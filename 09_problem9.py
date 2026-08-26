from functools import reduce

list1 = [14,64,35,77,245,45]

def greater(a,b):
    if (a>b):
        return a
    return  b

grf = (reduce(greater,list1))
print(grf)