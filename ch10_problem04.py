from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

        
    def book(self,fro,to):
        print(f"The ticket booked in train no: {self.trainNo} from {fro} to {to} ")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time ")

    def getFare(self,fro,to):
        print(f"The ticket fare for train no: {self.trainNo} from {fro} to {to} is ₹ {randint(50,5000)} only")

t = Train(2524)
t.book("Dhampur", "Bangaluru")
t.getStatus()
t.getFare("Dhampur", "Bangaluru")