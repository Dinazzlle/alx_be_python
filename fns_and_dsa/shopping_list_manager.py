def display_menu():
    # Adjusted print to match the expected output format
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Initialize shopping_list as an empty list

    while True:
        display_menu()  # Call the display_menu function to show the options
        
        try:
            choice = int(input("Enter your choice: "))  # Ensure input is taken as an integer
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            item = input("Enter the item to add: ").strip()  # Prompt for item and remove any extra spaces
            shopping_list.append(item)  # Add item to the shopping list
            print(f"'{item}' has been added to the list.")
        
        elif choice == 2:
            item = input("Enter the item to remove: ").strip()  # Prompt for item to remove
            if item in shopping_list:
                shopping_list.remove(item)  # Remove item if it exists
                print(f"'{item}' has been removed from the list.")
            else:
                print(f"'{item}' not found in the list.")  # Inform if item is not found
        
        elif choice == 3:
            if shopping_list:  # Check if the shopping list is not empty
                print("\nCurrent Shopping List:")
                for i, item in enumerate(shopping_list, 1):  # Display items with index
                    print(f"{i}. {item}")
            else:
                print("\nThe shopping list is empty.")  # Message if the list is empty
        
        elif choice == 4:
            print("Goodbye!")  # Exit message
            break
        
        else:
            print("Invalid choice. Please try again.")  # Handle invalid menu choice

if __name__ == "__main__":
    main()  # Run the main function when the script is executed
