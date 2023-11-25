def check_bal(balance):
    print("The current balance is", balance)

def deposit_bal(balance):
    depositBal=int(input("enter an amount to deposit"))
    balance= balance +depositBal
    print("The current balance is", balance)

def withDraw_bal(balance):
    withDrawAmount=int(input("enter an amount to with draw from the ATM"))
    if(withDrawAmount<=balance):
        balance=balance-withDrawAmount
        print(f"The current balance is {balance}")
    else:
        print(f"Enter an amount less than {balance}")


def main():
    pin=12345
    balance= int(input("Enter an amount"))

    print("----- PLEASE INSERT YOUR CARD -----")
    choice=3
    
   
    while choice>0:
        choice = choice-1
        confirm_pin=int(input("verify the pin"))
        if pin == confirm_pin:
            choice=0
            print("verified pin successfully")
            while True:
                print("""
                    1. CHECK BALANCE
                    2. DEPOSIT BALANCE
                    3. WITHDRAW BALANCE
                    4. EXIT
                            """)
                option=int(input("enter an 1 to check balance/2 to deposit balance/3 to withdraw balance/4 to exit"))
                if option == 1:
                    check_bal(balance)
                elif option == 2:
                    deposit_bal(balance)
                elif option == 3:
                    withDraw_bal(balance)
                else:
                    return False
                    print("Transaction has beed ended")
        else:
            print(f"You have Entered wrong pin, Remaining choices you have {choice}")
        
    print("Transaction has been completed successfully")

if __name__ == "__main__":
    main()


