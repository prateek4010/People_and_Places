import pytest
from config import people_table, places_table
from models.mysql.people import PeopleMySQLClient
from models.mysql.places import PlacesMySQLClient


@pytest.fixture()
def test_fetch_data():
    people_obj = PeopleMySQLClient()
    people_df = people_obj.fetch_data(people_table)
    people_obj.close_connection()
    assert (people_df.shape[0] == 1)

    places_obj = PlacesMySQLClient()
    places_df = places_obj.fetch_data(places_table)
    assert (places_df.shape[0] == 1)
