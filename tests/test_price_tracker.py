import unittest
from price_tracker import get_crypto_price

class TestPriceTracker(unittest.TestCase):

    def test_valid_symbol(self):
        """Tests that a valid cryptocurrency symbol returns a price."""
        price = get_crypto_price('bitcoin')
        self.assertIsNotNone(price)
        self.assertIsInstance(price, float)

    def test_invalid_symbol(self):
        """Tests that an invalid symbol returns None."""
        price = get_crypto_price('invalid_coin')
        self.assertIsNone(price)

if __name__ == '__main__':
    unittest.main()
