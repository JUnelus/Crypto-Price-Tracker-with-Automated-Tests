import unittest
from price_tracker import get_crypto_prices

class TestPriceTracker(unittest.TestCase):

    def test_valid_symbols(self):
        """Tests that valid cryptocurrency symbols return prices."""
        symbols = ['bitcoin', 'ethereum']
        prices = get_crypto_prices(symbols)

        # Check if prices were returned for all symbols
        self.assertEqual(len(prices), len(symbols))

        # Check if prices are floats and not None
        for symbol in symbols:
            self.assertIsNotNone(prices[symbol])
            self.assertIsInstance(prices[symbol], float)

    def test_mixed_symbols(self):
        """Tests a mix of valid and invalid symbols."""
        symbols = ['bitcoin', 'invalid_coin']
        prices = get_crypto_prices(symbols)

        # Check if the valid symbol has a price and the invalid one is None
        self.assertIsNotNone(prices['bitcoin'])
        self.assertIsInstance(prices['bitcoin'], float)
        self.assertIsNone(prices['invalid_coin'])

    def test_empty_list(self):
        """Tests an empty list of symbols."""
        symbols = []
        prices = get_crypto_prices(symbols)

        # Check if an empty dictionary is returned
        self.assertEqual(prices, {})

if __name__ == '__main__':
    unittest.main()