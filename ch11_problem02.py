class animals:
    pass

class pets(animals):
    pass

class dog(pets):
    @staticmethod
    def bark():
        print("BHaw Bhaw")

d = dog()
d.bark()