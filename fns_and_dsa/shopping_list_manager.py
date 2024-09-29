# Function to display the menu
def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# Main function to handle the shopping list operations
def main():
    # Initialize an empty shopping list
    shopping_list = []
    
    # Start a loop that runs until the user chooses to exit
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Adding an item to the shopping list
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)  # Append the item to the list
            print(f"'{item}' has been added to the shopping list.")
        
        elif choice == '2':
            # Removing an item from the shopping list
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)  # Remove the item if found
                print(f"'{item}' has been removed from the shopping list.")
            else:
                # Notify the user if the item is not in the list
                print(f"'{item}' not found in the shopping list.")
        
        elif choice == '3':
            # Displaying the shopping list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("The shopping list is currently empty.")
        
        elif choice == '4':
            # Exiting the program
            print("Goodbye!")
            break
        
        else:
            # Handle invalid input
            print("Invalid choice. Please try again.")

# Ensure that the main function runs only when the script is executed directly
if __name__ == "__main__":
    main()

