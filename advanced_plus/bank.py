# python banking program

def show_balance(balance):
    print("***********************")
    print(f"Your balance is: ${balance:.2f}")
    print("***********************")

def deposit():
    print("********************")
    amount = float(input("Enter an amount to be deposited: "))
    print("********************")
    if amount < 0:
        print("**************************")
        print("That's not a valid amount!")
        print("**************************")
        return 0
    else:
        print("************************************")
        print(f"You have successfully deposited: ${amount}")
        print("************************************")
        return amount

def withdraw(balance):
    print("********************")
    amount = float(input("Enter amount to be withdraw: "))
    print("********************")
    if amount > balance:
        print("******************")
        print("Insufficient funds")
        print("******************")
        return 0
    elif amount < 0:
        print("*********************************")
        print("Amount must be greater than zero.")
        print("*********************************")
        return 0
    else:
        print("************************************")
        print(f"You have successfully withdraw: ${amount}")
        print("************************************")
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("***************")
        print("Banking Program")
        print("***************")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("***************")
     
        print("***************")
        choice = input("Enter your choice (1-4): ")
        print("***************")
        
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("***************************")
            print("That is not a valid choice!")
            print("***************************")

    print("***************************")
    print("Thank you! Have a nice day!")
    print("***************************")

if __name__ == '__main__':
    main()