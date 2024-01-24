"""To run these tests, your MoneyFactory needs to be able to create
2 distinct factories:
   "TH" - factory for Thai money
   "MY" - factory for Malaysian money (Ringgit)
"""

import unittest

from money_factory import *

class MoneyFactoryTest(unittest.TestCase):

    def setUp(self):
        pass

    def testFactoryIsUnique(self):
        """There should be only 1 instance of a Factory for a given country code."""
        factory1 = MoneyFactory.get_instance("TH")
        malay_factory = MoneyFactory.get_instance("MY")
        factory2 = MoneyFactory.get_instance("TH")
        self.assertIs(factory1, factory2)
        # but Thai Factory not same as Malay Factory
        self.assertIsNot(factory1, malay_factory)
        
    def testFactoryInstance(self):
        """Factory method returns subclasses of base class."""
        factory = MoneyFactory.get_instance("TH")
        self.assertIsInstance(factory, MoneyFactory)

    def testValidMalayMoney(self):
        """Test that factory produces valid Malaysian money."""
        factory = MoneyFactory.get_instance("MY")
        coins = [0.01, 0.1, 0.2, 0.5]
        for value in coins:
            cash = factory.create_cash(value)
            self.assertIsInstance(cash, Coin)
            self.assertEqual(value, cash.value)
            self.assertEqual("Ringgit", cash.currency)
        notes = [1, 5, 10, 20, 50, 100]
        for value in notes:
            cash = factory.create_cash(value)
            self.assertIsInstance(cash, Banknote)
            self.assertEqual(value, cash.value)
            self.assertEqual("Ringgit", cash.currency)

    def testInvalidMalayMoney(self):
        """Should raise exception when an invalid value is given."""
        factory = MoneyFactory.get_instance("MY")
        values = [0.25, 2, 25, 500, 1000]

        for value in values:
            try:
                cash = factory.create_cash(value)
                self.fail(f"Should raise ValueError for value={value}")
            except ValueError:
                # ok
                pass
