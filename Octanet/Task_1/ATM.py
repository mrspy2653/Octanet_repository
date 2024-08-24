print("*********WELCOME TO ATM MACHINE********")
print("1. Balance Enquiry")
print("2. Cash Withdrawal")
print("3. Change Pin")
print("4. Cash Deposit")
print("5. Exit")
user_inp = int(input("choose the Option : "))


def option(user_inp):
    balance = 4000
    pinn = 2322
    match user_inp:
        case 1:
            print(f"Your Balance is : ₹{balance}")
        case 2:
            print("*********CASH WITHDRAWAL********")
            print("Enter withdrawal Amount: ")
            amt = int(input())
            print("Enter your Pin: ")
            pin = int(input())
            if pin == pinn:
                if amt > balance:
                    print("Insufficient Funds")
                else:
                    print("Withdrawal Success")
                    balance -= amt
                    print(f"Balance after Money Withdrawal: ₹{balance}")
            else:
                print("Incorrect Pin")
        case 3:
            print("*********PIN CHANGE********")
            print("Enter Previous Pin")
            change_pin = int(input())
            if pinn == change_pin:
                print("Enter New Pin")
                new_pin = int(input())
                print("Enter Again")
                ag_pin = int(input())
                if new_pin == ag_pin:
                    pinn = new_pin
                    print("Pin Updated Successfully")
                else:
                    print("Enter same as New Pin")
            else:
                print("Incorrect Previous Pin")
        case 4:
            print("*********CASH DEPOSIT********")
            print("Enter Deposit Balance")
            dp_bal = int(input())
            print("Enter Pin")
            dp_pin = int(input())
            if pinn == dp_pin:
                print("Cash Deposited Sucessfully")
                balance += dp_bal
                print(f"Total Balance: ₹{balance}")
            else:
                print("Entered Incorrect Pin")
        case 5:
            print("Exited Sucessfully")
        case _:
            print("Invalid Option")






option(user_inp)