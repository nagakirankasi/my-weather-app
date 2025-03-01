import unittest
from src.weather import get_weather

class TestWeatherAPI(unittest.TestCase):
    def test_valid_city(self):
        weather = get_weather("London")
        self.assertIn("temperature", weather)

    def test_invalid_city(self):
        weather = get_weather("InvalidCity")
        self.assertIn("error", weather)

if __name__ == "__main__":
    unittest.main()
