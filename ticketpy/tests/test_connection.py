import pytest
from ticketpy.connection import Connection

"""
Testing file for Connection Class and its modules

Written By Kyle Richardson
"""


@pytest.fixture()
def test_connection_no_ver():
    return Connection("thisismyfakeapikey")


@pytest.fixture()
def test_connection_ver():
    return Connection("thisismyfakeapikey", 2)


def test_create_url(test_connection_no_ver, test_connection_ver):
    """Tests create_url method combines strings together
    correctly."""
    good_url = ("https://app.ticketmaster.com/discovery/v2/"
                "events.json?apikey=thisismyfakeapikey")
    assert test_connection_no_ver.create_url("discovery") == good_url
    assert test_connection_ver.create_url("discovery") == good_url
