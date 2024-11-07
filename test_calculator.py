import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def testadd1(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    #Add the following test methods to the TestCalculator class:

    def testadd2(self):
        self.assertEqual(self.calc.add(77, 33), 110)

    def testsubtract1(self):
        self.assertEqual(self.calc.subtract(4, 6), 2)
    def testsubtract2(self):
        self.assertEqual(self.calc.subtract(47, 35), -12)

    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(7, 5), 35)
    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(0, 6), 0)

    def test_divide1(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
    def test_divide2(self):
        self.assertEqual(self.calc.divide(60, 5), 12)

    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(6, 2), 0)
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(8, 3), 2)

if __name__ == '__main__':
    unittest.main()