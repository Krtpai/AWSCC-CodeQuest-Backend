# Menu display.
def display_menu():
    print("\nOptions:")
    print("1. Add item to the shopping list")
    print("2. View shopping list")
    print("3. Remove item from the shopping list")
    print("4. Quit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            item = input("Enter the item you want to add: ")
            shopping_list.append(item)
            print(f"{item} has been added to your shopping list.")
        elif choice == "2":
            print("Your shopping list:")
            for item in shopping_list:
                print(item)
        elif choice == "3":
            item = input("Enter the item you want to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from your shopping list.")
            else:
                print(f"{item} is not in your shopping list.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()