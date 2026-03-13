balance = 0

while True:
    print("\n1 Deposit")
    print("2 Withdraw")
    print("3 Check Balance")
    print("4 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        balance += amount
        print("Deposited successfully")

    elif choice == "2":
        amount = float(input("Enter amount: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    elif choice == "3":
        print("Balance:", balance)

    elif choice == "4":
        break
