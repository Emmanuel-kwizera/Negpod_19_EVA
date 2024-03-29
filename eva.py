from meter import Meter


class ElectricityVendingSystem:
    def __init__(self):
        self.meters = {}

    def welcome_message(self):
        print("Welcome to the Electricity Vending System!\n")
        print("This application allows you to conveniently manage your electricity usage and top up your meter.\n")
        print("**Before you begin, please note:**\n")
        print("* This non-commercial simulation does not connect to real electricity grids.")
        print("* Meter IDs are virtual for this application.\n")
        print("**Ready to manage your electricity?**\n")

    def get_user_choice(self, message, valid_choices):
        choice = input(message)
        while choice not in valid_choices:
            choice = input("Invalid choice. Please try again: ")
        return choice

    def create_meter(self):
        meter_id = input("Enter a unique meter ID: ")
        if meter_id in self.meters:
            print("Meter ID already exists.")
        else:
            nickname = input("Enter a nickname for the meter (optional): ")
            self.meters[meter_id] = Meter(meter_id, nickname)
            print(f"Meter {meter_id} created successfully.")

    def update_meter(self):
        meter_id = self.get_meter_id("Select the meter you want to update: ")
        if meter_id:
            new_nickname = input("Enter a new nickname for the meter (leave blank to keep the current one): ")
            if new_nickname:
                self.meters[meter_id].update_nickname(new_nickname)
                print("Meter nickname updated successfully.")
            else:
                print("Meter nickname unchanged.")

    def delete_meter(self):
        meter_id = self.get_meter_id("Select the meter you want to delete: ")
        if meter_id:
            confirm = self.get_user_choice(f"Are you sure you want to delete meter {meter_id}? (Y/N) ", ["Y", "N"])
            if confirm == "Y":
                del self.meters[meter_id]
                print(f"Meter {meter_id} deleted successfully.")

    def list_meters(self):
        if not self.meters:
            print("No meters found.")
        else:
            print("Registered meters:")
            for meter_id, meter in self.meters.items():
                nickname = f" ({meter.nickname})" if meter.nickname else ""
                print(f"- {meter_id}{nickname}")

    def purchase_token(self):
        meter_id = self.get_meter_id("Enter the meter ID for the token purchase: ")
        if meter_id:
            token_code = input("Enter the token code you purchased: ")
            credit_amount = len(token_code) * 10
            self.meters[meter_id].add_credit(credit_amount)
            print(f"Token {token_code} applied successfully. ${credit_amount} added to meter {meter_id}.")

    def view_balance(self):
        meter_id = self.get_meter_id("Select the meter to view the balance: ")
        if meter_id:
            balance = self.meters[meter_id].get_balance()
            print(f"Current balance for meter {meter_id}: ${balance}")

    def view_top_up_history(self):
        meter_id = self.get_meter_id("Select the meter to view the top-up history: ")
        if meter_id:
            history = self.meters[meter_id].get_top_up_history()
            if not history:
                print(f"No top-up history found for meter {meter_id}.")
            else:
                print(f"Top-up history for meter {meter_id}:")
                for entry in history:
                    amount, description = entry
                    print(f"- ${amount} ({description})")

    def get_meter_id(self, prompt):
        meter_id = input(prompt)
        if meter_id not in self.meters:
            print(f"Meter {meter_id} not found.")
            return None
        return meter_id

    def display_tariffs(self):
        print("Electricity Tariffs:")
        print("- Tier 1 (0-100 kWh): $0.10 per kWh")
        print("- Tier 2 (101-200 kWh): $0.12 per kWh")
        print("- Tier 3 (201+ kWh): $0.15 per kWh")
        print("- Off-peak hours (10 PM - 6 AM): 20% discount")
        print("- Special offer: Sign up for auto-pay and get 5% off your total bill!")

    def run(self):
        self.welcome_message()
        start = self.get_user_choice("Enter Y to continue or N to exit: ", ["Y", "N"])
        if start == "N":
            print("Goodbye!")
            return

        while True:
            choice = self.get_user_choice("\n**Main Menu:**\n\n"
                                           "1. Meter Management\n"
                                           "2. Purchase with Token\n"
                                           "3. View Credit Balance\n"
                                           "4. View Top-up History\n"
                                           "5. Learn About Electricity Tariffs\n"
                                           "6. Exit\n\n"
                                           "Enter your choice: ", ["1", "2", "3", "4", "5", "6"])

            if choice == "1":
                meter_choice = self.get_user_choice("\n**Meter Management:**\n\n"
                                                     "a. Create Meter\n"
                                                     "b. Update Meter\n"
                                                     "c. Delete Meter\n"
                                                     "d. List Meters (if applicable)\n\n"
                                                     "Enter your choice: ", ["a", "b", "c", "d"])
                if meter_choice == "a":
                    self.create_meter()
                elif meter_choice == "b":
                    self.update_meter()
                elif meter_choice == "c":
                    self.delete_meter()
                elif meter_choice == "d":
                    self.list_meters()

            elif choice == "2":
                self.purchase_token()

            elif choice == "3":
                self.view_balance()

            elif choice == "4":
                self.view_top_up_history()

            elif choice == "5":
                self.display_tariffs()

            elif choice == "6":
                print("Thank you for using the Electricity Vending System. Goodbye!")
                break
