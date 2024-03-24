# calculator.py

from calculations.addition import Addition
from calculations.subtraction import Subtraction
from calculations.multiplication import Multiplication
from calculations.division import Division

def main():
    print("Welcome to Calculator App")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = Addition(num1, num2).add()
        print("Result:", result)
    elif choice == '2':
        result = Subtraction(num1, num2).subtract()
        print("Result:", result)
    elif choice == '3':
        result = Multiplication(num1, num2).multiply()
        print("Result:", result)
    elif choice == '4':
        result = Division(num1, num2).divide()
        print("Result:", result)
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
