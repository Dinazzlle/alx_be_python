# pattern_drawing.py

def draw_pattern():
    # Prompt the user to input a positive integer for the pattern size
    size = int(input("Enter the size of the pattern: "))
    
    # Initialize the row counter for the while loop
    row = 0
    
    # Outer while loop to control the number of rows
    while row < size:
        # Nested for loop to print asterisks in a single row
        for col in range(size):
            print("*", end="")
        
        # Move to the next line after printing a full row of asterisks
        print()
        
        # Increment the row counter
        row += 1

# Run the draw_pattern function
if __name__ == "__main__":
    draw_pattern()
