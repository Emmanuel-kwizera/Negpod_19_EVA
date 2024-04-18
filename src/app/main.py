from src.app import Meter, ElectricityVendingSystem
from src.app.token import Token
from src.database import DatabaseConnection


def main():
    connection = DatabaseConnection()
    system = ElectricityVendingSystem()
    meter = Meter(connection)
    token = Token(connection)

    while True:
        choice = system.main_menu()
        if choice == 1:
            meter.worker()
        elif choice == 2:
            token.purchase_electricity()
        elif choice == 3:
            token_code = input("Enter token: ")
            tk = token.find_by_token_id(token_code)
            id, meter_number, amount, token_code, created_at, electricity_units = tk
            if tk is not None:
                meter.update_meter_balance(meter_number, electricity_units)
                print(f"Token {token_code} worth {amount} RWF has been loaded.")
                print(f"Units added: {electricity_units} KwH")
            else:
                print("Token not found.")

        elif choice == 4:
            meter_info = meter.find_by_meter_number()
            Meter.display_meter_info(meter_info)

        elif choice == 5:
            system.help_submenu()
            pass
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

    print("Thank you for using the Electricity Vending System!")


if __name__ == "__main__":
    main()
