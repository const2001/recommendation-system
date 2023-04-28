import unittest
from recommendation_gen import recommend_coupons 
from validators import validate_user,validate_event,validate_coupon


class TestUserValidator(unittest.TestCase):
    
    def test_valid_user(self):
        user = {
            "name": "John Doe",
            "email": "johndoe@example.com",
            "age": 30
        }
        result = validate_user(user)
        self.assertEqual(result, "The JSON data is valid.")
    
    def test_invalid_user(self):
        user = {
            "name": "Jane Doe",
            "email": "janedoe.example.com",
            "age": "30"
        }
        result = validate_user(user)
        self.assertIn("The JSON data is not valid.", result)





class TestRecommendCoupons(unittest.TestCase):

    def test_recommend_coupons(self):
     user = {"user_id": 1, "birth_year": 1990, "country": "Italy", "sport_pref": "Football",
            "currency": "EUR", "registration_date": "2022-03-01T00:00:00"}
     events = [
        {"event_id": "E001", "league": "Premier League", "sport": "Football", "country": "England", "begin_timestamp":
            "2022-04-10 15:00:00+00:00", "end_timestamp": "2022-04-10 17:00:00+00:00", "participants": ["Liverpool", "Chelsea"]},
        {"event_id": "E002", "league": "La Liga", "sport": "Football", "country": "Spain", "begin_timestamp": "2022-04-10 20:00:00+02:00",
            "end_timestamp": "2022-04-10 22:00:00+02:00", "participants": ["Real Madrid", "Barcelona"]},
        {"event_id": "E003", "league": "Serie A", "sport": "Football", "country": "Italy", "begin_timestamp": "2022-04-12 21:00:00+02:00",
            "end_timestamp": "2022-04-12 23:00:00+02:00", "participants": ["Juventus", "AC Milan"]}
      ]
     coupons = [
        {"coupon_id": "C001", "selections": [{"event_id": "E001", "odds": 2.0}],
            "stake": 10.0, "timestamp": "2022-04-08T09:30:00", "user_id": 1},
        {"coupon_id": "C002", "selections": [{"event_id": "E002", "odds": 1.5}, {
            "event_id": "E003", "odds": 2.0}], "stake": 5.0, "timestamp": "2022-04-08T10:30:00", "user_id": 2},
        {"coupon_id": "C003", "selections": [{"event_id": "E003", "odds": 2.5}],
            "stake": 20.0, "timestamp": "2022-04-08T11:30:00", "user_id": 3},
     ]
     result = recommend_coupons(user, coupons, events)
     expected_result =  [{'coupon_id': 'C003', 'selections': [{'event_id': 'E003', 'odds': 2.5}], 'stake': 20.0, 'timestamp': '2022-04-08T11:30:00', 'user_id': 3, 'odds': 2.5}]
     self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
