class bikeShop:
    def __init__(self,stock):
        self.stock=stock
    def displayBkike(self):
        print("Total bikes",self.stock)
    def rentForBike(self,q):
        if q<=0:
            print("Enter the positive value or greater then zero")
        elif q>self.stock:
            print("Enter the value (less then stock)")
        else:
            self.stock=self.stock-q
            print("Total price",q*100)
            print("Total Bikes",self.stock)

obj=bikeShop(200)
while True:
    uc=int(input('''
    1 Display Stocks
    2 Rent a Bike
    3 Exit
    '''))
    if uc==1:
        obj.displayBkike()
    elif uc==2:
        n=int(input("Enter the Qty:-"))
        obj.rentForBike(n)
    else:
        break
