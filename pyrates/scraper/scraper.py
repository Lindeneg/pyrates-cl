from typing import Sequence, MutableSequence, Tuple, List
from time import time
from re import findall

from lxml import html
from lxml.html import HtmlElement

from pyrates.util.url_manager import URLManager
from pyrates.util.constants import Types, Constants
from pyrates.logger.logger import mLogger


class Scraper:
    """
    A class for webscraping currency rates from x-rates

    Static Methods:

        ScrapeRates() -> Tuple
    """
    @staticmethod
    def ScrapeRates() -> Tuple[Sequence[Types.DictableRate], float]:
        """
        Webscrapes x-rates for updated rates

        Return a Tuple containing the data and a timestamp

            Returns:
                    data (Tuple)    : Tuple containing data and timestamp
        """
        rates: Sequence[Types.DictableRate] = []
        timestamp: float = 0
        request: Types.URLResponse = URLManager(url=Constants.url, header=Constants.header)
        if isinstance(request, bytes):
            response: HtmlElement = html.fromstring(request)
            rawNames: MutableSequence[str] = FindXPath(response, Constants.xpathName)
            rawFromEuros: MutableSequence[str] = FindXPath(response, Constants.xpathFrom)
            rawToEuros: MutableSequence[str] = FindXPath(response, Constants.xpathTo)
            
            names: Sequence[List[str]] = GetNames(rawNames)
            abbreviations: Sequence[List[str]] = [[i] for i in Constants.currencies.keys()]
            fromEuros: Sequence[List[str]] = [FindFloats(str(i)) for i in rawFromEuros]
            toEuros:  Sequence[List[str]] = [FindFloats(str(i)) for i in rawToEuros]

            mRates: Sequence[Sequence[str]] = [
                name + abbreviation + fromEuro + toEuro for
                name, abbreviation, fromEuro, toEuro in zip(
                    names, abbreviations, fromEuros, toEuros
                )
            ]
            rates, timestamp = MakeRatesDictable(mRates)
        else:
            mLogger.critical(f"ScrapeRatesExpection: response: {request}, handled: {rates}")
        return rates, timestamp


def GetNames(rawNames: Sequence[str]) -> Sequence[List[str]]:
    """
    Matches a sequence of strings to a given country-name found in Constants.currencies
    
    Return a list of lists of strings containing the matched names

        Returns:
                names (Sequence)    : List of lists of strings containing matched names
    """
    names: MutableSequence[List[str]] = []
    name: str
    for name in Constants.currencies.values():
        otherName: str
        for otherName in rawNames:
            match: Sequence[str] = findall(name, otherName)
            if len(match) > 0:
                names.append([match[0]])
    return names


def MakeRatesDictable(rates: Sequence[Sequence[str]]) -> Tuple[Sequence[Types.DictableRate], float]:
    """
    Converts a list of lists of stringified rate information into a Tuple containing a Sequence of rate maps and a timestamp float

        Returns:
                data (Tuple)    : Tuple containing data and timestamp
    """
    mRates: MutableSequence[Types.DictableRate] = []
    mTime: float = time()
    rate: Sequence[str]
    for rate in rates:
        mRates.append(
            {
                Constants.name: rate[0], 
                Constants.currencyCode: rate[1], 
                Constants.fromEuro: float(rate[2]), 
                Constants.toEuro: float(rate[3])
            }
        )
    return mRates, mTime


def FindFloats(inputString: str) -> List[str]:
    """
    Finds a floating point number in a given string

        Returns:
                result (Sequence)    : Sequence of strings containing the float(s) found
    """
    return [i for i in findall(r"[-+]?\d*\.\d+|\d+", inputString)]


def FindXPath(res: HtmlElement, xPath: str) -> MutableSequence[str]:
    """
    Find the content in a xpath in a given HtmlElement

    Convert the result to a string and append it to a Sequence

        Returns:
                result (Sequence)    : Sequence of strings containing the content found at the given xpath
    """
    return [str(html.tostring(i)) for i in res.xpath(xPath)]
