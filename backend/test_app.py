import unittest
import json
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_hello_endpoint(self):
        response = self.client.get("/api/test")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello World!"})

    def test_add_endpoint(self):
        payload = json.dumps({"number_1": 5, "number_2": 3})
        response = self.client.post(
            "/api/add", data=payload, content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"result": 8})

    def test_add_invalid_input(self):
        payload = json.dumps({"number_1": 5})
        response = self.client.post(
            "/api/add", data=payload, content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"error": "Invalid input"})

    # Optional: Tests for additional operations
    # Uncomment and complete these tests if you implement
    # the below routes

    def test_multiply_endpoint(self):
        # Prepare test data
        payload = json.dumps({"number_1": 4, "number_2": 5})

        # Get Response from API endpoint '/api/multiply'
        response = self.client.post(
            "/api/multiply", data=payload, content_type="application/json"
        )

        # Assert equals if API response is OK (200)
        self.assertEqual(response.status_code, 200)

        # Assert equals if API response 'result' is 20 (4 * 5)
        self.assertEqual(response.json, {"result": 20})

    def test_subtract_endpoint(self):
        # Prepare test data
        payload = json.dumps({"number_1": 6, "number_2": 4})

        # Get Response from API endpoint '/api/subtract'
        response = self.client.post(
            "/api/subtract", data=payload, content_type="application/json"
        )

        # Assert equals if API response is OK (200)
        self.assertEqual(response.status_code, 200)

        # Assert equals if API response 'result' is 2 (6 - 4)
        self.assertEqual(response.json, {"result": 2})

    def test_divide_endpoint(self):
        # Prepare test data
        payload = json.dumps({"number_1": 8, "number_2": 4})

        # Get Response from API endpoint '/api/divide'
        response = self.client.post(
            "/api/divide", data=payload, content_type="application/json"
        )

        # Assert equals if API response is OK (200)
        self.assertEqual(response.status_code, 200)

        # Assert equals if API response 'result' is 2.0 (8 / 4)
        self.assertEqual(response.json, {"result": 2.0})

    # Add more tests for any additional routes created

    def test_sqrt_endpoint(self):
        # Prepare test data
        payload = json.dumps({"number": 9})

        # Get Response from API endpoint '/api/sqrt'
        response = self.client.post(
            "/api/sqrt", data=payload, content_type="application/json"
        )

        # Assert equals if API response is OK (200)
        self.assertEqual(response.status_code, 200)

        # Assert equals if API response 'result' is 3.0 (sqrt(9))
        self.assertEqual(response.json, {"result": 3.0})

    def test_power_endpoint(self):
        # Prepare test data
        payload = json.dumps({"base": 2, "exponent": 3})

        # Get Response from API endpoint '/api/power'
        response = self.client.post(
            "/api/power", data=payload, content_type="application/json"
        )

        # Assert equals if API response is OK (200)
        self.assertEqual(response.status_code, 200)

        # Assert equals if API response 'result' is 8.0 (2**3)
        self.assertEqual(response.json, {"result": 8.0})

    def test_log_endpoint(self):
        # Prepare test data
        payload = json.dumps({"number": 1})

        # Get Response from API endpoint '/api/log'
        response = self.client.post(
            "/api/log", data=payload, content_type="application/json"
        )

        # Assert equals if API response is OK (200)
        self.assertEqual(response.status_code, 200)

        # Assert equals if API response 'result' is 0.0 (ln(1))
        self.assertEqual(response.json, {"result": 0.0})


if __name__ == "__main__":
    unittest.main()
