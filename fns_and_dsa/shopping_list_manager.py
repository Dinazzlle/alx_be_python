def display_menu():
    # Ensure this matches the exact expected format
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    # Initialize the shopping_list as an empty list
    shopping_list = []
    
    while True:
        # Call the display_menu function
        display_menu()
        
        # Get user's choice and convert it to an integer
        choice = input("Enter your choice: ")
        
        try:
            # Convert input to an integer
            choice = int(choice)
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue  # If input is not a number, restart the loop
        
        if choice == 1:
            # Prompt for and add an item
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.")
        
        elif choice == 2:
            # Prompt for and remove an item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' was not found in your shopping list.")
        
        elif choice == 3:
            # Display the shopping list
            if shopping_list:
                print("\nYour shopping list:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")
        
        elif choice == 4:
            # Exit the program
            print("Goodbye!")
            break
        
        else:
            # Handle invalid choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
