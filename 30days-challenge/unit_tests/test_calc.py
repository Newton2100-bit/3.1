import unittest
import calc

class test_calc(unittest.TestCase):
    def test_add(self):# Note that the naming conventon for test methods is test_ failure to that no tests actually taeks place
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(10, 4), 14)
        self.assertEqual(calc.add(-1, 4), 3)
        self.assertEqual(calc.add(30, 4), 34)

    def test_substract(self):# Note that the naming conventon for test methods is test_ failure to that no tests actually taeks place
        self.assertEqual(calc.substract(10, 5), 5)
        self.assertEqual(calc.substract(10, 4), 6)
        self.assertEqual(calc.substract(-6, 4), -10)
        self.assertEqual(calc.substract(-11, -13), 1)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 20), 200)

    def test_divide(self):
        self.assertEqual(calc.divide(20, 10), 2)

        # Testing that actually dividing by zero raises an error
        # Method 1
        self.assertRaises(ValueError, calc.divide, 10, 0)
        self.assertRaises(ValueError, calc.divide, 20, 0)

        # Method 20 
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
