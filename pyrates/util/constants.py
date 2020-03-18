from typing import Mapping, Callable, Union, Any, Sequence, MutableMapping
from os import path
from random import randint


def GetUserAgent() -> str:
    data: Sequence[str] = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
        "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"
    ]
    agent: str = data[randint(0, len(data)-1)]
    return agent


GetXPath: Callable[[int], str] = lambda i: f"/html/body/div[2]/div/div[3]/div[1]/div/div[1]/div[1]/table[2]/tbody/tr/td[{i}]"


class Types:
    DictableRate = Mapping[str, Union[str, float]]
    File = Mapping[str, Union[Sequence[DictableRate], float]]
    URLResponse = Union[bytes, Mapping[str, Any]]
    Number = Union[int, float]


class Constants:
    url: str = "https://www.x-rates.com/table/?from=EUR&amount=1"
    header: MutableMapping[str, str] = {
        "User-Agent": GetUserAgent(),
        "Accept": "*/*"
    }
    dataPath: str = str(path.join(path.dirname(__file__), '..', 'data'))
    logPath: str = str(path.join(path.dirname(__file__), '..', 'log'))
    xpathName: str = GetXPath(1)
    xpathFrom: str = GetXPath(2)
    xpathTo: str = GetXPath(3)
    source: str = "x-rates.com"
    name: str = "name"
    currencyCode: str = "currency_code"
    fromEuro: str = "from_euro"
    data: str = "data"
    timestamp: str = "timestamp"
    toEuro: str = "to_euro"
    defaultFrom: str = "eur"
    defaultFromName: str = "euro"
    defaultTo: str = "usd"
    defaultAmount: float = 1.0
    defaultDict: Mapping[str, None] = {"data": None}
    logFileName: str = "pyrates.log"
    dataFileName: str = "data.json"
    rateStringLength: int = 31
    nameStringLength: int = 9
    cacheLimitInSeconds: int = 1800
    currencies: Mapping[str, str] = {
        "ARS": "Argentine Peso",
        "AUD": "Australian Dollar",
        "BHD": "Bahraini Dinar",
        "BWP": "Botswana Pula",
        "BRL": "Brazilian Real",
        "BND": "Bruneian Dollar",
        "BGN": "Bulgarian Lev",
        "CAD": "Canadian Dollar",
        "CLP": "Chilean Peso",
        "CNY": "Chinese Yuan Renminbi",
        "COP": "Colombian Peso",
        "HRK": "Croatian Kuna",
        "CZK": "Czech Koruna",
        "DKK": "Danish Krone",
        "HKD": "Hong Kong Dollar",
        "HUF": "Hungarian Forint",
        "ISK": "Icelandic Krona",
        "INR": "Indian Rupee",
        "IDR": "Indonesian Rupiah",
        "IRR": "Iranian Rial",
        "ILS": "Israeli Shekel",
        "JPY": "Japanese Yen",
        "KZT": "Kazakhstani Tenge",
        "KRW": "South Korean Won",
        "KWD": "Kuwaiti Dinar",
        "LYD": "Libyan Dinar",
        "MYR": "Malaysian Ringgit",
        "MUR": "Mauritian Rupee",
        "MXN": "Mexican Peso",
        "NPR": "Nepalese Rupee",
        "NZD": "New Zealand Dollar",
        "NOK": "Norwegian Krone",
        "OMR": "Omani Rial",
        "PKR": "Pakistani Rupee",
        "PHP": "Philippine Peso",
        "PLN": "Polish Zloty",
        "QAR": "Qatari Riyal",
        "RON": "Romanian New Leu",
        "RUB": "Russian Ruble",
        "SAR": "Saudi Arabian Riyal",
        "SGD": "Singapore Dollar",
        "ZAR": "South African Rand",
        "LKR": "Sri Lankan Rupee",
        "SEK": "Swedish Krona",
        "CHF": "Swiss Franc",
        "TWD": "Taiwan New Dollar",
        "THB": "Thai Baht",
        "TTD": "Trinidadian Dollar",
        "TRY": "Turkish Lira",
        "AED": "Emirati Dirham",
        "GBP": "British Pound",
        "USD": "US Dollar",
        "VEF": "Venezuelan Bolivar"   
    }


class GUI:
    title: str = "PyRatesGUI 0.2"
    source: str = "https://github.com/lindeneg/pyrates-cl"
    defaultUtilityContent: str = "PyRatesGUI - 0.2\n\nMake a Conversion.."
    defaultMainView: str = "default"
    supportedRatesView: str = "supportedRates"
    height: int = 800
    width: int = 800
    conversionHeight: int = 150
    conversionWidth: int = 645
    labelWidth: int = 20
    xOffset: int = 10
    yOffset: int = 5
    utilityXOffset: int = 300
    utilityYOffset: float = height-(height * 0.9)+20
    utilityContentHeight: int = 9
    utilityContentWidth: int = 44
    componentTableHeight: int = 32
    backgroundColor: str = "#000000"
    textColor: str = "#ffffff"
    buttonColor: str = "#666666"
    buttonWidth: int = 16
    buttonYPadding: int = 20
    amountInputLabelSpacing: int = 4
    fromInputLabelSpacing: int = 15
    toInputLabelSpacing: int = 21
    resizeable: bool = False