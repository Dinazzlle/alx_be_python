# match_case_calculator.py

def calculator():
    # Prompt user for input numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    # Ask for the operation
    operation = input("Choose the operation (+, -, *, /): ")
    
    # Perform calculation using match-case
    match operation:
        case '+':
            result = num1 + num2
            print(f"The result is {result}.")
        case '-':
            result = num1 - num2
            print(f"The result is {result}.")
        case '*':
            result = num1 * num2
            print(f"The result is {result}.")
        case '/':
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"The result is {result}.")
        case _:
            print("Invalid operation. Please choose one of (+, -, *, /).")
            
# Run the calculator
if __name__ == "__main__":
    calculator()


