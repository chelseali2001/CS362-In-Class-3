import unittest
import leapYear

class SimpleTest(unittest.TestCase):
    def test_leapYear(self):
        self.assertEqual(leapYear.ly(0), "is a leap year")

    def test_leapYear(self):
        self.assertEqual(leapYear.ly(100), "is not a leap year")
    
    def test_leapYear(self):
        self.assertEqual(leapYear.ly(400), "is a leap year")

    def test_leapYear(self):
        self.assertEqual(leapYear.ly(2004), "is a leap year")
    
    def test_leapYear(self):
        self.assertEqual(leapYear.ly("2004"), "is a leap year")