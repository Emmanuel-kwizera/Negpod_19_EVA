import mysql.connector
from threading import local

from src.app import Meter
from src.config.settings import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME


class DatabaseConnection:
    _connection_pool = local()

    def __init__(self):
        self.connection = None

    @classmethod
    def get_connection(cls):
        if not hasattr(cls._connection_pool, "conn"):
            cls._connection_pool.conn = mysql.connector.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
            )
            print("Connected to MySQL database successfully!")
        return cls._connection_pool.conn

    def close_connection(self):
        # No need to close the connection here, managed by pool
        pass

    def execute_query(self, query, params=None):
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Error executing query: {err}")
            return None
        finally:
            cursor.close()
