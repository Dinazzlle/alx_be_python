# multiplication_table.py

def multiplication_table():
    # Prompt user for a number
    number = int(input("Enter a number to see its multiplication table: "))
    
    # Generate and print the multiplication table from 1 to 10
    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i} = {product}")

# Run the multiplication table function
if __name__ == "__main__":
    multiplication_table()
