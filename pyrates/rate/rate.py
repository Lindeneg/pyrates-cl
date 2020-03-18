from __future__ import annotations
from typing import MutableSequence, Sequence, Mapping, Union, Optional, Any

from pyrates.util.constants import Types, Constants
from pyrates.logger.logger import mLogger


class Rate:
    """
    A class to hold methods and attributes for any given rate

    Properties:

        name                             -> string
        code                             -> string
        fromEuro                         -> float
        toEuro                           -> float

    Methods:

        Convert(toRate, amount)          -> float
        GetTableString()                 -> string
    
    Static Methods:

        GetRate(rateCode, rates)         -> Rate
        GetDictableRate(rateCode, rates) -> Mapping
        GenerateRates(data)              -> Sequence
    """
    def __init__(self, name: str, code: str, fromEuro: float, toEuro: float) -> None:
        self.__name: str = name
        self.__code: str = code
        self.__fromEuro: float = fromEuro
        self.__toEuro: float = toEuro

    @property
    def name(self) -> str:
        return self.__name

    @property
    def code(self) -> str:
        return self.__code

    @property
    def fromEuro(self) -> float:
        return self.__fromEuro

    @property
    def toEuro(self) -> float:
        return self.__toEuro

    @staticmethod
    def GetRate(rateCode: str, rates: Sequence[Rate]) -> Optional[Rate]:
        """
        Return a Rate object.
        
        Return None if the rate could not be found.

            Parameters:
                    rateCode (str)                 : Three letter currencycode string
                    rates    (Sequence)            : Sequence of Rate objects

            Returns:
                    result   (Rate, None)          : Rate object or None
        """
        rate: Rate
        for rate in rates:
            if rate.code.upper() == rateCode.upper():
                return rate
        mLogger.debug(f"GetRate: could not retrieve '{rateCode}' from rate sequence")
        return None

    @staticmethod
    def GetDictableRate(rateCode: str, rates: Sequence[Types.DictableRate]) -> Optional[Types.DictableRate]:
        """
        Return a dictionary with the given rate information
        
        Return None if the rate could not be found

            Parameters:
                    rateCode (str)                 : Three letter currencycode string
                    rates    (Sequence)            : Sequence of rate dictionaries

            Returns:
                    result   (Sequence, None)      : Dictionary with given rate information or None
        """
        rate: Types.DictableRate
        for rate in rates:
            name: Any = rate[Constants.currencyCode]
            if isinstance(name, str) and name.upper() == rateCode.upper():
                return rate
        mLogger.debug(f"GetDictableRate: could not retrieve '{rateCode}' from rate mapping")
        return None

    @staticmethod
    def GenerateRates(data: Sequence[Types.DictableRate]) -> Sequence[Rate]:
        """
        Generates Rate objects from a Sequence of rate dictionaries

            Parameters:
                    data    (Sequence)    : Sequence of rate dictionaries

            Returns:
                    rates   (Sequence)    : Sequence of Rate objects
        """
        if not isinstance(data, Sequence):
            mLogger.critical(f"GenerateRatesException: data is not type sequence but type '{type(data)}'")
            raise TypeError("Argument to function GenerateRates must be a of a sequence type not of type '%s'" % type(data))
        generatedRates: MutableSequence[Rate] = []
        item: Mapping[str, Union[str, float]]
        for item in data:
            rate: Rate = Rate(str(item["name"]), str(item["currency_code"]), float(item["from_euro"]), float(item["to_euro"]))
            generatedRates.append(rate)
        generatedRates.append(Rate("Euro", "EUR", 1.0, 1.0))
        return generatedRates
    
    def Convert(self, toRate: Rate, amount: float = 1) -> float:
        """
        Converts a given amount of self into toRate 

            Parameters:
                    toRate     (Rate): Rate object target for currency conversion

            Returns:
                    conversion (float)    : The amount of self converted into toRate
        """
        if isinstance(toRate, Rate):
            return (self.toEuro / toRate.toEuro) * amount
        mLogger.critical(f"ConvertException: toRate is not type Rate but type '{type(toRate)}'")
        raise TypeError("toRate argument must be of type 'Rate' and not type '%s'" % type(toRate))

    def GetTableString(self) -> str:
        """
        Generates a string to be used by PyRates __repr__ method

            Returns:
                    tableString (str)  : A string confining Rate data into a table-like structure
        """
        return f"""| {self.__Fill(self.code, Constants.nameStringLength)}| {self.__Fill(str(self.fromEuro), Constants.rateStringLength)}| {self.__Fill(str(self.toEuro), Constants.rateStringLength)}
|==========================================================================|
"""

    def __Fill(self, inputString, limit) -> str:
        """
        Used by GetTableString to generate whitespaces, such that the spacing between Rates in the table-like structure are consistent

            Parameters:
                    inputString (str): String to be filled with whitespaces
                    limit       (int): Target length of the string

            Returns:
                    result      (str): inputString filled with the appropiate amount of whitespaces
        """
        for i in range((limit - len(inputString))):
            inputString += " "
        return inputString

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Rate):
            return self.name == other.name and self.code == other.code
        mLogger.warning(f"RateEqualityException: can only compare a Rate type with another Rate, not type '{type(other)}'")
        return False
