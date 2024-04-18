from src.app.menu import Menu


class ElectricityVendingSystem:
    def __init__(self):
        pass

    @staticmethod
    def main_menu():
        main_menu = Menu("Electricity Vending System", [
            "1. Meter Management",
            "2. Purchase Electricity",
            "3. Load Token",
            "4. View Account Information",
            "5. Help",
            "6. Exit"
        ])
        main_menu.display()
        choice = main_menu.get_user_choice()
        return choice

    @staticmethod
    def help_submenu():
        """
        Prints a help menu with explanations for functionalities.
        """
        print("\nHelp Menu:")
        print("1. Meter Management:")
        print("\t- Create Meter: Add a new meter to the system and associate it with a location.")
        print("\t- View All Meters: List all meters and their details (meter number, location).")
        print("\t- Find Meter by Number: Search for a specific meter and view its details.")
        print("\t- Add Token: Associate a token with a meter for future electricity purchases.")
        print("\t- Remove Token: Disassociate a token from a meter if it's no longer needed.")
        print("2. Purchase Electricity: (Not implemented yet)")
        print(
            "\t- This functionality will allow users to purchase electricity using tokens associated with their meters.")
        print("3. View Account Information: (Not implemented yet)")
        print("\t- This functionality will display account-related information (purchase history, balance, etc.).")

