from src.app.menu import Menu


class Meter:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    @staticmethod
    def meter_menu():
        meter_menu = Menu("Meter Management", [
            "1. Create Meter",
            "2. View All Meters",
            "3. Find Meter by Number",  # Added update option
            "4. Back to Main Menu"
        ])
        meter_menu.display()
        choice = meter_menu.get_user_choice()
        return choice

    def worker(self):
        while True:
            choice = Meter.meter_menu()
            if choice == 1:
                Meter.create_meter(self)
            elif choice == 2:
                Meter.view_all_meters(self)
            elif choice == 3:
                meter_info = Meter.find_by_meter_number(self)
                Meter.display_meter_info(meter_info)
            elif choice == 4:
                return
            else:
                print("Invalid choice. Please enter a number between 1 and 4")

    def create_meter(self):
        meter_number = input("Enter meter number: ")
        owner = input("Enter meter owner: ")
        location = input("Enter meter location: ")
        # Set current_balance to 0 by default
        current_balance = 0.0
        query = "INSERT INTO meters (meter_number, owner, location, current_balance) VALUES (%s, %s, %s, %s)"
        params = (meter_number, owner, location, current_balance)
        self.db_connection.execute_query(query, params)
        print(f"Meter {meter_number} created successfully!")

    def view_all_meters(self):
        query = "SELECT * FROM meters"
        results = self.db_connection.execute_query(query)
        if not results:
            print("No meters found.")
            return
        print("\n######## Meter List ######")
        for row in results:
            id, meter_number, owner, location, current_balance = row
            print(f"\tMeter Number: {meter_number}")
            print(f"\tOwner: {owner}")
            print(f"\tLocation: {location}")
            print(f"\tCurrent Balance: {current_balance} KwH")
            print("------------------------------")

    def find_by_meter_number(self):
        meter_number = input("Enter meter number: ")
        query = "SELECT * FROM meters WHERE meter_number = %s"
        params = (meter_number,)
        results = self.db_connection.execute_query(query, params)
        if not results:
            print(f"Meter number {meter_number} not found.")
            return None
        return results[0]

    @staticmethod
    def display_meter_info(meter_info):
        if meter_info is None:
            return
        id, meter_number, owner, location, current_balance = meter_info
        print(f"\nMeter Details for {meter_number}:")
        print(f"\tOwner: {owner}")
        print(f"\tLocation: {location}")
        print(f"\tCurrent Balance: {current_balance} KwH")

    def update_meter_balance(self, meter_number, units):
        query = "SELECT current_balance FROM meters WHERE meter_number = %s"
        params = (meter_number,)
        results = self.db_connection.execute_query(query, params)
        if not results:
            print(f"Meter number {meter_number} not found.")
            return
        current_balance = results[0][0]
        new_balance = current_balance + units
        query = "UPDATE meters SET current_balance = %s WHERE meter_number = %s"
        params = (new_balance, meter_number)
        self.db_connection.execute_query(query, params)
        print(f"Meter balance updated successfully!")
