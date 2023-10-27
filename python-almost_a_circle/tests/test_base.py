#!/usr/bin/python3
"""Unittest for the Base class"""

import unittest
from models.base import Base
from io import StringIO


class TestBase(unittest.TestCase):
    """Test cases for the Base class"""

    def test_init(self):
        """Test initialization of the Base class"""
        # Test case 1: Default initialization, id should be 1
        b = Base()
        self.assertEqual(b.id, 1)

        # Test case 2: Custom initialization with id=69
        b = Base(69)
        self.assertEqual(b.id, 69)

        # Test case 3: Testing the to_json_string method with an empty list
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

        # Test case 4: Testing the to_json_string method with None
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

        """
            Test case 5: Testing the to_json_string
            method with a list containing a dictionary
        """
        d = [{'id': 36}]
        result = Base.to_json_string(d)
        self.assertEqual(result, '[{"id": 36}]')

        # Test case 6: Testing the from_json_string method with an empty string
        result = Base.from_json_string("[]")
        self.assertEqual(result, [])

        # Test case 7: Testing the from_json_string method with None
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

        """
            Test case 8: Testing the from_json_string
            method with a JSON-formatted string
        """
        d = '[{"id": 36}]'
        result = Base.from_json_string(d)
        self.assertEqual(result, [{"id": 36}])


if __name__ == '__main__':
    unittest.main()
