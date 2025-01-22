import Alias.al_calculator_functions as calc  # importing with alias

def calculator():
    print("Welcome to the Python Calculator!")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Square root (√)")
    print("7. Factorial (!)")
    print("8. Exit")

    while True:
        choice = input("\nEnter the operation number (1-8): ")
        
        if choice == "8":
            print("Exiting calculator. Goodbye!")
            break
        
        if choice in ["1", "2", "3", "4", "5"]:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == "1":
                print(f"Result: {calc.add(num1, num2)}")  # using alias calc
            elif choice == "2":
                print(f"Result: {calc.subtract(num1, num2)}")
            elif choice == "3":
                print(f"Result: {calc.multiply(num1, num2)}")
            elif choice == "4":
                print(f"Result: {calc.divide(num1, num2)}")
            elif choice == "5":
                print(f"Result: {calc.power(num1, num2)}")
        
        elif choice == "6":
            try:
                num = float(input("Enter the number: "))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                continue
            print(f"Result: {calc.sqrt(num)}")
        
        elif choice == "7":
            try:
                num = int(input("Enter an integer: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
                continue
            print(f"Result: {calc.factorial(num)}")
        
        else:
            print("Invalid operation. Please select a number between 1 and 8.")

if __name__ == "__main__":
    calculator()
