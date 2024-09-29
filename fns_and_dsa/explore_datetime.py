from datetime import datetime, timedelta

# Part 1: Display the current date and time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format it as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    # Print the current date and time
    print(f"Current date and time: {formatted_date}")
    return current_date

# Part 2: Calculate a future date
def calculate_future_date(current_date):
    # Prompt the user to enter the number of days
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    # Calculate the future date by adding the days to the current date
    future_date = current_date + timedelta(days=days_to_add)
    # Print the future date in "YYYY-MM-DD" format
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    return future_date

def main():
    # Display the current date and time
    current_date = display_current_datetime()
    # Calculate and display the future date
    calculate_future_date(current_date)

if __name__ == "__main__":
    main()
