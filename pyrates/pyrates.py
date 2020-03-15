from typing import Sequence, Union, Optional, Any
from time import time
from datetime import datetime

from pyrates.scraper.scraper import Scraper
from pyrates.rate.rate import Rate
from pyrates.util.file_manager import FileManager
from pyrates.util.constants import Types, Constants
from pyrates.logger.logger import mLogger


class PyRates:
    """
    A class to hold methods appropiate for doing currency conversions

    Methods:

        Convert(fromRate, toRate, amount)   -> float
        GetRates()                          -> Sequence
        GetRate(rate)                       -> Mapping
        GetRateObjects()                    -> Sequence
        GetRateObject(rate)                 -> Rate
        GetTimeString()                     -> string
        GetTimestamp()                      -> float
        UpdateRates()                       -> bool
        GetSupportedCurrencies()            -> Mapping
    """
    def __init__(self) -> None:
        self.__rates: Sequence[Rate] = []
        self.__dictableRates: Sequence[Types.DictableRate] = []
        self.__timestamp: float = 0
        self.__Init()
        if len(self.__dictableRates) <= 0 or len(self.__rates) <= 0 or self.__timestamp == 0:
            print(self.__dictableRates)
            raise Exception("PyRatesInitError: Failed to initialize. Check '%s/%s' for further inspection." % (Constants.logPath, Constants.logFileName))

    def Convert(
        self, 
        fromRate: Union[str, Rate] = Constants.defaultFrom, 
        toRate: Union[str, Rate] = Constants.defaultTo, 
        amount: float = Constants.defaultAmount
        ) -> float:
        """
        Converts a given amount of fromRate into toRate

            Parameters:
                    fromRate   (str, Rate): Three letter currencycode string or a Rate object, default: "eur"
                    toRate     (str, Rate): Three letter currencycode string or a Rate object, default: "usd"
                    amount     (float)    : The amount to convert,                             default: 1.0

            Returns:
                    conversion (float)    : The amount of fromRate converted into toRate
        """
        mFromRate: Optional[Rate]
        mToRate: Optional[Rate]
        if not isinstance(fromRate, Rate):
            mFromRate = Rate.GetRate(fromRate, self.__rates)
        else:
            mFromRate = fromRate
        if not isinstance(toRate, Rate):
            mToRate = Rate.GetRate(toRate, self.__rates)
        else:
            mToRate = toRate
        if isinstance(mFromRate, Rate) and isinstance(mToRate, Rate):
            return mFromRate.Convert(mToRate, amount)
        raise Exception(f"PyRatesConversionError: Failed to convert {amount} {fromRate} -> {toRate}. Check '{Constants.logPath}/{Constants.logFileName}' for further inspection.")
    
    def GetRates(self) -> Sequence[Types.DictableRate]:
        """
        Return a sequence of dictionaries with rate information

            Returns:
                    rates (Sequence)  : Sequence of rate dictionaries
        """
        return self.__dictableRates

    def GetRate(self, rate: str) -> Optional[Types.DictableRate]:
        """
        Return a dictionary with the given rate information
        
        Return None if the rate could not be found

            Parameters:
                    rate   (str)                 : Three letter currencycode string, default: "usd"

            Returns:
                    result (Sequence, None)      : Dictionary with given rate information or None
        """
        return Rate.GetDictableRate(rate, self.__dictableRates)

    def GetRateObjects(self) -> Sequence[Rate]:
        """
        Return a sequence of Rate objects

            Returns:
                    rates (Sequence)  : Sequence of Rate objects
        """
        return self.__rates

    def GetRateObject(self, rate: str) -> Optional[Rate]:
        """
        Return a Rate object.
        
        Return None if the rate could not be found.

            Parameters:
                    rate   (str)                 : Three letter currencycode string, default: "usd"

            Returns:
                    result (Rate, None)          : Rate object or None
        """
        return Rate.GetRate(rate, self.__rates)


    def GetTimeString(self) -> str:
        """
        Return the timestamp converted into a UTC timestring

            Returns:
                    timestring (string)  : UTC timestring generated from the timestamp representing the last time the rates were updated
        """
        return f"{datetime.utcfromtimestamp(self.__timestamp).strftime('%Y-%m-%d %H:%M:%S')} UTC"

    def GetTimestamp(self) -> float:
        """
        Return the current time in seconds since the Epoch. Fractions of a second may be present if the system clock provides them.

            Returns:
                    timestamp (float)  : Floating number representing the last time the rates were updated
        """
        return self.__timestamp
    
    def UpdateRates(self) -> bool:
        """
        Rates must be older than the 'cacheLimitInSeconds' (default: 1800) value found in util/constants.py in order to update

        Return True/False depending upon successful update of rates

            Returns:
                    result (bool)  : Did the rates update?
        """
        if self.__RatesWithinLimit(self.__timestamp):
            return False
        self.__UpdateRates()
        return True
    
    def __Init(self) -> None:
        """
        Run everytime a new instance is created. Find data to be used

        If no data can be found or the data that can be found is older than 'cacheLimitInSeconds' (default: 1800),
        
        then new data will be fetched from x-rates using the scraper object

            Returns:
                    None
        """
        data: Optional[Types.File] = FileManager(Constants.dataPath, Constants.dataFileName)
        if data is not None and data[Constants.data] and data[Constants.timestamp]:
            timestamp: Any = data[Constants.timestamp]
            dictData: Any = data[Constants.data]
            if isinstance(timestamp, float) and isinstance(dictData, Sequence) and self.__RatesWithinLimit(timestamp):
                self.__dictableRates = dictData
                self.__timestamp = timestamp
                self.__rates = Rate.GenerateRates(self.__dictableRates)
                return
        self.__UpdateRates()

    def __UpdateRates(self) -> None:
        """
        Update attributes of class instance and save data locally in a JSON file 

            Returns:
                    None
        """
        self.__dictableRates, self.__timestamp = Scraper.ScrapeRates()
        self.__rates = Rate.GenerateRates(self.__dictableRates)
        FileManager(Constants.dataPath, Constants.dataFileName, {Constants.data: self.__dictableRates, Constants.timestamp: self.__timestamp})

    def __RatesWithinLimit(self, timestamp: float) -> bool:
        """
        Check to see if the rates are within 'cacheLimitInSeconds' (default: 1800)

        Return True if so, otherwise return False

            Returns:
                    result (bool)  : Returns a bool representing if rates are within the limit
        """
        return abs(time() - timestamp) < Constants.cacheLimitInSeconds

    def __repr__(self) -> str:
        return f"""
|==========================================================================|
| CURRENCY | 1.0 EUR                        | INV 1.0
|==========================================================================|
{"".join([rate.GetTableString() for rate in self.__rates if not rate.code.upper() == "EUR"])}
"""
