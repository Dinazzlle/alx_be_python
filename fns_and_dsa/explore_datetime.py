# explore_datetime.py

from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date and time
    print(f"Current date and time: {formatted_date}")
    return current_date

# Part 2: Calculate a Future Date
def calculate_future_date(days_to_add):
    current_date = datetime.now()  # Get the current date and time
    future_date = current_date + timedelta(days=days_to_add)  # Add the specified number of days
    formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format the future date
    print(f"Future date: {formatted_future_date}")
    return future_date

# Main script logic
if __name__ == "__main__":
    display_current_datetime()  # Display current date and time
    
    # Prompt the user to enter a number of days
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)  # Calculate and display the future date
    except ValueError:
        print("Please enter a valid integer for the number of days.")