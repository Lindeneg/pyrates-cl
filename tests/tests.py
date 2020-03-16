import unittest
from typing import Sequence, Mapping

from pyrates.pyrates import PyRates
from pyrates.rate.rate import Rate
from pyrates.util.constants import Constants


class TestPyRates(unittest.TestCase):
    
    def __init__(self, methodName="TestPyRates"):
        super().__init__(methodName)
        pyrates = PyRates()
        self.conversionDefault = pyrates.Convert()
        self.conversionArguments = pyrates.Convert("dkk", "aud", 122.5)
        self.rates = pyrates.GetRates()
        self.rate = pyrates.GetRate("usd")
        self.ratesObjects = pyrates.GetRateObjects()
        self.rateObject = pyrates.GetRateObject("dkk")

    def testConversionDefaultIsFloat(self):
        self.assertIsInstance(self.conversionDefault, float)

    def testConversionArgumentsIsFloat(self):
        self.assertIsInstance(self.conversionArguments, float)

    def testGetRatesReturnsSequence(self):
        self.assertIsInstance(self.rates, Sequence)

    def testGetRateReturnsMapping(self):
        self.assertIsInstance(self.rate, Mapping)

    def testGetRateObjectsReturnsSequence(self):
        self.assertIsInstance(self.ratesObjects, Sequence)

    def testGetRateObjectReturnsRate(self):
        self.assertIsInstance(self.rateObject, Rate)

    def testRatePropertyFromEuroReturnsFloat(self):
        self.assertIsInstance(self.rateObject.fromEuro, float)

    def testRatePropertyToEuroReturnsFloat(self):
        self.assertIsInstance(self.rateObject.toEuro, float)

    def testGetRatesLengthIsEqualToSupportedCurrencies(self):
        self.assertEqual(len(self.rates), len(Constants.currencies))

    def testGetRateObjectsLengthIsEqualToSupportedCurrenciesPlusOne(self):
        self.assertEqual(len(self.ratesObjects), len(Constants.currencies)+1)

    def testGetRateReturnsCorrectRate(self):
        self.assertEqual(self.rate[Constants.name].upper(), "US DOLLAR")

    def testGetRateReturnsCorrectCode(self):
        self.assertEqual(self.rate[Constants.currencyCode].upper(), "USD")

    def testGetRateObjectReturnsCorrectRate(self):
        self.assertEqual(self.rateObject.name.upper(), "DANISH KRONE")

    def testGetRateObjectReturnsCorrectCode(self):
        self.assertEqual(self.rateObject.code.upper(), "DKK")


if __name__ == "__main__":
    unittest.main()
