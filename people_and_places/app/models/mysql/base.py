from models.mysql.util import connect_to_database
import pandas as pd


class MySQLClient:
    def __init__(self):
        # Connect to the MySQL database
        self.connection = connect_to_database()
        self.cursor = self.connection.cursor()

    def insert_to_mysql(self, table, df):
        # Iterate over each row in the DataFrame and insert into the database
        for _, row in df.iterrows():
            values = tuple(row)
            placeholders = ", ".join(["%s"] * len(row))
            query = f"INSERT IGNORE INTO {table} VALUES ({placeholders})"
            self.cursor.execute(query, values)

    def fetch_data(self, table):
        # Fetch Data from MYSQL Tables
        query = f"SELECT * FROM {table}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        df = pd.DataFrame(result, columns=[column[0] for column in self.cursor.description])
        return df

    def close_connection(self):
        # Commit the changes and close the cursor and connection
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
