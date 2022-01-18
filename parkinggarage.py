class Garage():
    # attributes
    def __init__(self):
        self.tickets = [10]
        self.parkingspots = [10]
        self.curticket = {}
    #    take ticket
    def taketicket(self):
        self.tickets[0] = self.tickets[0] - 1
        print(f"There are {self.tickets} tickets left")
        self.parkingspots[0] = self.parkingspots[0] - 1
        print(f"There are {self.parkingspots} left")
    #    pay for parking
    def payforpark(self):
        fee = input("Please deposit your fee.(10)  ")
        if fee == "10":
            print("Thank you for your payment you now have 15 minutes to leave.  ")
            self.curticket.update({"paid" : True})
        
    #   leave garage
    def leavegarage(self):
        if "paid" in self.curticket:
            print("Thank you have a nice day!  ")     
        else:
            while True:
                latefee = input("Please deposit your late fee now.(15)  ")
                if latefee == "15":
                    print("Thank you have a good day.")
                    break       
        self.tickets[0] = self.tickets[0] + 1
        print(f"There are {self.tickets} tickets left")
        self.parkingspots[0] = self.parkingspots[0] + 1
        print(f"There are {self.parkingspots} left")
    #    methods put together arriving           
    def arrive(self):
        self.taketicket()
        self.payforpark()
        self.leave()
    #    leaving
    def leave(self):
        while True:
            leave = input("Ready to leave?  ")
            if leave == "yes":
                self.leavegarage()
                break
            else:
                print("Enter 'yes' when you are ready to exit.")
            
user = Garage()
user.arrive()





