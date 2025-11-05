import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Test for 'name_function.py'"""

    def test_first_last_name(self):
        formatted_name = get_formatted_name('quartz', 'quote')
        self.assertEqual(formatted_name, 'Quartz Quote')
    
    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('billy', 'jones', 'bobby')
        self.assertEqual(formatted_name, 'Billy Bobby Jones')

if __name__ == '__main__':
    unittest.main()