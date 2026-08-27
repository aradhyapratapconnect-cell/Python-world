class TwoDVector:
    def __init__(self,i,j):
        self.i = i 
        self.j = j
    
    def show(self):
        print(f"The Vector is {self.i} i + {self.j} j")

class ThreeDVector(TwoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k

    def show(self):
        print(f"The Vector is {self.i} i + {self.j} j + {self.k} k")

o = TwoDVector(18,45)
o.show()
p = ThreeDVector(18,45,7)
p.show()