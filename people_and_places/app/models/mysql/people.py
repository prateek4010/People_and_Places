from models.mysql.base import MySQLClient


class PeopleMySQLClient(MySQLClient):
    def __init__(self):
        super().__init__()

    def insert_to_mysql(self, table, df):
        super().insert_to_mysql(table, df)

    def fetch_data(self, table):
        return super().fetch_data(table)

    def close_connection(self):
        super().close_connection()
