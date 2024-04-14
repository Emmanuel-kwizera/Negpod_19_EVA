import secrets
import string

from src.database.connection import DatabaseManager


class ElectricityVendingSystem:
    def __init__(self):
        self.db_manager = DatabaseManager()

    def generate_token(self, token_length=10):
        characters = string.digits
        return ''.join(secrets.choice(characters) for _ in range(token_length))

    def purchase_token(self, meter_id, amount):
        token = self.generate_token()
        meter = self.get_meter(meter_id)
        meter.add_token(token, amount)
        self.db_manager.save_meter(meter)
        self.db_manager.save_token(token, amount, meter_id)
        print(f"Token {token} worth ${amount} has been generated for meter {meter_id}.")

    def get_meter(self, meter_id):
        return self.db_manager.get_meter(meter_id)

    def view_tokens(self, meter_id):
        meter = self.get_meter(meter_id)
        tokens = meter.get_tokens()
        for token, amount in tokens.items():
            print(f"- Token: {token}, Amount: ${amount}")

    def close(self):
        self.db_manager.close()
