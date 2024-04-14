from src.app import ElectricityVendingSystem, get_user_choice, get_meter_id

def welcome_message():
    print("Welcome to the Electricity Vending System!\n")
    print("This application allows you to conveniently manage your electricity usage and top up your meter.\n")
    print("**Before you begin, please note:**\n")
    print("* This non-commercial simulation does not connect to real electricity grids.")
    print("* Meter IDs are virtual for this application.\n")
    print("**Ready to manage your electricity?**\n")


def run():
    welcome_message()
    start = get_user_choice("Enter Y to continue or N to exit: ", ["Y", "N"])
    if start == "N":
        print("Goodbye!")
        return

    system = ElectricityVendingSystem()

    while True:
        choice = get_user_choice("\n**Main Menu:**\n\n"
                                 "1. Purchase Token\n"
                                 "2. View Tokens\n"
                                 "3. Exit\n\n"
                                 "Enter your choice: ", ["1", "2", "3"])

        if choice == "1":
            meter_id = get_meter_id("Enter the meter ID for the token purchase: ")
            try:
                amount = float(input("Enter the amount you want to pay: "))
            except ValueError:
                print("\033[91mInvalid amount entered.\033[0m")
                continue
            system.purchase_token(meter_id, amount)

        elif choice == "2":
            meter_id = get_meter_id("Select the meter to view tokens: ")
            system.view_tokens(meter_id)

        elif choice == "3":
            print("\033[92mThank you for using the Electricity Vending System. Goodbye!\033[0m")
            system.close()
            break


if __name__ == "__main__":
    run()
