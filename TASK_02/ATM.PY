class ATM:
    def __init__(self, balance=0):
        self.ac_bal = balance

    def check_bal(self):
        return self.ac_bal

    def deposit(self, amount):
        if amount > 0:
            self.ac_bal += amount
            return f"Deposit{amount}. New balance:{self.a_b}"
        else:
            return "invalid amount"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.ac_bal:
            self.account_balance -= amount
            return f"Withdrew{amount} New balance{self.ac_bal}"
        elif amount <= 0:
            return "Invalid withdrawal amount"
        else:
            return "Insufficient money"

def main():
    atm = ATM(5000)

    while True:
        print("\nATM Menu:")
        print("1.Check Bal")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice = input("Select an option (1/2/3/4): ")

        if choice == "1":
            print(f"Current balance{atm.check_bal()}")
        elif choice == "2":
            amount = float(input("Enter the deposit amount"))
            print(atm.deposit(amount))
        elif choice == "3":
            amount = float(input("Enter the withdrawal amount"))
            print(atm.withdraw(amount))
        elif choice == "4":
            print("Tanku for using ATM")
            break
        else:
            print("Invalid Pls enter a valid 1,2,3,4")

if __name__ == "__main__":
    main()
