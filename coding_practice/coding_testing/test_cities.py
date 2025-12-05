import unittest
from city_functions import get_formatted_location

class LocationsTestCase(unittest.TestCase):
    """Test for 'city_functions.py'"""

    def test_city_country(self):
        formatted_location = get_formatted_location('seoul', 'south korea')
        self.assertEqual(formatted_location, 'Seoul, South Korea')
    
    def test_city_country_population(self):
        formatted_location = get_formatted_location('santiago', 'chile', 5000000)
        self.assertEqual(formatted_location, 'Santiago, Chile - population: 5000000')

if __name__ == '__main__':
    unittest.main()