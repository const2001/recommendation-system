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


class TestGetUsers(unittest.TestCase):

    def setUp(self):
        self.dbc = mock.MagicMock(spec=['cursor'])

    def test_get_users_returns_list_of_users(self):
        # Prepare mock data
        expected_users = [
            {
                "user_id": 1,
                "birth_year": 1990,
                "gender": "Male",
                "country": "Italy",
                "sport_pref": "Football",
                "currency": "EUR",
                "registration_date": "2022-03-01T00:00:00",
            },
            {
                "user_id": 2,
                "birth_year": 1985,
                "gender": "Female",
                "country": "USA",
                "sport_pref": "Basketball",
                "currency": "USD",
                "registration_date": "2022-02-15T12:30:00",
            }
        ]

        # Mock the cursor and its execute method
        cursor_mock = self.dbc.cursor.return_value
        cursor_mock.fetchall.return_value = expected_users

        # Execute the function being tested
        users = getUsersFromDatabase(self.dbc)

        # Assert the result
        self.assertEqual(users, expected_users)

    def test_get_users_empty_result_returns_empty_list(self):
        # Mock the cursor and its execute method
        cursor_mock = self.dbc.cursor.return_value
        cursor_mock.fetchall.return_value = []

        # Execute the function being tested
        users = getUsersFromDatabase(self.dbc)

        # Assert the result
        self.assertEqual(users, [])


class TestGetEvents(unittest.TestCase):

    def setUp(self):
        self.dbc = mock.MagicMock(spec=['cursor'])

    def test_get_events_returns_list_of_events(self):
        # Prepare mock data
        expected_events = [
            {
                "event_id": 1,
                "league": "Premier League",
                "sport": "Football",
                "country": "England",
                "begin_timestamp": "2022-04-10 15:00:00+00:00",
                "end_timestamp": "2022-04-10 17:00:00+00:00",
                "participants": ["Liverpool", "Chelsea"],
            },
            {
                "event_id": 2,
                "league": "NBA",
                "sport": "Basketball",
                "country": "USA",
                "begin_timestamp": "2022-05-20 20:00:00+00:00",
                "end_timestamp": "2022-05-20 22:00:00+00:00",
                "participants": ["Los Angeles Lakers", "Brooklyn Nets"],
            }
        ]

        # Mock the cursor and its execute method
        cursor_mock = self.dbc.cursor.return_value
        cursor_mock.fetchall.return_value = expected_events

        # Execute the function being tested
        events = getEventsFromDatabase(self.dbc)

        # Assert the result
        self.assertEqual(events, expected_events)

    def test_get_events_empty_result_returns_empty_list(self):
        # Mock the cursor and its execute method
        cursor_mock = self.dbc.cursor.return_value
        cursor_mock.fetchall.return_value = []

        # Execute the function being tested
        events = getEventsFromDatabase(self.dbc)

        # Assert the result
        self.assertEqual(events, [])  
    
        
class TestGetCoupons(unittest.TestCase):

    def setUp(self):
        self.dbc = mock.MagicMock(spec=['cursor'])

    def test_get_coupons_returns_list_of_coupons(self):
        # Prepare mock data
        expected_coupons = [
            {
                "coupon_id": 1,
                "selections": [{"event_id": 1, "odds": 2.0}],
                "stake": 10.0,
                "timestamp": "2022-04-08T09:30:00",
                "user_id": 1,
            },
            {
                "coupon_id": 2,
                "selections": [{"event_id": 2, "odds": 1.5}],
                "stake": 5.0,
                "timestamp": "2022-04-09T14:45:00",
                "user_id": 2,
            }
        ]

        # Mock the cursor and its execute method
        cursor_mock = self.dbc.cursor.return_value
        cursor_mock.fetchall.return_value = expected_coupons

        # Execute the function being tested
        coupons = getCouponsFromDatabase(self.dbc)

        # Assert the result
        self.assertEqual(coupons, expected_coupons)

    def test_get_coupons_empty_result_returns_empty_list(self):
        # Mock the cursor and its execute method
        cursor_mock = self.dbc.cursor.return_value
        cursor_mock.fetchall.return_value = []

        # Execute the function being tested
        coupons = getCouponsFromDatabase(self.dbc)

        # Assert the result
        self.assertEqual(coupons, [])

if __name__ == "__main__":
    unittest.main()
