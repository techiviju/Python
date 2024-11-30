# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.
from random import randint

class Train:
    def __init__(self,trainNo):
        self.trainNo=trainNo

    def book(self,fro,to):
        print(f"Your Ticket is bookd in Train No {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Your train number is {self.trainNo} runing on time")

    def fare(self,fro,to):
        print(f"Ticket Fare in train No {self.trainNo} from {fro} to {to} is {randint(1200 , 5555)}")

T=Train(12564)
T.book("Chandrapur","Hydrabad")

T.getStatus()

T.fare("Chandrapur","Hydrabad")