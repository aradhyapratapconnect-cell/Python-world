class complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i

    def __add__(self,c2) -> complex:
        return complex(self.r + c2.r,self.i + c2.i)
    
    def __str__(self):
        return f"{self.r} + {self.i}"

c1 = complex(133, 39)
c2 = complex(234, 3983)
print(c1 +c2)