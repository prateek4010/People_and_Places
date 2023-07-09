from config import people_table, places_table
from models.mysql.people import PeopleMySQLClient
from models.mysql.places import PlacesMySQLClient
import pandas as pd


def calculate_results(people_df, places_df):
    # Join people and places table
    joined_df = pd.merge(people_df, places_df, left_on='place_of_birth', right_on='city', how='inner')

    # Dropping duplicates
    joined_df.drop_duplicates(inplace=True)
    summary_df = joined_df.groupby('country')['given_name'].count().rename('count').reset_index()
    print(summary_df)

    # Write to json file
    summary_df.set_index('country')['count'].to_json('data/summary_output.json')


def process_all():
    # Read the CSV file into a pandas DataFrame
    people_df = pd.read_csv(f"sources/{people_table}.csv")
    places_df = pd.read_csv(f"sources/{places_table}.csv")

    # Check for empty sources
    if people_df.empty or places_df.empty:
        print("Empty data")
        # Can set alerts/notifications here
        return

    # Process people data
    people_obj = PeopleMySQLClient()
    people_obj.insert_to_mysql(people_table, people_df)
    print("People Data inserted successfully!")
    people_df = people_obj.fetch_data(people_table)
    people_obj.close_connection()
    print(people_df.shape)

    # Process people data
    places_obj = PlacesMySQLClient()
    places_obj.insert_to_mysql(places_table, places_df)
    print("Places Data inserted successfully!")
    places_df = places_obj.fetch_data(places_table)
    places_obj.close_connection()
    print(places_df.shape)

    # Calculating end result and output to summary json file
    calculate_results(people_df, places_df)

    # Can set alerts/notifications here


if __name__ == "__main__":
    process_all()
