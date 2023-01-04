import unittest
from addNumbers import addNumbers

class MyTestCase(unittest.TestCase):
    def testSimpleAddOfNumbers(self):
        a = "1 1 1"
        b = "1 1 1"
        assert addNumbers(a, b) == "2.0 2.0 2.0"
    
    def testSimpleAddOfNumbersWithDifferentStrings(self):
        a = "1 1 1"
        b = "3 4 5"
        assert addNumbers(a, b) == "4.0 5.0 6.0"

    def testAddNumbersDecimal(self):
        a = "1.5 1.2 1"
        assert addNumbers(a, a) == "3.0 2.4 2.0"

    def testAddLargeNumbers(self):
        a = "100000000000 10000000000"
        assert addNumbers(a, a) == "200000000000.0 20000000000.0"
    
    def testNegativeNumbers(self):
        a = "1 2 -3"
        b = "1 2 1"
        assert addNumbers(a, b) == "2.0 4.0 -2.0"

    def testDifferentSize(self):
        with self.assertRaises(Exception):
            a = "1 1 1"
            b = "2 2"
            addNumbers(a, b)

    def testExceptionsWithNoNumbers(self):
        with self.assertRaises(Exception) as exc_info:
            a = "1 1 1"
            b = "1 s 2"
            addNumbers(a, b)
            assert type(exc_info.value.__cause__) is ValueError


if __name__ == '__main__':
    unittest.main()
