from src.app import Meter
import random
import string

class Token:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.meter = Meter(db_connection)

    @staticmethod
    def generate_token():
        """
        Generates a random 8-character alphanumeric token.
        """
        token = random.randint(10000000, 100000000)
        return token

    def create_token(self, meter_number, amount, electricity_units):
        # generate token number
        token_code = Token.generate_token()
        query = "INSERT INTO tokens (token_code, meter_number, amount, electricity_units) VALUES (%s, %s, %s, %s)"
        params = (token_code, meter_number, amount, electricity_units)
        self.db_connection.execute_query(query, params)
        print(f"Token {token_code} worth {amount} RWF has been generated.")

    def purchase_electricity(self):
        meter_info = self.meter.find_by_meter_number()
        # if meter_info is None, say meter not found
        # else, display meter info

        if meter_info is None:
            print("Meter not found.")
            return
        id, meter_number, owner, location, current_balance = meter_info
        print(f"Enter the amount you want to purchase for the meter {meter_number} ({owner})")

        amount_str = input("Amount: ")
        try:
            amount = float(amount_str)  # Convert the input string to a float (can also use int() for integers)
        except ValueError:
            print("Invalid input. Please enter a number.")
            amount = None  # Set amount to None to indicate an error

        # Now you can use the 'amount' variable, but check if it's None first (due to potential conversion error)
        if amount is not None:
            units = amount / 400
            self.create_token(meter_number, amount, units)

    def list_tokens(self, meter_number=None):
        if meter_number:
            query = "SELECT * FROM tokens WHERE meter_number = %s"
            params = (meter_number,)
        else:
            query = "SELECT * FROM tokens"
            params = None
        results = self.db_connection.execute_query(query, params)
        if not results:
            print("No tokens found.")
            return
        print("Token List:")
        for row in results:

            token_code, meter_number, amount, created_at, electricity_units = row
            print(f"Token ID: {token_code}")
            print(f"\tMeter Number: {meter_number}")
            print(f"\tAmount: {amount}")
            print(f"\tCreated At: {created_at}")
            print(f"\tElectricity Units: {electricity_units} KwH")

    def find_by_token_id(self, token_code):
        query = "SELECT * FROM tokens WHERE token_code = %s"
        params = (token_code,)
        results = self.db_connection.execute_query(query, params)
        if not results:
            print(f"Token {token_code} not found.")
            return None
        return results[0]
