from engine import run_analysis, view_history, clear_history

def main_menu():
    while True:
        print("\n==============================")
        print("Perspective Simulator :)")
        print("==============================")
        print("1. Enter a situation")
        print("2. View history")
        print("3. Clear history")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            text = input("\nDescribe your situation: ")
            run_analysis(text)

        elif choice == "2":
            view_history()

        elif choice == "3":
            clear_history()

        elif choice == "4":
            print("Goodbye! I hope I helped you feel better :)")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main_menu()
