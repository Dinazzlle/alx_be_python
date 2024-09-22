# daily_reminder.py

def daily_reminder():
    # Prompt the user for the task description
    task = input("Enter your task: ")
    
    # Prompt the user for the task priority (high, medium, low)
    priority = input("Priority (high/medium/low): ").lower()
    
    # Ask if the task is time-bound
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    
    # Match case for priority level
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task."
        case "medium":
            reminder = f"'{task}' is a medium priority task."
        case "low":
            reminder = f"'{task}' is a low priority task."
        case _:
            reminder = f"'{task}' has an unspecified priority."

    # Add extra note for time-sensitive tasks
    if time_bound == "yes":
        reminder += " It requires immediate attention today!"
    else:
        reminder += " Consider completing it when you have free time."

    # Print the customized reminder in the expected format
    print(f"Reminder: {reminder}")

# Run the daily_reminder function
if __name__ == "__main__":
    daily_reminder()

