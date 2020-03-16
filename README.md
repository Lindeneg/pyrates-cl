PyRates
=============
Convert rates between 53 currencies
-------------

To do:
- Implement GUI and CLI
- Implement unit tests


# Installation

with pip
```shell
$ python -m pip install pyrates-cl
```

with source

```shell
$ git clone https://github.com/Lindeneg/pyrates-cl && cd pyrates-cl
$ python setup.py install
```

# Usage
```python
from pyrates import PyRates

pyrates = PyRates()
```
```python
# pyrates.Convert(fromRate, toRate, amount) -> float

"""
| Arguments | Type             | Required | Default |
|-----------|------------------|----------|---------|
| fromRate  | Union[str, Rate] | No       | "eur"   |
| toRate    | Union[str, Rate] | No       | "usd"   |
| amount    | float            | No       | 1.0     |
"""
>>> pyrates.Convert(fromRate="nok", toRate="aud", amount=122.5)
19.574542061193018


# pyrates.GetRates() -> Sequence[Mapping[str, Union[str, float]]]
>>> pyrates.GetRates()
[...
    {
        "name": "British Pound",
        "currency_code": "GBP",
        "from_euro": 0.901865,
        "to_euro": 1.108813
    }
...]


# pyrates.GetRate(rate) -> Optional[Mapping[str, Union[str, float]]]
"""
| Arguments | Type             | Required | Default |
|-----------|------------------|----------|---------|
| rate      | str              | Yes      |    -    |
"""
>>> pyrates.GetRate(rate="dkk")
{
    "name": "Danish Krone", 
    "currency_code": "DKK", 
    "from_euro": 7.473825, 
    "to_euro": 0.1338
}


# pyrates.GetRateObjects() -> Sequence[Rate]
>>> pyrates.GetRateObjects()
[...
    <pyrates.rate.rate.Rate object>
...]


# pyrates.GetRateObject(rate) -> Optional[Rate]
"""
| Arguments | Type             | Required | Default |
|-----------|------------------|----------|---------|
| rate      | str              | Yes      |    -    |
"""
>>> pyrates.GetRateObject(rate="dkk")
<pyrates.rate.rate.Rate object>


# pyrates.GetTimestamp() -> float
>>> pyrates.GetTimestamp()
1584304647.245822


# pyrates.GetTimeString() -> str
>>> pyrates.GetTimeString()
'2020-03-15 20:37:27 UTC'


# pyrates.UpdateRates() -> bool
"""
Rates are only updated, if the difference between the current time and the saved timestamp
is more than the 'cacheLimitInSeconds' value specified in constants.py
Default value for 'cacheLimitInSeconds' is 1800

pyrates.UpdateRates() returns True if rates were updated, otherwise returns False
"""
>>> pyrates.UpdateRates()
True


# pyrates.GetSupportedCurrencies() -> Mapping[str, str]
>>> pyrates.GetSupportedCurrencies()
{
    ...
    "GBP": "British Pound",
    "USD": "US Dollar",
    ...
}


# pyrates.__repr__() -> str
>>> print(pyrates)
'''
SOURCE: x-rates.com
TIME  : 2020-03-15 20:53:20 UTC

|==========================================================================|
| CURRENCY | 1.0 EUR                        | INV 1.0 EUR
|==========================================================================|
| [...]    | [...]                          | [...]
|==========================================================================|
| DKK      | 7.473316                       | 0.133809
|==========================================================================|
| HKD      | 8.599625                       | 0.116284
|==========================================================================|
| HUF      | 339.243118                     | 0.002948
|==========================================================================|
| [...]    | [...]                          | [...]
|==========================================================================|
'''
```