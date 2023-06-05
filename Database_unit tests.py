import unittest
import psycopg2
from datetime import datetime
from unittest import mock

from DatabaseManager import connectPostgressDatabase,DatabaseConnection,getDbCursor,getDbHostPort,addUserToDatabase,addEventToDatabase,addCouponToDatabase,getUsersFromDatabase,getEventsFromDatabase,getCouponsFromDatabase


class Test_insert_rows(unittest.TestCase):

    def setUp(self):
        self.dbc = mock.MagicMock(spec=['cursor', 'commit'])
        self.test_user = {
        "birth_year": 1990,
        "gender": "Male",
        "country": "Italy",
        "sport_pref": "Football",
        "currency": "EUR",
        "registration_date": "2022-03-01T00:00:00",
         }


    def test_insert_rows_calls_cursor_method(self):
    
        rows = self.test_user
        addUserToDatabase(rows,self.dbc)
        self.assertTrue(self.dbc.cursor.called)

class TestInsertUsers(unittest.TestCase):

    def setUp(self):
        self.dbc = mock.MagicMock(spec=['cursor', 'commit'])

    def test_insert_user_calls_cursor_execute_and_commit(self):
        # Prepare test data
        user = {
        "user_id" : 1,
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
        
if __name__ == "__main__":
    unittest.main()
