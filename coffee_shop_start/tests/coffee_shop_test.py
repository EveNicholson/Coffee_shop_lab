import unittest
from src.coffee_shop import CoffeeShop
from src.drink import Drink

class TestCoffeeShop(unittest.TestCase):

    def setUp(self):
        self.coffee = Drink("Black Coffee", 3.95)
        self.tea = Drink("Earl Grey", 2.00)
        self.drinks = [self.coffee, self.tea]
        
        
        self.coffee_shop = CoffeeShop("The Prancing Pony", 100, self.drinks)

        
    
    def test_coffee_shop_has_name(self):
        expected = "The Prancing Pony"
        actual = self.coffee_shop.name
        self.assertEqual(expected, actual)
        # or
        self.assertEqual("The Prancing Pony", self.coffee_shop.name)

    # @unittest.skip("delete this line to run the test")
    def test_coffee_shop_has_till(self):
        self.assertEqual(100, self.coffee_shop.till)

    def test_coffee_shop_has_drinks(self):
        self.assertEqual([self.coffee, self.tea], self.coffee_shop.drinks)
        # or
        self.assertEqual(2, len(self.coffee_shop.drinks))
    def test_increase_till(self):
        self.coffee_shop.change_till_by_amount(10)
        self.assertEqual(110, self.coffee_shop.till)

    def test_decrease_till(self):
        self.coffee_shop.change_till_by_amount(-10)
        self.assertEqual(90, self.coffee_shop.till)

    
    