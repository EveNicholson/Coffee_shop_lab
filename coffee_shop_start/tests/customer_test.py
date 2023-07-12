import unittest
from src.customer import Customer
from src.drink import Drink
class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Sky", 500)
        self.water = Drink("Spring Water", 10)

    def test_customer_has_name(self):
       
        expected = "Sky"
        actual = self.customer.name
        self.assertEqual(expected, actual)

    def test_wallet(self):
        self.assertEqual(500, self.customer.wallet)


    def test_customer_can_buy_drink(self):
        self.customer.buy_drink(self.water)
        self.assertEqual(490, self.customer.wallet)
           
    