import mysql.connector

from src.app import Meter
from src.config.settings import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME


class DatabaseConnection:
    def __init__(self):
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor

    def commit(self):
        self.connection.commit()

    def close(self):
        if self.connection:
            self.connection.close()


class DatabaseManager:
    def __init__(self):
        self.db = DatabaseConnection()
        self.db.connect()

    def get_meter(self, meter_id):
        query = "SELECT meter_id, nickname, tokens FROM meters WHERE meter_id = %s"
        cursor = self.db.execute_query(query, (meter_id,))
        row = cursor.fetchone()
        if row:
            meter_id, nickname, tokens = row
            return Meter(meter_id, nickname, eval(tokens))
        else:
            return Meter(meter_id, "", {})

    def save_meter(self, meter):
        query = "INSERT INTO meters (meter_id, nickname, tokens) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE nickname = %s, tokens = %s"
        tokens = str(meter.tokens)
        self.db.execute_query(query, (meter.meter_id, meter.nickname, tokens, meter.nickname, tokens))
        self.db.commit()

    def save_token(self, token, amount, meter_id):
        query = "INSERT INTO tokens (token, amount, meter_id) VALUES (%s, %s, %s)"
        self.db.execute_query(query, (token, amount, meter_id))
        self.db.commit()

    def close(self):
        self.db.close()
