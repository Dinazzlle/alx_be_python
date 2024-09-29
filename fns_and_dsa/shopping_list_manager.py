# shopping_list_manager.py

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Start with an empty list

    while True:
        display_menu()  # Display menu options
        choice = input("Enter your choice: ").strip()  # Get user input and strip extra whitespace

        if choice == '1':  # Add item to the shopping list
            item = input("Enter the item to add: ").strip()
            if item:  # Ensure that the user entered something
                shopping_list.append(item)
                print(f"'{item}' has been added to the list.")
            else:
                print("Item name cannot be empty.")
        
        elif choice == '2':  # Remove item from the shopping list
            if shopping_list:
                item = input("Enter the item to remove: ").strip()
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"'{item}' has been removed from the list.")
                else:
                    print(f"'{item}' not found in the list.")
            else:
                print("The shopping list is currently empty.")
        
        elif choice == '3':  # View the shopping list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("The shopping list is currently empty.")
        
        elif choice == '4':  # Exit the program
            print("Goodbye!")
            break
        
        else:  # Handle invalid choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()