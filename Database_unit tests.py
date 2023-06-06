import unittest
import psycopg2
from datetime import datetime
from unittest import mock

from DatabaseManager import connectPostgressDatabase,DatabaseConnection,getDbCursor,getDbHostPort,addUserToDatabase,addEventToDatabase,addCouponToDatabase,getUsersFromDatabase,getEventsFromDatabase,getCouponsFromDatabase




class TestInsertUser(unittest.TestCase):

    def setUp(self):
        self.dbc = mock.MagicMock(spec=['cursor', 'commit'])

    def test_insert_user_calls_cursor_execute_and_commit(self):
        # Prepare test data
        user = {
        "birth_year": 1990,
        "gender": "Male",
        "country": "Italy",
        "sport_pref": "Football",
        "currency": "EUR",
        "registration_date": "2022-03-01T00:00:00",
    }

        # Execute the function being tested
        addUserToDatabase(user, self.dbc)

        # Assert that cursor.execute and commit were called
        self.assertTrue(self.dbc.cursor().execute.called)
        self.assertTrue(self.dbc.commit.called)

class TestInsertEvent(unittest.TestCase):

    def setUp(self):
        self.dbc = mock.MagicMock(spec=['cursor', 'commit'])

    def test_insert_event_calls_cursor_execute_and_commit(self):
        # Prepare test data
        event = {
    
        "league": "Premier League",
        "sport": "Football",
        "country": "England",
        "begin_timestamp": "2022-04-10 15:00:00+00:00",
        "end_timestamp": "2022-04-10 17:00:00+00:00",
        "participants": ["Liverpool", "Chelsea"],
    }

        # Execute the function being tested
        addEventToDatabase(event, self.dbc)

        # Assert that cursor.execute and commit were called
        self.assertTrue(self.dbc.cursor().execute.called)
        self.assertTrue(self.dbc.commit.called)        
        

class TestInsertCoupon(unittest.TestCase):

    def setUp(self):
        self.dbc = mock.MagicMock(spec=['cursor', 'commit'])

    def test_insert_coupon_calls_cursor_execute_and_commit(self):
        # Prepare test data
        coupon=   {
        
        "selections": [{"event_id": 1, "odds": 2.0}],
        "stake": 10.0,
        "timestamp": "2022-04-08T09:30:00",
        "user_id": 1,
       }

        # Execute the function being tested
        addCouponToDatabase(coupon, self.dbc)

        # Assert that cursor.execute and commit were called
        self.assertTrue(self.dbc.cursor().execute.called)
        self.assertTrue(self.dbc.commit.called)      
        
           
if __name__ == "__main__":
    unittest.main()
