def admin_dash_menu():
    print("\t       Welcome to the EVA panel. Here is the menu\n")
    print("\t_______________________________________________________\n")
    print("\t     1. Buy Electricity \n")
    print("\t     2. View Recent Receipts \n")
    print("\t     3. Exit\n")
    print("\n\n\t_______________________________________________________\n")
    choice = int(input("\t\t\t Enter your choice      : "))
    return choice

def main():
    choice = admin_dash_menu()
    print("You entered:", choice)

if __name__ == "__main__":
    main()

