import unittest 
from employee import Employee

class test_employee(unittest.TestCase):

    def setUpClass(cls):
        pass

    def tearDownClass(cls):
        pass

    def setUp(self):
        self.emp1 = Employee('Corey', 'Schafer', 50_000)
        self.emp2 = Employee('Sue', 'Smith', 60_000)

    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.emp1.email,'Corey.Schafer@email.com')
        self.assertEqual(self.emp2.email, 'Sue.Smith@email.com')

        self.emp1.first = 'John'
        self.emp2.first = 'newton'

        self.assertEqual(self.emp1.email,'John.Schafer@email.com')
        self.assertEqual(self.emp2.email, 'newton.Smith@email.com')




if __name__ == '__main__':
    unittest.main()


