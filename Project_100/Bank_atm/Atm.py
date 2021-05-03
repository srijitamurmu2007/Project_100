class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your balance is 50000")

    def withdrawal(self,amount):
        new_amount = 50000 - amount
        print("You have withdrawn amount "+str(amount) +".Your remaining balance is "+str(new_amount))

def main():
    Card_Number = input("Insert your card number:- ")
    Pin_Number = input("Insert your pin:- ")

    new_user = Atm(Card_Number, Pin_Number)

    print("Choose your activity")
    print("1.Balance Enquiry    2.Cash Withdrawal")
    activity = int(input("Enter activity number:-"))

    if (activity == 1):
        new_user.check_balance()
    elif (activity ==2):
        amount = int(input("Enter the amount:- "))
        new_user.withdrawal(amount)
    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()