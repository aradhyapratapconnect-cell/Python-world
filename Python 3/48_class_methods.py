class nonu:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")


e = nonu()
e.a = 45
e.show()