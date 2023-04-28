import unittest
from recommendation_gen import recommend_coupons
from validators import validate_user, validate_event, validate_coupon


class TestUserValidator(unittest.TestCase):
    def test_valid_user(self):
        user = {
            "user_id": 5,
            "birth_year": 1998,
            "country": "USA",
            "sport_pref": "American Football",
            "currency": "USD",
            "registration_date": "2022-04-11T00:00:00",
        }
        valid, message = validate_user(user)
        self.assertTrue(valid)
        self.assertEqual(message, "The JSON data is valid.")

    def test_invalid_user(self):
        user = {
            "user_id": "5",
            "birth_year": 1998,
            "country": "USA",
            "sport_pref": "American Football",
            "currency": "USD",
            "registration_date": "2022-04-11T00:00:00",
        }
        valid, message = validate_user(user)
        self.assertFalse(valid)
        self.assertIn(
            "The JSON data is not valid. '5' is not of type 'integer'",
            message,
        )

    def test_invalid_user(self):
        user = {
            "user_id": "5",
            "birth_year": 1998,
            "sport_pref": "American Football",
            "currency": "USD",
            "registration_date": "2022-04-11T00:00:00",
        }
        valid, message = validate_user(user)
        self.assertFalse(valid)
        self.assertIn(
            "The JSON data is not valid. 'country' is a required property",
            message,
        )


class TestEventValidator(unittest.TestCase):
    def test_valid_event(self):
        event = {
            "begin_timestamp": "2020-02-08 18:00:00+00",
            "country": "Czech Republic",
            "end_timestamp": "2099-01-01 00:00:00+00",
            "event_id": "2ff91a42-09b3-41a2-a8c4-4a78ba85f4cf",
            "league": "Extraliga",
            "participants": ["HC Zubri", "HBC Ronal Jicin"],
            "sport": "handball",
        }
        valid, message = validate_event(event)
        self.assertTrue(valid)
        self.assertEqual(message, "The JSON data is valid.")

    def test_invalid_event_with_incorrect_type(self):
        event = {
            "begin_timestamp": "2020-02-08 18:00:00+00",
            "country": "Czech Republic",
            "end_timestamp": 4083072000,
            "event_id": "2ff91a42-09b3-41a2-a8c4-4a78ba85f4cf",
            "league": "Extraliga",
            "participants": ["HC Zubri", "HBC Ronal Jicin"],
            "sport": "handball",
        }
        valid, message = validate_event(event)
        self.assertFalse(valid)
        self.assertIn(
            "The JSON data is not valid. 4083072000 is not of type 'string'",
            message,
        )

    def test_invalid_event_with_missing_country(self):
        event = {
            "begin_timestamp": "2020-02-08 18:00:00+00",
            "end_timestamp": "2099-01-01 00:00:00+00",
            "event_id": "2ff91a42-09b3-41a2-a8c4-4a78ba85f4cf",
            "league": "Extraliga",
            "participants": ["HC Zubri", "HBC Ronal Jicin"],
            "sport": "handball",
        }
        valid, message = validate_event(event)
        self.assertFalse(valid)
        self.assertIn(
            "The JSON data is not valid. 'country' is a required property",
            message,
        )


class TestCouponValidator(unittest.TestCase):
    def test_valid_coupon(self):
        coupon = {
            "coupon_id": "C001",
            "selections": [{"event_id": "E001", "odds": 2.0}],
            "stake": 10.0,
            "timestamp": "2022-04-08T09:30:00",
            "user_id": 1,
        }
        valid, message = validate_coupon(coupon)
        self.assertTrue(valid)
        self.assertEqual(message, "The JSON data is valid.")

    def test_invalid_coupon_with_incorrect_type(self):
        coupon = {
            "coupon_id": "C001",
            "selections": [{"event_id": "E001", "odds": "2.0"}],
            "stake": 10.0,
            "timestamp": "2022-04-08T09:30:00",
            "user_id": 1,
        }
        valid, message = validate_coupon(coupon)
        self.assertFalse(valid)
        self.assertIn(
            "The JSON data is not valid. '2.0' is not of type 'number'",
            message,
        )

    def test_invalid_coupon_with_missing_coupon_id(self):
        coupon = {
            "selections": [{"event_id": "E001", "odds": 2.0}],
            "stake": 10.0,
            "timestamp": "2022-04-08T09:30:00",
            "user_id": 1,
        }
        valid, message = validate_coupon(coupon)
        self.assertFalse(valid)
        self.assertIn(
            "The JSON data is not valid. 'coupon_id' is a required property",
            message,
        )

    def test_invalid_coupon_with_missing_user_id(self):
        coupon = {
            "coupon_id": "C001",
            "selections": [{"event_id": "E001", "odds": 2.0}],
            "stake": 10.0,
            "timestamp": "2022-04-08T09:30:00",
        }
        valid, message = validate_coupon(coupon)
        self.assertFalse(valid)
        self.assertIn(
            "The JSON data is not valid. 'user_id' is a required property",
            message,
        )


class TestRecommendCoupons(unittest.TestCase):
    def test_recommend_coupons(self):
        user = {
            "user_id": 1,
            "birth_year": 1990,
            "country": "Italy",
            "sport_pref": "Football",
            "currency": "EUR",
            "registration_date": "2022-03-01T00:00:00",
        }
        events = [
            {
                "event_id": "E001",
                "league": "Premier League",
                "sport": "Football",
                "country": "England",
                "begin_timestamp": "2022-04-10 15:00:00+00:00",
                "end_timestamp": "2022-04-10 17:00:00+00:00",
                "participants": ["Liverpool", "Chelsea"],
            },
            {
                "event_id": "E002",
                "league": "La Liga",
                "sport": "Football",
                "country": "Spain",
                "begin_timestamp": "2022-04-10 20:00:00+02:00",
                "end_timestamp": "2022-04-10 22:00:00+02:00",
                "participants": ["Real Madrid", "Barcelona"],
            },
            {
                "event_id": "E003",
                "league": "Serie A",
                "sport": "Football",
                "country": "Italy",
                "begin_timestamp": "2022-04-12 21:00:00+02:00",
                "end_timestamp": "2022-04-12 23:00:00+02:00",
                "participants": ["Juventus", "AC Milan"],
            },
        ]
        coupons = [
            {
                "coupon_id": "C001",
                "selections": [{"event_id": "E001", "odds": 2.0}],
                "stake": 10.0,
                "timestamp": "2022-04-08T09:30:00",
                "user_id": 1,
            },
            {
                "coupon_id": "C002",
                "selections": [
                    {"event_id": "E002", "odds": 1.5},
                    {"event_id": "E003", "odds": 2.0},
                ],
                "stake": 5.0,
                "timestamp": "2022-04-08T10:30:00",
                "user_id": 2,
            },
            {
                "coupon_id": "C003",
                "selections": [{"event_id": "E003", "odds": 2.5}],
                "stake": 20.0,
                "timestamp": "2022-04-08T11:30:00",
                "user_id": 3,
            },
        ]
        result = recommend_coupons(user, coupons, events)
        expected_result = [
            {
                "coupon_id": "C003",
                "selections": [{"event_id": "E003", "odds": 2.5}],
                "stake": 20.0,
                "timestamp": "2022-04-08T11:30:00",
                "user_id": 3,
                "odds": 2.5,
            }
        ]
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
