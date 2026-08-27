from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

        
    def book(slf,fro,to):
        print(f"The ticket booked in train no: {slf.trainNo} from {fro} to {to} ")

    def getStatus(slf):
        print(f"Train no: {slf.trainNo} is running on time ")

    def getFare(slf,fro,to):
        print(f"The ticket fare for train no: {slf.trainNo} from {fro} to {to} is ₹ {randint(50,5000)} only")

t = Train(2524)
t.book("Dhampur", "Bangaluru")
t.getStatus()
t.getFare("Dhampur", "Bangaluru")