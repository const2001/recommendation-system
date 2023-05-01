import unittest
from unittest.mock import patch
from flask_controller import app

class TestRecommendationEndpoint(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.user_id = 1

    def test_get_recommendation_success(self):
        with patch("app.get_user_by_id", return_value={"user_id": self.user_id, "name": "Test User"}), \
             patch("app.recommend_coupons", return_value=[{'coupon_id': 3, 'selections': [{'event_id': 3, 'odds': 2.5}], 'stake': 20.0, 'timestamp': '2022-04-08T11:30:00', 'user_id': 3}, {'coupon_id': 1, 'selections': [{'event_id': 1, 'odds': 2.0}], 'stake': 10.0, 'timestamp': '2022-04-08T09:30:00', 'user_id': 1}, {'coupon_id': 2, 'selections': [{'event_id': 2, 'odds': 1.5}, {'event_id': 3, 'odds': 2.0}], 'stake': 5.0, 'timestamp': '2022-04-08T10:30:00', 'user_id': 2}]), \
             patch("app.validate_coupon", return_value=True):
            response = self.app.get(f"/recommendation?user_id={self.user_id}")
            self.assertEqual(response.status_code, 200)
            self.assertIn("recommended_coupons", response.json)
            self.assertIsInstance(response.json["recommended_coupons"], list)

    def test_get_recommendation_no_user_id(self):
        response = self.app.get("/recommendation")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode("utf-8"), "No user ID provided")

    def test_get_recommendation_user_not_found(self):
        with patch("app.get_user_by_id", return_value=None):
            response = self.app.get(f"/recommendation?user_id={self.user_id}")
            self.assertEqual(response.status_code, 404)
            self.assertEqual(response.data.decode("utf-8"), "No user found")

    def test_get_recommendation_validation_error(self):
        with patch("app.get_user_by_id", return_value={"user_id": self.user_id, "name": "Test User"}), \
             patch("app.recommend_coupons", return_value=[{"coupon_id": 1, "discount": "50% off"}]), \
             patch("app.validate_coupon", return_value=False):
            response = self.app.get(f"/recommendation?user_id={self.user_id}")
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.data.decode("utf-8"), "Validation error")

    def test_get_recommendation_no_coupons(self):
        with patch("app.get_user_by_id", return_value={"user_id": self.user_id, "name": "Test User"}), \
             patch("app.recommend_coupons", return_value=[]):
            response = self.app.get(f"/recommendation?user_id={self.user_id}")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data.decode("utf-8"), "No coupons recommended")

if __name__ == "__main__":
    unittest.main()
