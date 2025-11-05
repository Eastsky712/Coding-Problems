import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):
    """Test for class Employee"""

    def setUp(self):
        """Creates a default employee"""
        self.emp = Employee('Bob', 'Johnson', 72_000)

    def test_give_default_raise(self):
        self.emp.give_raise()
        self.assertEqual(self.emp.salary, 77_000)
    
    def test_give_custom_raise(self):
        self.emp.give_raise(10_000)
        self.assertEqual(self.emp.salary, 82_000)


if __name__ == '__main__':
    unittest.main()