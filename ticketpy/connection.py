"""
Script containing the Connection Class.

Connections are used to establish a reusable connection with the
Ticketmaster API. These Connections are used to make all API
requests to Ticketmaster(Refered to as 'TM' in comments).

Written by Kyle Richardson

For more information on the Ticketmaster API visit
http://developer.ticketmaster.com
"""

class Connection(object):
    """Connection class used to make API queries to Ticketmaster"""
    def __init__(self, api_key, version=2):
        """Initiation method for Connection Class
        Parameters:
        api_key(string): Your Application API key provided by Ticketmaster
        version(int): Specify the version of TM API to be used.
            defaults to most current verison (2.0 as of 8/6/16)"""
        self.api_key = api_key
        self.version = version

    def create_url(self, api_cat):
        """Creates the url for TM API requests."""
