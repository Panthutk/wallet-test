import unittest
from wallet import Wallet
from cash import *
# do we need to import Money?  It should be either imported or defined in cash.py.

# default currency
CURRENCY = "Baht"
CURRENCY2 = "Ringgit"
class WalletTest(unittest.TestCase):

    def setUp(self):
        self.wallet = Wallet()

    def test_wallet_constructor(self):
        """A new Wallet should be empty."""
        self.assertTrue(self.wallet.is_empty())
        self.assertEqual(0, len(self.wallet.get_items()))
    
    def test_zero_value_wallet(self):
        """Value of a new wallet should be Money(0,currency), not 0 (float)."""
        self.assertEqual(Money(0,CURRENCY), self.wallet.balance(CURRENCY))

    def test_deposit(self):
        """Can deposit a single item."""
        coin = Coin(5, CURRENCY)
        self.wallet.deposit(coin)
        self.assertFalse(self.wallet.is_empty())
        items = self.wallet.get_items()
        self.assertListEqual([coin], items)

    def test_balance_one_currency(self):
        """Test balance after deposits of a single currency."""
        self.wallet.deposit(Coin(10, CURRENCY))
        self.assertEqual(Money(10,CURRENCY), self.wallet.balance(CURRENCY))
        self.wallet.deposit(Coin(5, CURRENCY))
        self.assertEqual(Money(15,CURRENCY), self.wallet.balance(CURRENCY))
        self.wallet.deposit(Coin(5, CURRENCY))
        self.assertEqual(Money(20,CURRENCY), self.wallet.balance(CURRENCY))
        self.wallet.deposit(Banknote(100, CURRENCY))
        self.assertEqual(Money(120,CURRENCY), self.wallet.balance(CURRENCY))    

    def test_balance_two_currencies(self):
        """Wallet accepts deposits of different currencies and balance computed for each currency."""
        self.wallet.deposit(Coin(10, CURRENCY))
        self.assertEqual(Money(10,CURRENCY), self.wallet.balance(CURRENCY))

        self.wallet.deposit(Coin(5, CURRENCY2))
        self.assertEqual(Money(10,CURRENCY), self.wallet.balance(CURRENCY))
        self.assertEqual(Money(5,CURRENCY2), self.wallet.balance(CURRENCY2))

        self.wallet.deposit(Coin(20, CURRENCY))
        self.assertEqual(Money(30,CURRENCY), self.wallet.balance(CURRENCY))

        self.wallet.deposit(Banknote(100, CURRENCY2))
        self.assertEqual(Money(105,CURRENCY2), self.wallet.balance(CURRENCY2))
        self.assertEqual(Money(30,CURRENCY), self.wallet.balance(CURRENCY))