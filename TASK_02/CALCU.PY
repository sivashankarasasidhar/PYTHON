class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "not allow"
        return x / y

def main():
    calculator = Calculator()

    while True:
        print("Options:")
        print("1. Add")
        print("2. Sub")
        print("3. Mul")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter 1,2,3,4")

        if choice == "5":
            print("nothing")
            break

        if choice in ["1", "2", "3", "4"]:
            num1 = float(input("Enter first number"))
            num2 = float(input("Enter second number"))

            if choice == "1":
                result = calculator.add(num1, num2)
                operator = "+"
            elif choice == "2":
                result = calculator.subtract(num1, num2)
                operator = "-"
            elif choice == "3":
                result = calculator.multiply(num1, num2)
                operator = "*"
            elif choice == "4":
                result = calculator.divide(num1, num2)
                operator = "/"

            print(f"Result: {num1} {operator} {num2} = {result}")
        else:
            print("Invalid enter valid 1,2,3,4")

if __name__ == "__main__":
    main()
